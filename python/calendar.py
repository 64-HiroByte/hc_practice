import datetime
import sys


def validate_command_line_args(month_names):
    """
    Validate the command-line arguments entered with the script file.

    Args:
        month_names (tuple): A tuple containing the names of the months in lowercase.
        
    Validates:
        - The presence of the '-m' option.
        - The validity of the month number or name.
        - The validity of the year if provided.
    """
    
    def validate_value(i, min_val, max_val, txt):
        """
        Validate the value of a command-line argument.

        Args:
            i (int): The index number of the command-line argument in sys.argv.
            min_val (int): The minimum allowed value for sys.argv[index].
            max_val (int): The max allowed value for sys.argv[index].
            txt (str): The error message to display if validation fails.
        """
        if not min_val <= int(sys.argv[i]) <= max_val:
            sys.exit(txt)
    
    if len(sys.argv) == 1:
        return
    
    if sys.argv[1] != '-m':
        sys.exit(f'"{sys.argv[1]}" is unknown option\nThe only option available is "-m"')
    
    if len(sys.argv) > 2:
        error_message = f'{sys.argv[2]} is neither a month number (1..12) nor a name'
        try:
            int(sys.argv[2])
        except ValueError:
            if sys.argv[2].lower() not in month_names:
                sys.exit(error_message)
        else:
            validate_value(i=2, min_val=1, max_val=12, txt=error_message)
    
    if len(sys.argv) > 3:
        error_message = f'{sys.argv[3]} is not a number or not in range 1..9999'
        try:
            int(sys.argv[3])
        except ValueError:
            sys.exit(error_message)
        else:
            validate_value(i=3, min_val=1, max_val=9999, txt=error_message)


def get_specified_month_and_year(month_names):
    """
    Determine the month and year specified from the command-line arguments.

    Args:
        month_names (tuple): This tuple contains the name of the montshs in lowercase.

    Returns:
        tuple: This tuple contains:
            - is_month_name(bool): True if the month was specified by name, False if specified by number.
            - specified_month(int): The specified month as a number(1..12).
            - specified_year(int): The specified year.
    """
    today = datetime.date.today()
    
    is_month_name = False
    specified_month = today.month
    specified_year = today.year

    if len(sys.argv) > 2:
        if sys.argv[2].isdecimal():
            specified_month = int(sys.argv[2])
        else:
            specified_month = month_names.index(sys.argv[2].lower()) + 1
            is_month_name = True

    if len(sys.argv) > 3:
        specified_year = int(sys.argv[3])
    
    return is_month_name, specified_month, specified_year


def get_first_day_of_week(mo, yr):
    """
    Get the first day of the week for the given month and year.

    Args:
        mo (int): The specified month.
        yr (int): The specified year.

    Returns:
        int: The weekday index of the first day of the month(0=Monday, 6=Sunday).
    """
    first_day = datetime.date(yr, mo, 1)
    first_day_of_week = datetime.date.weekday(first_day)
    return first_day_of_week


def get_last_day_of_month(mo, yr):
    """
    Get the last day of the month for the given month and year.

    Args:
        mo (int): The specified month.
        yr (int): The specified year.

    Returns:
        int: The last day of the month.
    """
    if mo == 12:
        yr += 1
        mo = 1
    else:
        mo += 1
        
    last_day = datetime.date(year=yr, month=mo, day=1) - datetime.timedelta(days=1)
    return last_day.day


def create_calendar_header(is_month_name, day_names, specified_month, specified_year):
    """
    Create the calendar header including the month-year and day names.

    Args:
        is_month_name (bool): True if the month was specified by name, False if specified by number.
        day_names (tuple): This tuple containing day names in two formats(EN/JP).
        specified_month(int): The specified month.
        specified_year(int): The specified year.
        
    Returns:
        list: A list of string representing the calendar header.
    """    
    calendar_header = []
    if is_month_name:
        calendar_header = [
            [f'{sys.argv[2].capitalize()} {specified_year}'.center(20)],
            day_names[1]
        ]
    else:
        calendar_header = [
            [f'{specified_month}月 {specified_year}'.center(20)],
            day_names[0]
        ]
    return calendar_header


def create_month_calendar(specified_month, specified_year):
    """
    Create the calendar for the specified month and year.

    Args:
        specified_month (int): The specified month
        specified_year (int): The specified year

    Returns:
        list: A list of weekly dates for the given month and year.
    """    
    first_day_index = get_first_day_of_week(mo=specified_month, yr=specified_year)
    last_day_of_month = get_last_day_of_month(mo=specified_month, yr=specified_year)
    
    day_of_month = 1
    month_calendar = []
    while day_of_month <= last_day_of_month:
        weekly_list = []
        for i in range(7):
            if day_of_month == 1 and i < first_day_index:
                str_value = ''
            else:
                str_value = str(day_of_month)
                day_of_month += 1
            str_value = f'{str_value:>2}'
            weekly_list.append(str_value)
            
            if day_of_month > last_day_of_month:
                break
        month_calendar.append(weekly_list)
        
    return month_calendar


def show_calendar(calendar_header, month_calendar):
    """
    Print the calendar to the console.

    Args:
        calendar_header (list): the calendar header including the month-year and day names.
        month_calendar (list): A list of weekly dates for the given month and year.
    """    
    calender_data = calendar_header + month_calendar
    for r in calender_data:
        print(' '.join(r))


if __name__ == '__main__':
    MONTH_NAMES = (
        'january', 'february', 'march', 'april', 'may', 'june',
        'july', 'august', "september", 'october', 'november', 'december'
    )
    
    DAY_NAMES = (
        ('月', '火', '水', '木', '金', '土', '日'),
        ('Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su')
    )

    validate_command_line_args(MONTH_NAMES)
    is_month_name, specified_month, specified_year = get_specified_month_and_year(MONTH_NAMES)
    calendar_header = create_calendar_header(is_month_name, DAY_NAMES, specified_month, specified_year)

    month_calendar = create_month_calendar(specified_month, specified_year)

    show_calendar(calendar_header, month_calendar)
