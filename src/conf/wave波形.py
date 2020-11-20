id_col_num = 1
header = ['波形', '编码', '文本', '编码系统', '测量单位', '测量部位']

data = {'151700^MDC_CONC_AWAY_CO2^MDC': ['ANES_CO2', '151700', 'MDC_CONC_AWAY_CO2', 'MDC', 'mmHg', ''],
        '151908^MDC_CONC_AWAY_O2^MDC': ['ANES_O2', '151908', 'MDC_CONC_AWAY_O2', 'MDC', '%', ''],
        '152048^MDC_CONC_AWAY_N2O^MDC': ['ANES_N2O', '152048', 'MDC_CONC_AWAY_N2O', 'MDC', '%', ''],
        '152456^MDC_CONC_AWAY_AGENT^MDC': ['Agent, Airway', '152456', 'MDC_CONC_AWAY_AGENT', 'MDC', 'mmHg, kPa, %', ''],
        '152024^MDC_CONC_AWAY_DESFL^MDC': ['ANES_DES', '152024', 'MDC_CONC_AWAY_DESFL', 'MDC', '%', ''],
        '152028^MDC_CONC_AWAY_ENFL^MDC': ['ANES_ENF', '152028', 'MDC_CONC_AWAY_ENFL', 'MDC', '%', ''],
        '152032^MDC_CONC_AWAY_HALOTH^MDC': ['ANES_HAL', '152032', 'MDC_CONC_AWAY_HALOTH', 'MDC', '%', ''],
        '152036^MDC_CONC_AWAY_SEVOFL^MDC': ['ANES_SEV', '152036', 'MDC_CONC_AWAY_SEVOFL', 'MDC', '%', ''],
        '152040^MDC_CONC_AWAY_ISOFL^MDC': ['ANES_ISO', '152040', 'MDC_CONC_AWAY_ISOFL', 'MDC', '%', ''],
        '151792^MDC_PRESS_AWAY^MDC': ['Pressure, Airway', '151792', 'MDC_PRESS_AWAY', 'MDC', 'mmHg, kPa, %', ''],
        '151764^MDC_FLOW_AWAY^MDC': ['Flow, Airway', '151764', 'MDC_FLOW_AWAY', 'MDC', 'mmHg, kPa, %', ''],
        '152708^MDC_VOL_AWAY^MDC': ['Volume, Airway', '152708', 'MDC_VOL_AWAY', 'MDC', 'mmHg, kPa, %', ''],
        '131329^MDC_ECG_ELEC_POTL_I^MDC': ['ECG Lead I', '131329', 'MDC_ECG_ELEC_POTL_I', 'MDC', 'mV', ''],
        '131330^MDC_ECG_ELEC_POTL_II^MDC': ['ECG Lead II', '131330', 'MDC_ECG_ELEC_POTL_II', 'MDC', 'mV', ''],
        '131389^MDC_ECG_ELEC_POTL_III^MDC': ['ECG Lead III', '131389', 'MDC_ECG_ELEC_POTL_III', 'MDC', 'mV', ''],
        '131391^MDC_ECG_ELEC_POTL_AVL^MDC': ['ECG Lead aVL', '131391', 'MDC_ECG_ELEC_POTL_AVL', 'MDC', 'mV', ''],
        '131390^MDC_ECG_ELEC_POTL_AVR^MDC': ['ECG Lead aVR', '131390', 'MDC_ECG_ELEC_POTL_AVR', 'MDC', 'mV', ''],
        '131392^MDC_ECG_ELEC_POTL_AVF^MDC': ['ECG Lead aVF', '131392', 'MDC_ECG_ELEC_POTL_AVF', 'MDC', 'mV', ''],
        '131395^MDC_ECG_ELEC_POTL_V^MDC': ['ECG Lead V', '131395', 'MDC_ECG_ELEC_POTL_V', 'MDC', 'mV', ''],
        '131331^MDC_ECG_ELEC_POTL_V1^MDC': ['ECG Lead V1', '131331', 'MDC_ECG_ELEC_POTL_V1', 'MDC', 'mV', ''],
        '131332^MDC_ECG_ELEC_POTL_V2^MDC': ['ECG Lead V2', '131332', 'MDC_ECG_ELEC_POTL_V2', 'MDC', 'mV', ''],
        '131333^MDC_ECG_ELEC_POTL_V3^MDC': ['ECG Lead V3', '131333', 'MDC_ECG_ELEC_POTL_V3', 'MDC', 'mV', ''],
        '131334^MDC_ECG_ELEC_POTL_V4^MDC': ['ECG Lead V4', '131334', 'MDC_ECG_ELEC_POTL_V4', 'MDC', 'mV', ''],
        '131335^MDC_ECG_ELEC_POTL_V5^MDC': ['ECG Lead V5', '131335', 'MDC_ECG_ELEC_POTL_V5', 'MDC', 'mV', ''],
        '131336^MDC_ECG_ELEC_POTL_V6^MDC': ['ECG Lead V6', '131336', 'MDC_ECG_ELEC_POTL_V6', 'MDC', 'mV', ''],
        '151780^MDC_IMPED_TTHOR^MDC': ['Transthoracic Impedance', '151780', 'MDC_IMPED_TTHOR', 'MDC', 'mΩ', ''],
        '150016^MDC_PRESS_BLD^MDC': ['Invasive Blood Pressure', '150016', 'MDC_PRESS_BLD', 'MDC', 'mmHg', ''],
        '150032^MDC_PRESS_BLD_ART^MDC': ['Arterial Blood Pressure', '150032', 'MDC_PRESS_BLD_ART', 'MDC', 'mmHg', ''],
        '150056^MDC_PRESS_BLD_ART_UMB^MDC': ['Umbilical Arterial Blood Pressure', '150056', 'MDC_PRESS_BLD_ART_UMB',
                                             'MDC', 'mmHg', ''],
        '150100^MDC_PRESS_BLD_VENT_LEFT^MDC': ['Left Ventricle Blood Pressure', '150100', 'MDC_PRESS_BLD_VENT_LEFT',
                                               'MDC', 'mmHg', ''],
        '150044^MDC_PRESS_BLD_ART_PULM^MDC': ['Pulmonary Arterial Blood Pressure', '150044', 'MDC_PRESS_BLD_ART_PULM',
                                              'MDC', 'mmHg', ''],
        '150084^MDC_PRESS_BLD_VEN_CENT^MDC': ['Central Venous Blood Pressure', '150084', 'MDC_PRESS_BLD_VEN_CENT',
                                              'MDC', 'mmHg', ''],
        '153608^MDC_PRESS_INTRA_CRAN^MDC': ['Intra Cranial Pressure', '153608', 'MDC_PRESS_INTRA_CRAN', 'MDC', 'mmHg',
                                            ''],
        '150064^MDC_PRESS_BLD_ATR_LEFT^MDC': ['Left Atria Blood Pressure', '150064', 'MDC_PRESS_BLD_ATR_LEFT', 'MDC',
                                              'mmHg', ''],
        '150068^MDC_PRESS_BLD_ATR_RIGHT^MDC': ['Right Atria Blood Pressure', '150068', 'MDC_PRESS_BLD_ATR_RIGHT', 'MDC',
                                               'mmHg', ''],
        '150028^MDC_PRESS_BLD_AORT^MDC': ['Aortic Blood Pressure', '150028', 'MDC_PRESS_BLD_AORT', 'MDC', 'mmHg', ''],
        '150680^MDC_PRESS_BLD_ART_BRACHIAL^MDC': ['Brachial Arterial Blood Pressure', '150680',
                                                  'MDC_PRESS_BLD_ART_BRACHIAL', 'MDC', 'mmHg', ''],
        '150648^MDC_PRESS_BLD_ART_FEMORAL^MDC': ['Femoral Arterial Blood Pressure', '150648',
                                                 'MDC_PRESS_BLD_ART_FEMORAL', 'MDC', 'mmHg', ''],
        '150088^MDC_PRESS_BLD_VEN_UMB^MDC': ['Umbilical Venous Blood Pressure', '150088', 'MDC_PRESS_BLD_VEN_UMB',
                                             'MDC', 'mmHg', ''],
        '153900^MDC_EEG_ELEC_POTL_CRTX^MDC': ['EEG', '153900', 'MDC_EEG_ELEC_POTL_CRTX', 'MDC', 'mV', '†'],
        '150452^MDC_PULS_OXIM_PLETH^MDC': ['Monitor_Pleth', '150452', 'MDC_PULS_OXIM_PLETH', 'MDC', '', ''],
        '160324^MDC_SPO2_SIGNAL_QUALITY_INDEX^MDC': ['SpO2 Signal Quality Index', '160324',
                                                     'MDC_SPO2_SIGNAL_QUALITY_INDEX', 'MDC', '', ''],
        '288^MNDRY_EEG_ELEC_POTL_BIS_EYE^99MNDRY': ['EGW_MDtag_Wavefor mData_BIS_EEG_E', '288',
                                                    'MNDRY_EEG_ELEC_POTL_BIS_EYE', '99MNDRY', 'mV', ''],
        '613^MNDRY_GSR^99MNDRY': ['MONITOR_GSR', '613', 'MNDRY_GSR', '99MNDRY', '', ''],
        '284^MNDRY_PRESS_INTRA_ABDOM^MNDRY99': ['Intra-abdominal Pressure', '284', 'MNDRY_PRESS_INTRA_ABDOM', 'MNDRY99',
                                                'mmHg', ''],
        '290^MNDRY_ICG_IMP^MNDRY99': ['Impedance Cardiography Impedance', '290', 'MNDRY_ICG_IMP', 'MNDRY99', 'mΩ', ''],
        '286^MNDRY_EEG_ELEC_POTL_BIS^MNDRY99': ['BIS EEG', '286', 'MNDRY_EEG_ELEC_POTL_BIS', 'MNDRY99', 'mV', ''],
        '287^MNDRY_EEG_ELEC_POTL_BIS_TEMPR^MNDRY99': ['BIS EEG, Right Temporal', '287', 'MNDRY_EEG_ELEC_POTL_BIS_TEMPR',
                                                      'MNDRY99', 'mV', 'Fore Head, Right'],
        '288^MNDRY_EEG_ELEC_POTL_BIS_EYE^MNDRY99': ['BIS EEG, Right Eye', '288', 'MNDRY_EEG_ELEC_POTL_BIS_EYE',
                                                    'MNDRY99', 'mV', 'Fore Head, Right']}
