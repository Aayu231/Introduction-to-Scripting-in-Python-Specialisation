IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """

    if(line1 == line2):
        return IDENTICAL
    else:
        if(len(line1) > len(line2)):
            line1, line2 = line2, line1
        i_1 = 0
    if(line1 == ''):
        return i_1
    while(line1[i_1] == line2[i_1]):
        if(i_1 < len(line1) - 1):
            i_1 += 1
        else:
            return i_1 + 1
    return i_1

def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    if(idx < 0 or idx > min(len(line1), len(line2))):
        return ""
    else:
        return(line1 + "\n" + "=" * idx + "^" + "\n" + line2 + "\n")
        
def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    if(lines1 == lines2):
        return (IDENTICAL, IDENTICAL)
    else:
        i_6 = 0
        if(len(lines1) > len(lines2)):
            lines2, lines1 = lines1, lines2
        i_5 = len(lines1)
        while(i_6 <= i_5):
            if(i_6 == i_5):
                return(i_6, 0)
            ln_1 = lines1[i_6]
            ln_2 = lines2[i_6]
            if(ln_1 != ln_2):
                i_7 = singleline_diff(ln_1, ln_2)
                return(i_6, i_7)
            i_6 += 1           
        
def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    f_1 = open(filename, 'rt')
    l_1 = []
    while True:
        line = f_1.readline()
        if (line == ""):
            return l_1
        line = line[0:len(line) - 1]
        l_1.append(line)


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    f_1 = get_file_lines(filename1)
    f_2 = get_file_lines(filename2)
    
    if(f_1 == f_2):
        return "No differences\n"
    li_ne, pos_ition = multiline_diff(f_1, f_2)

    return("Line "+ str(li_ne) + ":" + '\n'
           + singleline_diff_format(f_1[li_ne], f_2[li_ne], pos_ition))
