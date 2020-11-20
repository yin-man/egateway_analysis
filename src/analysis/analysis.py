#!/usr/bin/env python
#_*_coding:utf-8_*_


import os
import sys
import time
import argparse
import hl7parser

from os.path import dirname, abspath, sep

from src.conf.root import msh

PWD = dirname(abspath(__file__))
CONFPATH = dirname(PWD) + sep + "conf"
LOGDIR = dirname(dirname(PWD)) + sep + "log"
LIBPATH = dirname(dirname(PWD)) + sep + "lib"

# print(PWD)
# print(LIBPATH)
sys.path.append(LIBPATH)

import lib
from utils import Utils
from file_log_manager import FileLogManager
from src.conf import root,params_conf,unit

file_path = "egateway_analysis.src.analysis.hl7_handler.%s_analysis"


from openpyxl import Workbook
def write_excel(data):
    wb=Workbook()
    for key,val in data.items():
        ws=wb.create_sheet(key,0)
        if isinstance(val,dict):
            ws.append(list(val.keys()))
            ws.append(list(val.values()))
        if isinstance(val,list):
            for i in val:
                ws.append(list(i.keys()))
                ws.append(list(i.values()))
    wb.save('result.xlsx')


class Analysis:

    _handler_obj = {}

    def __init__(self, env, debug):
        self.env = env
        self.debug = debug
        self._init_logger()
        self._init_conf()
        self._init_hl7()

    def _init_logger(self):
        self.logger = FileLogManager("hl7_analysis_log", log_dir=LOGDIR)

    def _init_hl7(self):
        pass

    def _init_conf(self):
        pass

    def filter_msg(self, msg):
        if msg.strip().startswith("0x0B") and msg.strip().endswith("0x0D"):
            return False
        return True

    def process(self, msg):
        data="""MSH|^~\&|MINDRAY_N-SERIES^00A037009B000000^EUI-64||||20200825020835000-0800||ORU^R01^ORU_R01|1|P|2.6|||AL|NE||UNICODE UTF-8|||IHE_PCD_001^IHE PCD^1.3.6.1.4.1.19376.1.6.1.1.1^ISO
PID|||^^^Hospital^PI||John^Smith-Demo^^^^^L|||M||Unknown
PV1||I|ccu^^12^大连
OBR|1|1^MINDRAY_N-SERIES^00A037009B000000^EUI-64|1^MINDRAY_N-SERIES^00A037009B000000^EUI-64|182777000^monitoring of patient^SCT|||20200825020835-0800
OBX|1|NM|147842^MDC_ECG_HEART_RATE^MDC|1.7.4.147842|60|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800||||00A037009B000000^^00A037009B000000^EUI-64
OBX|2|NM|148066^MDC_ECG_V_P_C_RATE^MDC|1.7.2.148066|0|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|3|NM|108^MNDRY_ECG_PAUSE_RATE^99MNDRY|1.7.2.108|0|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|4|NM|352^MNDRY_ECG_VPB_RATE^99MNDRY|1.7.2.352|0|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|5|NM|298^MNDRY_ECG_COUPLETS_RATE^99MNDRY|1.7.2.298|0|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|6|NM|299^MNDRY_ECG_MISSED_BEATS_RATE^99MNDRY|1.7.2.299|0|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|7|NM|302^MNDRY_ECG_P_V_C_RonT_RATE^99MNDRY|1.7.2.302|0|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|8|NM|151578^MDC_TTHOR_RESP_RATE^MDC|1.7.1.151578|20|264928^MDC_DIM_RESP_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|9|NM|150456^MDC_PULS_OXIM_SAT_O2^MDC|1.3.1.150456|97|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|10|NM|149530^MDC_PULS_OXIM_PULS_RATE^MDC|1.3.1.149530|60|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|11|NM|150488^MDC_BLD_PERF_INDEX^MDC|1.3.1.150488|3.04|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|12|NM|150037^MDC_PRESS_BLD_ART_ABP_SYS^MDC|1.1.1.150037|120|266016^MDC_DIM_MMHG^MDC||DEMO|||R|||20200825020835-0800
OBX|13|NM|150039^MDC_PRESS_BLD_ART_ABP_MEAN^MDC|1.1.1.150039|93|266016^MDC_DIM_MMHG^MDC||DEMO|||R|||20200825020835-0800
OBX|14|NM|150038^MDC_PRESS_BLD_ART_ABP_DIA^MDC|1.1.1.150038|80|266016^MDC_DIM_MMHG^MDC||DEMO|||R|||20200825020835-0800
OBX|15|NM|364^MNDRY_BLD_PULS_RATE_ART_ABP^99MNDRY|1.1.1.364|80|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|16|NM|150087^MDC_PRESS_BLD_VEN_CENT_MEAN^MDC|1.1.1.150087|9|266016^MDC_DIM_MMHG^MDC||DEMO|||R|||20200825020835-0800
OBX|17|NM|150033^MDC_PRESS_BLD_ART_SYS^MDC|1.1.11.150033|120|266016^MDC_DIM_MMHG^MDC||DEMO|||R|||20200825020835-0800
OBX|18|NM|150035^MDC_PRESS_BLD_ART_MEAN^MDC|1.1.11.150035|93|266016^MDC_DIM_MMHG^MDC||DEMO|||R|||20200825020835-0800
OBX|19|NM|150034^MDC_PRESS_BLD_ART_DIA^MDC|1.1.11.150034|80|266016^MDC_DIM_MMHG^MDC||DEMO|||R|||20200825020835-0800
OBX|20|NM|149522^MDC_BLD_PULS_RATE_INV^MDC|1.1.11.149522|80|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|21|NM|150087^MDC_PRESS_BLD_VEN_CENT_MEAN^MDC|1.1.12.150087|9|266016^MDC_DIM_MMHG^MDC||DEMO|||R|||20200825020835-0800
OBX|22|NM|150344^MDC_TEMP^MDC|1.2.1.150344|99.5|266560^MDC_DIM_FAHR^MDC||DEMO|||R|||20200825020835-0800
OBX|23|NM|150344^MDC_TEMP^MDC|1.2.2.150344|97.7|266560^MDC_DIM_FAHR^MDC||DEMO|||R|||20200825020835-0800
OBX|24|NM|188440^MDC_TEMP_DIFF^MDC|1.2.4.188440|1.8|266560^MDC_DIM_FAHR^MDC||DEMO|||R|||20200825020835-0800
OBX|25|NM|152108^MDC_CONC_AWAY_N2O_ET^MDC|1.9.1.152108|45|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|26|NM|152192^MDC_CONC_AWAY_N2O_INSP^MDC|1.9.1.152192|50|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|27|NM|152096^MDC_CONC_AWAY_SEVOFL_ET^MDC|1.9.1.152096|2.7|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|28|NM|152180^MDC_CONC_AWAY_SEVOFL_INSP^MDC|1.9.1.152180|2.4|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|29|NM|151594^MDC_CO2_RESP_RATE^MDC|1.8.1.151594|20|264928^MDC_DIM_RESP_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|30|NM|119^MNDRY_CONC_MAC^99MNDRY|1.9.1.119|1.7|262656^MDC_DIM_DIMLESS^MDC||DEMO|||R|||20200825020835-0800
OBX|31|NM|151708^MDC_CONC_AWAY_CO2_ET^MDC|1.8.1.151708|38|266016^MDC_DIM_MMHG^MDC||DEMO|||R|||20200825020835-0800
OBX|32|NM|151716^MDC_CONC_AWAY_CO2_INSP^MDC|1.8.1.151716|2|266016^MDC_DIM_MMHG^MDC||DEMO|||R|||20200825020835-0800
OBX|33|NM|152440^MDC_CONC_AWAY_O2_ET^MDC|1.9.1.152440|27|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|34|NM|152196^MDC_CONC_AWAY_O2_INSP^MDC|1.9.1.152196|27|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|35|NM|151570^MDC_AWAY_RESP_RATE^MDC|1.11.4.151570|18|264928^MDC_DIM_RESP_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|36|NM|151884^MDC_VOL_MINUTE_AWAY_EXP^MDC|1.11.3.151884|8.82|265216^MDC_DIM_L_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|37|NM|151804^MDC_PRESS_AWAY_END_EXP_POS^MDC|1.11.1.151804|3.5|266048^MDC_DIM_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|38|NM|151817^MDC_PRESS_AWAY_INSP_PEAK^MDC|1.11.1.151817|13|266048^MDC_DIM_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|39|SN|151832^MDC_RATIO_IE^MDC|1.11.4.151832|^1^:^2|262656^MDC_DIM_DIMLESS^MDC||DEMO|||R|||20200825020835-0800
OBX|40|NM|145^MNDRY_RATIO_VOL_FORCED_EXP^99MNDRY|1.11.4.145|71|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|41|NM|151819^MDC_PRESS_AWAY_INSP_MEAN^MDC|1.11.1.151819|6.5|266048^MDC_DIM_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|42|NM|144^MNDRY_VOL_AWAY_TIDAL_INSP^99MNDRY|1.11.3.144|490|263762^MDC_DIM_MILLI_L^MDC||DEMO|||R|||20200825020835-0800
OBX|43|NM|143^MNDRY_VOL_AWAY_TIDAL_EXP^99MNDRY|1.11.3.143|490|263762^MDC_DIM_MILLI_L^MDC||DEMO|||R|||20200825020835-0800
OBX|44|NM|151888^MDC_VOL_MINUTE_AWAY_INSP^MDC|1.11.3.151888|8.82|265216^MDC_DIM_L_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|45|NM|151769^MDC_FLOW_AWAY_EXP_MAX^MDC|1.11.2.151769|33|265216^MDC_DIM_L_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|46|NM|151773^MDC_FLOW_AWAY_INSP_MAX^MDC|1.11.2.151773|35|265216^MDC_DIM_L_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|47|NM|151784^MDC_PRESS_RESP_PLAT^MDC|1.11.1.151784|5.0|266048^MDC_DIM_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|48|NM|151688^MDC_COMPL_LUNG^MDC|1.11.4.151688|33|268050^MDC_DIM_MILLI_L_PER_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|49|NM|151840^MDC_RES_AWAY^MDC|1.11.4.151840|2.6|268064^MDC_DIM_CM_H2O_PER_L_PER_SEC^MDC||DEMO|||R|||20200825020835-0800
OBX|50|NM|146^MNDRY_RAPID_SHALLOW_BREATH_INDEX^99MNDRY|1.11.4.146|37|270848^MDC_DIM_BREATHS_PER_MIN_PER_L^MDC||DEMO|||R|||20200825020835-0800
OBX|51|NM|193^MNDRY_PRESSURE_NEGATIVE_INSPIRATORY^99MNDRY|1.11.1.193|0.0|266048^MDC_DIM_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|52|NM|183^MNDRY_WK_OF_BREATHING_VENT^99MNDRY|1.11.4.183|3.40|10009^MNDRY_DIM_JOULES_PER_L^99MNDRY||DEMO|||R|||20200825020835-0800
OBX|53|NM|150492^MDC_OUTPUT_CARD_CTS^MDC|1.6.2.150492|5.50|265216^MDC_DIM_L_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|54|NM|378^MNDRY_OUTPUT_CARD_INDEX_CTS^99MNDRY|1.6.2.378|9.76|264992^MDC_DIM_L_PER_MIN_PER_M_SQ^MDC||DEMO|||R|||20200825020835-0800
OBX|55|NM|188436^MDC_TEMP_BLD^MDC|1.6.1.188436|98.6|266560^MDC_DIM_FAHR^MDC||DEMO|||R|||20200825020835-0800
OBX|56|NM|150376^MDC_TEMP_INJ^MDC|1.6.1.150376|77.0|266560^MDC_DIM_FAHR^MDC||DEMO|||R|||20200825020835-0800
OBX|57|NM|150312^MDC_RES_VASC_SYS^MDC|1.6.4.150312|1237|10000^MNDRY_DIM_DYNE_SEC_PER_CM5^99MNDRY||DEMO|||R|||20200825020835-0800
OBX|58|NM|149760^MDC_RES_VASC_SYS_INDEX^MDC|1.6.4.149760|2800|268160^MDC_DIM_DYNE_SEC_PER_M_SQ_PER_CM_5^MDC||DEMO|||R|||20200825020835-0800
OBX|59|NM|150404^MDC_VOL_BLD_STROKE^MDC|1.6.3.150404|118|263762^MDC_DIM_MILLI_L^MDC||DEMO|||R|||20200825020835-0800
OBX|60|NM|147^MNDRY_VOL_BLD_STROKE_INDEX^99MNDRY|1.6.3.147|35|263570^MDC_DIM_MILLI_L_PER_M_SQ^MDC||DEMO|||R|||20200825020835-0800
OBX|61|NM|147842^MDC_ECG_CARD_BEAT_RATE^MDC|1.6.3.147842|60|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|62|NM|148^MNDRY_VOL_BLD_STROKE_VARIATION^99MNDRY|1.6.3.148|27|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|63|NM|153^MNDRY_PRESS_PULSE_VARIATION^99MNDRY|1.6.3.153|12|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|64|NM|160^MNDRY_POWER_CARD_OUTPUT^99MNDRY|1.6.3.160|1.37|266176^MDC_DIM_WATT^MDC||DEMO|||R|||20200825020835-0800
OBX|65|NM|161^MNDRY_POWER_CARD_OUTPUT_INDEX^99MNDRY|1.6.3.161|0.40|10013^MNDRY_DIM_WATT_PER_M_SQ^99MNDRY||DEMO|||R|||20200825020835-0800
OBX|66|NM|156^MNDRY_CONTRACTILITY_LEFT_VENT^99MNDRY|1.6.3.156|243|10014^MNDRY_DIM_MMHG_PER_SEC^99MNDRY||DEMO|||R|||20200825020835-0800
OBX|67|NM|312^MNDRY_TEMP_BLD_DIFF^99MNDRY|1.6.1.312|0.0|266560^MDC_DIM_FAHR^MDC||DEMO|||R|||20200825020835-0800
OBX|68|NM|155024^MDC_EEG_PAROX_CRTX_BURST_SUPPRN^MDC|1.17.1.155024|11|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|69|NM|153992^MDC_EEG_FREQ_PWR_SPEC_CRTX_SPECTRAL_EDGE^MDC|1.17.1.153992|21.0|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|70|NM|153984^MDC_EEG_FREQ_PWR_SPEC_CRTX_MEDIAN^MDC|1.17.1.153984|14.5|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|71|NM|153988^MDC_EEG_FREQ_PWR_SPEC_CRTX_PEAK^MDC|1.17.1.153988|15.0|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|72|NM|154040^MDC_EEG_PWR_SPEC_TOT^MDC|1.17.1.154040|42|268576^MDC_DIM_DECIBEL^MDC||DEMO|||R|||20200825020835-0800
OBX|73|NM|153916^MDC_EMG_ELEC_POTL_MUSCL^MDC|1.17.1.153916|32|268576^MDC_DIM_DECIBEL^MDC||DEMO|||R|||20200825020835-0800
OBX|74|NM|154076^MDC_EEG_PWR_SPEC_DELTA_REL^MDC|1.17.1.154076|57|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|75|NM|154080^MDC_EEG_PWR_SPEC_THETA_REL^MDC|1.17.1.154080|20|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|76|NM|154068^MDC_EEG_PWR_SPEC_ALPHA_REL^MDC|1.17.1.154068|55|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|77|NM|154072^MDC_EEG_PWR_SPEC_BETA_REL^MDC|1.17.1.154072|525|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|78|NM|155024^MDC_EEG_PAROX_CRTX_BURST_SUPPRN^MDC|1.17.2.155024|11|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|79|NM|153992^MDC_EEG_FREQ_PWR_SPEC_CRTX_SPECTRAL_EDGE^MDC|1.17.2.153992|21.0|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|80|NM|153984^MDC_EEG_FREQ_PWR_SPEC_CRTX_MEDIAN^MDC|1.17.2.153984|14.5|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|81|NM|153988^MDC_EEG_FREQ_PWR_SPEC_CRTX_PEAK^MDC|1.17.2.153988|15.0|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|82|NM|154040^MDC_EEG_PWR_SPEC_TOT^MDC|1.17.2.154040|42|268576^MDC_DIM_DECIBEL^MDC||DEMO|||R|||20200825020835-0800
OBX|83|NM|153916^MDC_EMG_ELEC_POTL_MUSCL^MDC|1.17.2.153916|32|268576^MDC_DIM_DECIBEL^MDC||DEMO|||R|||20200825020835-0800
OBX|84|NM|154076^MDC_EEG_PWR_SPEC_DELTA_REL^MDC|1.17.2.154076|57|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|85|NM|154080^MDC_EEG_PWR_SPEC_THETA_REL^MDC|1.17.2.154080|20|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|86|NM|154068^MDC_EEG_PWR_SPEC_ALPHA_REL^MDC|1.17.2.154068|55|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|87|NM|154072^MDC_EEG_PWR_SPEC_BETA_REL^MDC|1.17.2.154072|525|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|88|NM|155024^MDC_EEG_PAROX_CRTX_BURST_SUPPRN^MDC|1.17.3.155024|11|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|89|NM|153992^MDC_EEG_FREQ_PWR_SPEC_CRTX_SPECTRAL_EDGE^MDC|1.17.3.153992|21.0|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|90|NM|153984^MDC_EEG_FREQ_PWR_SPEC_CRTX_MEDIAN^MDC|1.17.3.153984|14.5|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|91|NM|153988^MDC_EEG_FREQ_PWR_SPEC_CRTX_PEAK^MDC|1.17.3.153988|15.0|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|92|NM|154040^MDC_EEG_PWR_SPEC_TOT^MDC|1.17.3.154040|42|268576^MDC_DIM_DECIBEL^MDC||DEMO|||R|||20200825020835-0800
OBX|93|NM|153916^MDC_EMG_ELEC_POTL_MUSCL^MDC|1.17.3.153916|32|268576^MDC_DIM_DECIBEL^MDC||DEMO|||R|||20200825020835-0800
OBX|94|NM|154076^MDC_EEG_PWR_SPEC_DELTA_REL^MDC|1.17.3.154076|57|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|95|NM|154080^MDC_EEG_PWR_SPEC_THETA_REL^MDC|1.17.3.154080|20|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|96|NM|154068^MDC_EEG_PWR_SPEC_ALPHA_REL^MDC|1.17.3.154068|55|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|97|NM|154072^MDC_EEG_PWR_SPEC_BETA_REL^MDC|1.17.3.154072|525|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|98|NM|155024^MDC_EEG_PAROX_CRTX_BURST_SUPPRN^MDC|1.17.4.155024|11|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|99|NM|153992^MDC_EEG_FREQ_PWR_SPEC_CRTX_SPECTRAL_EDGE^MDC|1.17.4.153992|21.0|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|100|NM|153984^MDC_EEG_FREQ_PWR_SPEC_CRTX_MEDIAN^MDC|1.17.4.153984|14.5|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|101|NM|153988^MDC_EEG_FREQ_PWR_SPEC_CRTX_PEAK^MDC|1.17.4.153988|15.0|264640^MDC_DIM_HZ^MDC||DEMO|||R|||20200825020835-0800
OBX|102|NM|154040^MDC_EEG_PWR_SPEC_TOT^MDC|1.17.4.154040|42|268576^MDC_DIM_DECIBEL^MDC||DEMO|||R|||20200825020835-0800
OBX|103|NM|153916^MDC_EMG_ELEC_POTL_MUSCL^MDC|1.17.4.153916|32|268576^MDC_DIM_DECIBEL^MDC||DEMO|||R|||20200825020835-0800
OBX|104|NM|154076^MDC_EEG_PWR_SPEC_DELTA_REL^MDC|1.17.4.154076|57|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|105|NM|154080^MDC_EEG_PWR_SPEC_THETA_REL^MDC|1.17.4.154080|20|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|106|NM|154068^MDC_EEG_PWR_SPEC_ALPHA_REL^MDC|1.17.4.154068|55|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|107|NM|154072^MDC_EEG_PWR_SPEC_BETA_REL^MDC|1.17.4.154072|525|262688^MDC_DIM_PERCENT^MDC||DEMO|||R|||20200825020835-0800
OBX|108|NM|149530^MDC_PULS_OXIM_PULS_RATE^MDC|1.3.1.149530|60|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|109|NM|151594^MDC_CO2_RESP_RATE^MDC|1.8.1.151594|20|264928^MDC_DIM_RESP_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|110|NM|382^MNDRY_VOL_CO2_PROD_RESP_BREATH^99MNDRY|1.32.1.382|20|263762^MDC_DIM_MILLI_L^MDC||DEMO|||R|||20200825020835-0800
OBX|111|NM|151776^MDC_FLOW_CO2_PROD_RESP^MDC|1.32.1.151776|200|265234^MDC_DIM_MILLI_L_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|112|NM|389^MNDRY_VOL_O2_CONSUMP_BREATH^99MNDRY|1.32.1.389|25|263762^MDC_DIM_MILLI_L^MDC||DEMO|||R|||20200825020835-0800
OBX|113|NM|152420^MDC_FLOW_O2_CONSUMP^MDC|1.32.1.152420|250|265234^MDC_DIM_MILLI_L_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|114|NM|151828^MDC_QUO_RESP^MDC|1.32.1.151828|0.80|262656^MDC_DIM_DIMLESS^MDC||DEMO|||R|||20200825020835-0800
OBX|115|NM|152812^MDC_RESP_EXPENDED_ENERGY^MDC|1.32.1.152812|1709|270563^MDC_DIM_KILO_CAL_PER_DAY^MDC||DEMO|||R|||20200825020835-0800
OBX|116|NM|151976^MDC_VENT_PRESS_AWAY_END_EXP_POS^MDC|1.13.1.151976|12.0|266048^MDC_DIM_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|117|NM|20017^MNDRY_PRESS_AWAY_END_EXP_POS_SETTING^99MNDRY|1.13.1.20017|12.0|266048^MDC_DIM_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|118|NM|151817^MDC_PRESS_AWAY_INSP_PEAK^MDC|1.13.1.151817|18|266048^MDC_DIM_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|119|NM|151784^MDC_PRESS_RESP_PLAT^MDC|1.13.1.151784|15|266048^MDC_DIM_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|120|NM|151819^MDC_PRESS_AWAY_INSP_MEAN^MDC|1.13.1.151819|6.0|266048^MDC_DIM_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|121|NM|151972^MDC_VENT_PRESS_AWAY^MDC|1.13.1.151972|9.0|266048^MDC_DIM_CM_H2O^MDC||DEMO|||R|||20200825020835-0800
OBX|122|NM|331^MNDRY_VOL_AWAY_TIDAL^99MNDRY|1.13.1.331|300|263762^MDC_DIM_MILLI_L^MDC||DEMO|||R|||20200825020835-0800
OBX|123|NM|143^MNDRY_VOL_AWAY_TIDAL_EXP^99MNDRY|1.13.1.143|300|263762^MDC_DIM_MILLI_L^MDC||DEMO|||R|||20200825020835-0800
OBX|124|NM|144^MNDRY_VOL_AWAY_TIDAL_INSP^99MNDRY|1.13.1.144|500|263762^MDC_DIM_MILLI_L^MDC||DEMO|||R|||20200825020835-0800
OBX|125|NM|176^MNDRY_VOL_EXP_TIDAL_PER_WEIGHT^99MNDRY|1.13.1.176|7|265330^MDC_DIM_MILLI_L_PER_KG^MDC||DEMO|||R|||20200825020835-0800
OBX|126|NM|177^MNDRY_VOL_SPON_EXP_TIDAL^99MNDRY|1.13.1.177|500|263762^MDC_DIM_MILLI_L^MDC||DEMO|||R|||20200825020835-0800
OBX|127|NM|20062^MNDRY_VOL_AWAY_TIDAL_APNEA_SETTING^99MNDRY|1.13.1.20062|490|263762^MDC_DIM_MILLI_L^MDC||DEMO|||R|||20200825020835-0800
OBX|128|NM|152008^MDC_VENT_VOL_MINUTE_AWAY^MDC|1.13.1.152008|15.0|265216^MDC_DIM_L_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|129|NM|152000^MDC_VENT_VOL_MINUTE_EXP^MDC|1.13.1.152000|15.0|265216^MDC_DIM_L_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|130|NM|152004^MDC_VENT_VOL_MINUTE_INSP^MDC|1.13.1.152004|15.0|265216^MDC_DIM_L_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|131|NM|178^MNDRY_BREATH_RATE_TOTAL^99MNDRY|1.13.1.178|30|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800
OBX|132|NM|180^MNDRY_BREATH_RATE_SPONT^99MNDRY|1.13.1.180|30|264864^MDC_DIM_BEAT_PER_MIN^MDC||DEMO|||R|||20200825020835-0800"""
        ret = {}
        obxs=[]
        msg=hl7parser.hl7.HL7Message(data)
        # print(msg.segments)
        for i in msg.segments:
            line_type, data_obj = i
            line=[str(x) for x in data_obj]
            if line_type=='msh':
                line.insert(0,'|')
            # print(line)
            item=getattr(root,line_type)
            res={}
            for i in line:
                index = item.get(line.index(i) + 1)
                if i and index:
                    res[index['cn']]=i
                    obx_4=res.get('监测参数')
                    match=params_conf.data.get(obx_4)
                    if obx_4 and match:
                        res['监测参数解析']=match[0]
                    obx_5 = res.get('单位')
                    match = unit.data.get(obx_5)
                    if obx_5 and match:
                        res['单位解析'] = match[0]

            if line_type=='obx':
                obxs.append(res)
            else:
                ret[line_type]=res
            ret['obxs']=obxs
        print(ret)
        write_excel(ret)



