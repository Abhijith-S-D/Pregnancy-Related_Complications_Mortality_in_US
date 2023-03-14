## CDC WONDER API - Natality, 2016-2021
CDC WONDER is a query tool from the Centers for Disease Control (CDC) that provides access to a collection of online databases for the analysis of public health data.

The following are a sampling of databases available through WONDER that provide vital statistics data through CDC's National Center for Health Statistics

Births
Compressed Mortality
Infant Deaths
Detailed Mortality
Multiple cause of death

For this project, we will focus on the Natality 2016-2021 database, which provides number of births and birth rates for underlying factors at the national, state and county level. Using the query tool, the user can select grouping and filtering variables that are used to generate a dataset. Results from the endpoint include a data table along with applicable footnotes and caveats, which can then be exported to a tab delimited file or visualized.

WONDER provides an API that allows the same queries to be issued through a HTTP POST request to WONDER's web server (no authentication required). Requests and responses are issued in XML format and are detailed in the API Documentation page. The documentation specifies that when running an automated query, the a limit of one query for every 2 minutes should be made to allow for good system recovery time.

Each XML request consists of a series of parameter tags with name and value.

The following broad categories are available in the dataset:

Abnormal conditions of newborn

Congenital anomalies of newborn

Delivery characteristics

Infant characteristics

Labor characteristics

Maternal Residence

Maternal characteristics

Maternal infections present and/or treated during pregnancy

Maternal morbidity

Maternal risk factors

Paternal characteristics

Pregnancy history and prenatal care characteristics

Pregnancy risk factors

The following is a listing of available values for each parameter name in the format:

<value> : <description>

Abnormal conditions of newborn

'D149.V116': 'Assisted Ventilation'

'D149.V117': 'Assisted Ventilation > 6 hrs'

'D149.V118': 'NICU Admission'

'D149.V119': 'Surfactant Replacement Therapy'

'D149.V120': 'Antibiotics for Suspected Neonatal Sepsis'

'D149.V121': 'Seizures'

'D149.V122': 'Abnormal Conditions Checked'

Congenital anomalies of newborn

'D149.V123': 'Anencephaly'

'D149.V124': 'Meningomyelocele / Spina Bifida'

'D149.V125': 'Cyanotic Congenital Heart Disease'

'D149.V126': 'Congenital Diaphragmatic Hernia'

'D149.V127': 'Omphalocele'

'D149.V128': 'Gastroschisis'

'D149.V129': 'Limb Reduction Defect'

'D149.V130': 'Cleft Lip with or without Cleft Palate'

'D149.V131': 'Cleft Palate Alone'

'D149.V132': 'Down Syndrome'

'D149.V133': 'Suspected Chromosomal Disorder'

'D149.V134': 'Hypospadias'

'D149.V135': 'Congenital Anomalies Checked'

Delivery characteristics

'D149.V20': 'Year'

'D149.V25': 'Month'

'D149.V26': 'Weekday'

'D149.V44': 'Time of Day'

'D149.V45': 'Birthplace'

'D149.V30': 'Birthplace Recode 6'

'D149.V46': 'Birthplace Recode 3'

'D149.V29': 'Medical Attendant'

'D149.V108': 'Mother Transferred'

'D149.V98': 'Fetal Presentation'

'D149.V99': 'Final Route and Delivery Method'

'D149.V101': 'Delivery Method Expanded'

'D149.V31': 'Delivery Method'

'D149.V100': 'Trial of Labor Attempted (if cesarean)'

'D149.V110': 'Source of Payment for Delivery'

'D149.V109': 'Source of Payment for Delivery Expanded'

Infant characteristics

'D149.V32': 'OE Gestational Age Recode 10'

'D149.V33': 'OE Gestational Age Recode 11'

'D149.V34': 'OE Gestational Age Weekly'

'D149.V6': 'LMP Gestational Recode 10'

'D149.V23': 'LMP Gestational Recode 11'

'D149.V24': 'LMP Gestational Age Weekly'

'D149.V3': 'Sex of Infant'

'D149.V7': 'Plurality'

'D149.V115': 'Set Order'

'D149.V9': 'Infant Birth Weight 12'

'D149.V35': 'Infant Birth Weight 14'

'D149.V41': 'Infant Birth Weight 100 gram increments'

'D149.V111': 'Five Minute APGAR Score'

'D149.V112': 'Five Minute APGAR Score Recode'

'D149.V113': 'Ten Minute APGAR Score'

'D149.V114': 'Ten Minute APGAR Score Recode'

'D149.V136': 'Infant Transferred'

'D149.V137': 'Infant Living at Time of Report'

'D149.V138': 'Infant Breastfed at Discharge'

Maternal Residence

'D149.V154': '2013 Metro/Nonmetro'

'D149.V155': '2006 Metro/Nonmetro'

'D149.V156': '2006 Urbanization'

Maternal characteristics

'D149.V42': "Mother's Single Race 6"

'D149.V49': "Mother's Single Race 15"

'D149.V50': "Mother's Single/Multi Race 31"

'D149.V43': "Mother's Hispanic Origin"

'D149.V4': "Mother's Expanded Hispanic Origin"

'D149.V1': 'Age of Mother 9'

'D149.V38': 'Age of Mother 13'

'D149.V5': "Mother's Education"

'D149.V27': 'Marital Status'

'D149.V51': 'Paternity Acknowledgment (if mother unmarried)'

'D149.V48': "Mother's Nativity"

'D149.V147': "Mother's Birth Country"

'D149.V47': "Mother's Birth State"

Maternal infections present and/or treated during pregnancy

'D149.V83': 'Gonorrhea'

