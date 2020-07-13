"""
Project for Week 3 of "Python Data Visualization".
Unify data via common country name.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv
import math
import pygal

def reconcile_countries_by_name(plot_countries, gdp_countries):
    """
    Inputs:
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      gdp_countries  - Dictionary whose keys are country names used in GDP data

    Output:
      A tuple containing a dictionary and a set.  The dictionary maps
      country codes from plot_countries to country names from
      gdp_countries The set contains the country codes from
      plot_countries that were not found in gdp_countries.
    """
    dict_for_matching = {}
    set_exclusion = set()
    for key, value in plot_countries.items():
        for _, value2 in gdp_countries.items():
            if value in value2['Country Name']:
                dict_for_matching[key] = value
    for key, value in plot_countries.items():
        if key not in dict_for_matching:
            set_exclusion.add(key)
             
                
    return dict_for_matching, set_exclusion


def build_map_dict_by_name(gdpinfo, plot_countries, year):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for

    Output:
      A tuple containing a dictionary and two sets.  The dictionary
      maps country codes from plot_countries to the log (base 10) of
      the GDP value for that country in the specified year.  The first
      set contains the country codes from plot_countries that were not
      found in the GDP data file.  The second set contains the country
      codes from plot_countries that were found in the GDP data file, but
      have no GDP data for the specified year.
    """
    dict_common = {}
    not_found_in_gdp = set()
    have_no_gdp = set()
    for_calculation = {}
    with open(gdpinfo["gdpfile"], newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=gdpinfo["separator"], 
                                quotechar=gdpinfo["quote"])
        for row in reader:
            for_calculation[row[gdpinfo["country_name"]]] = row

    for keys in plot_countries:
        if plot_countries[keys] in for_calculation:
            if year in for_calculation[plot_countries[keys]]:
                if for_calculation[plot_countries[keys]][year] != '':
                    dict_common[keys] = math.log10(float(for_calculation[plot_countries[keys]]
                                                         [year]))
                else:
                    have_no_gdp.add(keys)
        else:
            not_found_in_gdp.add(keys)		
    return dict_common, not_found_in_gdp, have_no_gdp


def render_world_map(gdpinfo, plot_countries, year, map_file):
    """
    Inputs:
      gdpinfo        - A GDP information dictionary
      plot_countries - Dictionary whose keys are plot library country codes
                       and values are the corresponding country name
      year           - String year to create GDP mapping for
      map_file       - Name of output file to create

    Output:
      Returns None.

    Action:
      Creates a world map plot of the GDP data for the given year and
      writes it to a file named by map_file.
    """
    dict_common, not_found_in_gdp, have_no_gdp = build_map_dict_by_name(
        gdpinfo, plot_countries, year)
    chart = pygal.maps.world.World()
    chart.title = "GDP datas {}".format(year)
    chart.add('GDP for {}'.format(year), dict_common)
    chart.add('Missing from World Bank Data', not_found_in_gdp)
    chart.add('No GDP data', have_no_gdp)
    chart.render_in_browser()
    


def test_render_world_map():
    """
    Test the project code for several years.
    """
    gdpinfo = {
        "gdpfile": "isp_gdp.csv",
        "separator": ",",
        "quote": '"',
        "min_year": 1960,
        "max_year": 2015,
        "country_name": "Country Name",
        "country_code": "Country Code"
    }

    # Get pygal country code map
    pygal_countries = pygal.maps.world.COUNTRIES

    # 1960
    render_world_map(gdpinfo, pygal_countries, "1960", "isp_gdp_world_name_1960.svg")

    # 1980
    render_world_map(gdpinfo, pygal_countries, "1980", "isp_gdp_world_name_1980.svg")

    # 2000
    render_world_map(gdpinfo, pygal_countries, "2000", "isp_gdp_world_name_2000.svg")

    # 2010
    render_world_map(gdpinfo, pygal_countries, "2010", "isp_gdp_world_name_2010.svg")


# Make sure the following call to test_render_world_map is commented
# out when submitting to OwlTest/CourseraTest.

# test_render_world_map()
