def extract_record(line):
    months = {
    '01': 'January',
    '02' :'February',
    '03' :'March',
    '04': 'April',
    '05' :'May',
    '06': 'June',
    '07' :'July',
    '08': 'August',
    '09': 'September',
    '10': 'October',
    '11': 'November',
    '12': 'December'
    }

    day={
        '1': 'Sunday',
        '2': 'Monday',
        '3': 'Tuesday',
        '4': 'Wednesday',
        '5': 'Thursday',
        '6': 'Friday',
        '7': 'Saturday'
    }

    birth_place = {
        '1': 'Hospital',
        '2': 'Freestanding Birth Center',
        '3': 'Home (intended)',
        '4': 'Home (not intended)',
        '5': 'Home (unknown if intended)',
        '6': 'Clinic / Doctor’s Office',
        '7': 'Other',
        '9': 'Unknown '
    }

    report_flag = {
        '0':'Non-Reporting',
        '1':'Reporting'
    }

    facility_recode = {
        '1': 'In Hospital',
        '2': 'Not in Hospital',
        '3': 'Unknown or Not Stated'
    }

    age_imputed = {
        ' ': False,
        '1': True
    }
    age_reported = {
        ' ': False,
        '1': True
    }
    mother_single_years_age = {
        '  ' : ' ',
        '12': '10 - 12 years',
        '13': '13 years',
        '14': '14 years',
        '15': '15 years',
        '16': '16 years',
        '17': '17 years',
        '18': '18 years',
        '19': '19 years',
        '20': '20 years',
        '21': '21 years',
        '22': '22 years',
        '23': '23 years',
        '24': '24 years',
        '25': '25 years',
        '26': '26 years',
        '27': '27 years',
        '28': '28 years',
        '29': '29 years',
        '30': '30 years',
        '31': '31 years',
        '32': '32 years',
        '33': '33 years',
        '34': '34 years',
        '35': '35 years',
        '36': '36 years',
        '37': '37 years',
        '38': '38 years',
        '39': '39 years',
        '40': '40 years',
        '41': '41 years',
        '42': '42 years',
        '43': '43 years',
        '44': '44 years',
        '45': '45 years',
        '46': '46 years',
        '47': '47 years',
        '48': '48 years',
        '49': '49 years',
        '50': '50 years and over' 

    }
    mot_age_r_14 = {
        '  ' : ' ',
        '01' : 'Under 15 Years',
        '03' : '15 years',
        '04' : '16 years',
        '05' : '17 years',
        '06' : '18 years',
        '07' : '19 years',
        '08' : '20-24 years',
        '09' : '25-29 years',
        '10' : '30-34 years',
        '11' : '35-39 years',
        '12' : '40-44 years',
        '13' : '45-49 years',
        '14' : '50-54 years' 
    }
    mot_age_r_9 = {
        ' ' : ' ',
        '1': 'Under 15 years',
        '2': '15-19 years',
        '3': '20-24 years',
        '4': '25-29 years',
        '5': '30-34 years',
        '6': '35-39 years',
        '7': '40-44 years',
        '9': '45-49 years',
        '8': '50-54 years'
    }
    mother_nativity = {
        ' ' : ' ',
        '1' : 'Born in the U.S. (50 US States)',
        '2' : 'Born outside the U.S. (includes possessions)',
        '3' : 'Unknown or Not Stated', 
    }
    resident_Status = {
        ' ' : ' ',
        '1': 'RESIDENT: State and county of occurrence and residence are the same.',
        '2': 'INTRASTATE NONRESIDENT: State of occurrence and residence are the same but county is different.',
        '3': 'INTERSTATE NONRESIDENT: State of occurrence and residence are different but both are one of the 50 US states or District of Columbia',
        '4': 'FOREIGN RESIDENT: The state of residence is not one of the 50 US states or District of Columbia.',
    }
    mother_race_recode_31 = {
        '  ': '',
        '01': 'White (only) [only one race reported]',
        '02': 'Black (only)',
        '03': 'AIAN (American Indian or Alaskan Native) (only)',
        '04': 'Asian (only)',
        '05': 'NHOPI (Native Hawaiian or Other Pacific Islander) (only)',
        '06': 'Black and White',
        '07': 'Black and AIAN',
        '08': 'Black and Asian',
        '09': 'Black and NHOPI',
        '10': 'AIAN and White',
        '11': 'AIAN and Asian',
        '12': 'AIAN and NHOPI',
        '13': 'Asian and White',
        '14': 'Asian and NHOPI',
        '15': 'NHOPI and White',
        '16': 'Black, AIAN, and White',
        '17': 'Black, AIAN, and Asian',
        '18': 'Black, AIAN, and NHOPI',
        '19': 'Black, Asian, and White',
        '20': 'Black, Asian, and NHOPI',
        '21': 'Black, NHOPI, and White',
        '22': 'AIAN, Asian, and White',
        '23': 'AIAN, NHOPI, and White',
        '24': 'AIAN, Asian, and NHOPI',
        '25': 'Asian, NHOPI, and White',
        '26': 'Black, AIAN, Asian, and White',
        '27': 'Black, AIAN, Asian, and NHOPI',
        '28': 'Black, AIAN, NHOPI, and White',
        '29': 'Black, Asian, NHOPI, and White',
        '30': 'AIAN, Asian, NHOPI, and White',
        '31': 'Black, AIAN, Asian, NHOPI, and White'
    }

    mother_race_recode_6 = {
        '': '',
        '1': 'White (only)',
        '2': 'Black (only)',
        '3': 'AIAN (only)',
        '4': 'Asian (only)',
        '5': 'NHOPI (only)',
        '6': 'More than one race'
    }
    mother_race_recode_15 = {
        '  ': '',
        '01': 'White (only)',
        '02': 'Black (only)',
        '03': 'AIAN (only)',
        '04': 'Asian Indian (only)',
        '05': 'Chinese (only)',
        '06': 'Filipino (only)',
        '07': 'Japanese (only)',
        '08': 'Korean (only)',
        '09': 'Vietnamese (only)',
        '10': 'Other Asian (only)',
        '11': 'Hawaiian (only)',
        '12': 'Guamanian (only)',
        '13': 'Samoan (only)',
        '14': 'Other Pacific Islander (only)',
        '15': 'More than one race'
    }
    mothers_race_imputed = {
        ' ' : 'Mothers Race Imputed Flag',
        '1' : 'Unknown race imputed',
        '2' : 'All other races, formerly coded 09, imputed.'
    }
    mother_hispanic_origin = {
        ' ' : '',
        '0' : 'Non-Hispanic',
        '1' : 'Mexican',
        '2' : 'Puerto Rican',
        '3' : 'Cuban',
        '4' : 'Central or South American',
        '5' : 'Dominican',
        '6' : 'Other and Unknown Hispanic',
        '9' : 'Origin unknown or not stated '
    }
    mother_hispanic_origin_recode = {
        ' ' : '',
        '0' : 'Non-Hispanic',
        '1' : 'Mexican',
        '2' : 'Puerto Rican',
        '3' : 'Cuban',
        '4' : 'Central or South American',
        '5' : 'Other and Unknown Hispanic',
        '9' : 'Origin unknown or not stated '
    }
    mother_origin_flag = {
        ' ' : '',
        '0' : 'Non-Reporting',
        '1' : 'Reporting'
    }
    mother_race_hisponic = {
        ' ' : '',
        '1' : 'Non-Hispanic White (only)',
        '2' : 'Non-Hispanic Black (only)',
        '3' : 'Non-Hispanic AIAN (only)',
        '4' : 'Non-Hispanic Asian (only)',
        '5' : 'Non-Hispanic NHOPI (only)',
        '6' : 'Non-Hispanic more than one race',
        '7' : 'Hispanic',
        '8' : 'Origin unknown or not stated'
    }
    paternity_acknowledge = {
        ' ' : '',
        'Y' : 'Yes',
        'N' : 'No',
        'U' : 'Unknown',
        'X' : 'Not Applicable'
    }
    record = {}
    record['Birth Year'] = int(line[8:12])
    record['Birth Month'] = months[line[12:14]]
    time_data = line[18:22]
    record['Time of Birth'] = 'Not Stated' if time_data == '9999' else time_data
    record['Birth Day of Week'] = day[line[22]]
    record['Birth Place'] = day[birth_place[31]]
    record['Reporting Flag for Birth Place'] = day[report_flag[32]]
    record['Facility Recode'] = day[facility_recode[49]]
    record["Mother's Age Imputed"] = day[age_imputed[72]]
    record["Reported Age of Mother Used Flag"] = day[age_reported[73]]
    record["Mother's Single Years of Age"] = day[mother_single_years_age[74:76]]
    record["Mother's Age Recode 14"] = day[mot_age_r_14[76:78]]
    record["Mother's Age Recode 9"] = day[mot_age_r_9[78]]
    record["Mother's Nativity"] = day[mother_nativity[83]]
    record["Residence Status"] = day[resident_Status[103]]
    record["Mother's Race Recode 31"] = day[mother_race_recode_31[104:106]]
    record["Mother's Race Recode 6"] = day[mother_race_recode_6[106]]
    record["Mother's Race Recode 15"] = day[mother_race_recode_15[107:109]]
    record["Mother's Race Imputed Flag"] = day[mothers_race_imputed[110]]
    record["Mother's Hispanic Origin "] = day[mother_hispanic_origin[111]]
    record["Mother's Hispanic Origin Recode"] = day[mother_hispanic_origin_recode[114]]
    record["Reporting Flag for Mother's Origin"] = day[mother_origin_flag[115]]
    record["Mother's Race/Hispanic Origin"] = day[mother_race_hisponic[116]]
    record["Paternity Acknowledged"] = day[paternity_acknowledge[118]]
    record["Paternity Acknowledged"] = day[paternity_acknowledge[118]]


data_file = open('Nat2021US.txt')
line = data_file.readline()

record = extract_record(line)


data_file.close()