'D149.V84': 'Syphilis'

'D149.V85': 'Chlamydia'

'D149.V86': 'Hepatitis B'

'D149.V87': 'Hepatitis C'

'D149.V88': 'Infections Checked'

Maternal morbidity

'D149.V102': 'Maternal Transfusion'

'D149.V103': 'Perineal Laceration'

'D149.V104': 'Ruptured Uterus'

'D149.V105': 'Unplanned Hysterectomy'

'D149.V106': 'Admission to Intensive Care Unit'

'D149.V107': 'Maternal Morbidity Checked'

Maternal risk factors

'D149.V70': "Mother's Height in Inches"

'D149.V71': "Mother's Pre-pregnancy BMI"

'D149.V73': "Mother's Weight Gain Recode"

'D149.V149': "Mother's Pre-pregnancy Weight"

'D149.V150': "Mother's Delivery Weight"

'D149.V10': 'Tobacco Use'

'D149.V143': 'Number of Cigarettes Before Pregnancy Recode'

'D149.V144': 'Number of Cigarettes 1st Trimester Recode'

'D149.V140': 'Number of Cigarettes 1st Trimester'

'D149.V145': 'Number of Cigarettes 2nd Trimester Recode'

'D149.V141': 'Number of Cigarettes 2nd Trimester'

'D149.V146': 'Number of Cigarettes 3rd Trimester Recode'

'D149.V142': 'Number of Cigarettes 3rd Trimester'

Paternal characteristics

'D149.V54': "Father's Single Race 6"

'D149.V55': "Father's Single Race 15"

'D149.V56': "Father's Single/Multi Race 31"

'D149.V53': "Father's Hispanic Origin"

'D149.V52': "Father's Expanded Hispanic Origin"

'D149.V57': 'Age of Father'

'D149.V58': "Father's Education"

Pregnancy history and prenatal care characteristics

'D149.V60': 'Interval Since Last Live Birth'

'D149.V61': 'Interval Since Last Other Pregnancy Outcome'

'D149.V62': 'Interval of Last Pregnancy'

'D149.V151': 'Prior Births Now Living'

'D149.V152': 'Prior Births Now Dead'

'D149.V153': 'Prior Other Pregnancy Outcomes'

'D149.V28': 'Live Birth Order'

'D149.V59': 'Total Birth Order'

'D149.V66': 'WIC'

'D149.V89': 'Successful External Cephalic Version'

'D149.V90': 'Failed External Cephalic Version'

'D149.V65': 'Number of Prenatal Visits Recode'

'D149.V64': 'SNumber of Prenatal Visits'

'D149.V63': 'Trimester Prenatal Care Began'
'D149.V8': 'Month Prenatal Care Began'

Pregnancy risk factors
'D149.V74': 'Pre-pregnancy Diabetes'

'D149.V75': 'Gestational Diabetes'

'D149.V16': 'Pre-pregnancy Hypertension'

'D149.V17': 'Gestational Hypertension'

'D149.V18': 'Eclampsia'

'D149.V76': 'Previous Preterm Birth'
'D149.V77': 'Infertility Treatment Used'

'D149.V78': 'Fertility Enhancing Drugs'

'D149.V79': 'Assistive Reproductive Technology'

'D149.V80': 'Previous Cesarean Delivery'

'D149.V81': 'Number of Previous Cesareans'

'D149.V82': 'Risk Factors Checked'
 

M - Measure Parameters

<name> :{ <value> - <description>}

'M_002': {'D149.M002': 'Births'}

'M_007': {'D149.M007': 'Percent of Total Births'}

'M_070': {'D149.M070': 'Average Age of Mother (years)'}

'M_071': {'D149.M071': 'Average Age of Mother (years) Standard Deviation'}

'M_080': {'D149.M080': 'Average OE Gestational Age (weeks)'}

'M_081': {'D149.M081': 'Average OE Gestational Age (weeks) Standard Deviation'}

'M_090': {'D149.M091': 'Average LMP Gestational Age (weeks)'}

'M_091': {'D149.M091': 'Average LMP Gestational Age (weeks) Standard Deviation'}

'M_095': {'D149.M095': 'Average Birth Weight (grams)'}

'M_096': {'D149.M096': 'Average Birth Weight (grams) Standard Deviation'}

'M_100': {'D149.M100': 'Average Pre-pregnancy BMI'}

'M_101': {'D149.M101': 'Average Pre-pregnancy BMI Standard Deviation'}

'M_110': {'D149.M110': 'Average Number of Prenatal Visits'}

'M_111': {'D149.M111': 'Average Number of Prenatal Visits Standard Deviation'}

'M_120': {'D149.M120': 'Average Interval Since Last Live Birth (months)'}

'M_121': {'D149.M121': 'Average Interval Since Last Live Birth (months) Standard Deviation'}

'M_130': {'D149.M130': 'Average Interval Since Last Other Pregnancy Outcome (months)'}

'M_131': {'D149.M130': 'Average Interval Since Last Other Pregnancy Outcome (months) Standard Deviation'}




# An example implementation:
group_by_list = [

    'D149.V20', # Years

    'D149.V71', #Tobacco Use

]

measure_selection = {

    'M_002': 'D149.M002', # Births

    'M_007': 'D149.M007', # Percent of Total Births

    'M_070': 'D149.M070', # Average Age of Mother (years)

}

observation_selection = {}

variable_filter = {

    'V_D149.V71': ['1','2','3','4'] # filtering only stated deliveries

}

dataObj = wd.WonderD149Data(group_by_list,measure_selection,observation_selection,variable_filter)

dataObj.getData()