if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    # parser.add_argument("-t", "--type", type=str, required=True,
    #         help="collect type: http_probe / tcp_probe/ switches_data ...")
    parser.add_argument("-e", "--env", default="dev", choices=["dev", "prod"],
            help="environment: dev or prod")
    parser.add_argument("-d", "--debug", type=Utils.judge_bool, default="true",
            help="log level: true or false")
    args = parser.parse_args()


    ana = Analysis(args.env, args.debug)

    """
    文档第6页 以 MSH 段为例，以下消息为在 TCP 传输中的 MSH 消息实例: 0x0BMSH|^~\&|||||||QRY^R02|||2.6<cr>QRD|19970731145557|R|I|Q839572|||||RES<cr>QRF|M ON||||3232241478&5^1^1^0^151&160&200|<cr>0x1C0x0D
    """

    test_msgs = """0x0BMSH|^~\&|MINDRAY_N-SERIES^00A037009B000000^EUI-64||||20200825020835000-0800||ORU^R01^ORU_R01|1|P|2.6|||AL|NE||UNICODE UTF-8|||IHE_PCD_001^IHE PCD^1.3.6.1.4.1.19376.1.6.1.1.1^ISO<cr>PID|||^^^Hospital^PI||John^Smith-Demo^^^^^L|||M||Unknown<cr>PV1||I|ccu^^12^大连0x1C0x0D"""
    ana.process(test_msgs)