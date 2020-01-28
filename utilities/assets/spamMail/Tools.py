import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass

working_dates = []
weekends = []
holidays = []
working_status = True


def get_working_dates():        #####################################
    return working_dates        #                                   #
                                #                                   #
                                #                                   #
def get_weekends():             #                                   #
    return weekends             #       Function getters for        #
                                #         global variables          #
                                #                                   #
def get_holidays():             #                                   #
    return holidays             #                                   #
                                #                                   #
                                #                                   #
def get_working_status():       #                                   #
    return working_status       #####################################


def set_dates(work_start, work_end):
    date_generated = [work_start + datetime.timedelta(days=x) for x in range(0, (work_end - work_start).days)]
    # Generate all dates between first day and last day at work.
    for date in date_generated:
        if date.weekday() in (5, 6):  # Append weekends to specified list.
            weekends.append(date)
        elif date.weekday() in holidays:  # Ignore holidays.
            continue
        else:  # Append working dates to specified list.
            working_dates.append(date)  # Weekends and holidays are not included.


def set_working_status(now):
    global working_status
    for day in holidays:  # No work during holidays.
        if now.date() == day:
            working_status = False
    for day in weekends:  # No work during weekends.
        if now.date() == day.date():
            working_status = False
    before_work = datetime.datetime(now.year, now.month, now.day, 9, 0, 0, 1)   # Same date as today, before work.
    after_work = datetime.datetime(now.year, now.month, now.day, 17, 0, 0, 1)   # Same date as today, after work.
    if now <= before_work or now >= after_work:
        working_status = False


def time_left(so_many_today):
    tfl = []
    days_left = so_many_today.days                   ##################################################################
    seconds_left = so_many_today.seconds             # Generate specified values, according to calculated difference. #
    micro_seconds_left = so_many_today.microseconds  ##################################################################

    years_left = days_left // 365                       #########################################################
    days_left -= years_left * 365                       #                                                       #
    months_left = days_left // 30                       #                                                       #
    days_left -= months_left * 30                       #                                                       #
    weeks_left = days_left // 7                         #                                                       #
    days_left -= weeks_left * 7                         #   Generate specified time periods with simple math    #
    hours_left = seconds_left // 60 // 60               #                                                       #
    seconds_left -= 60 * 60 * hours_left                #                                                       #
    minutes_left = seconds_left // 60                   #                                                       #
    seconds_left -= 60 * minutes_left                   #                                                       #
    mil_seconds_left = micro_seconds_left // 1000       #                                                       #
    micro_seconds_left -= 1000 * mil_seconds_left       #########################################################
    tfl.extend([years_left, months_left, weeks_left, days_left,
                hours_left, minutes_left, seconds_left, mil_seconds_left, micro_seconds_left])
    # Add above time values to tfl list.

    return tfl


def set_holidays():
    global holidays
    holidays = [datetime.date(2019, 12, 25),
                datetime.date(2019, 12, 26),
                datetime.date(2020, 1, 1),
                datetime.date(2020, 1, 6),
                datetime.date(2020, 3, 2),
                datetime.date(2020, 3, 25),
                datetime.date(2020, 4, 17),
                datetime.date(2020, 4, 20),
                datetime.date(2020, 5, 1),
                ]

def paid_days_off(now):
    off_days_paid = 0
    if now.month == 11:
        # off_days_paid = 2.48
        off_days_paid = 0
    elif now.month == 12:
        # off_days_paid = 2.48 + 5
        off_days_paid = 2.48
    elif now.month == 1:
        # off_days_paid = 2.48 + 5 + 4
        off_days_paid = 2.48 + 5
    elif now.month == 2:
        # off_days_paid = 2.48 + 5 + 4 + 5
        off_days_paid = 2.48 + 5 + 4
    elif now.month == 3:
        # off_days_paid = 2.48 + 5 + 4 + 5 + 5
        off_days_paid = 2.48 + 5 + 4 + 5
    elif now.month == 4:
        # off_days_paid = 2.48 + 5 + 4 + 5 + 5 + 5
        off_days_paid = 2.48 + 5 + 4 + 5 + 5
    elif now.month == 5:
        # off_days_paid = 2.48 + 5 + 4 + 5 + 5 + 5 + 2.48
        off_days_paid = 2.48 + 5 + 4 + 5 + 5 + 5
    return off_days_paid

def send_email(zois_email):
    msg = MIMEMultipart()  # Create message object instance.
    # recipients = ["theonzwg@gmail.com", "tzogx@hotmail.com", "Marianna.Leventi@ruhr-uni-bochum.de",
    #               "zwisss@hotmail.com"]
    msg['From'] = "zwisss@hotmail.com"  # Setup the parameters of the message.
    # msg['To'] = ", ".join(recipients)
    # msg['To'] = "zwisss@hotmail.com"
    msg['Subject'] = "Very important stuff"
    msg.attach(MIMEText(zois_email, 'plain'))  # Add in the message body.

    server = smtplib.SMTP("smtp.live.com", 587)
    server.ehlo()  # Hostname to send for this command defaults to the fully qualified domain name of the local host.
    server.starttls()  # Puts connection to SMTP server in TLS mode
    server.ehlo()
    server.login('zwisss@hotmail.com', getpass.getpass("Password: "))  # Hide password typing from screen.
    server.sendmail(msg['From'], "zwisss@hotmail.com", msg.as_string())  # Send the message via the server.
    print("\nMail to maself was successfully sent.")
    server.sendmail(msg['From'], "theonzwg@gmail.com", msg.as_string())
    print("Mail to Porportheon was successfully sent.")
    server.sendmail(msg['From'], "Marianna.Leventi@ruhr-uni-bochum.de", msg.as_string())
    print("Mail to Marianna, was successfully sent.")
    server.sendmail(msg['From'], "tzogx@hotmail.com", msg.as_string())
    print("Mail to Taso, was successfully sent.")
    msg['Subject'] = "Σχετικά με τον μηνιαίο μισθό."
    server.sendmail(msg['From'], "ilias.Anagnostopoulos@intrasoft-intl.com", msg.as_string())
    print("Mail to Ilia, was successfully sent.")

    server.quit()

