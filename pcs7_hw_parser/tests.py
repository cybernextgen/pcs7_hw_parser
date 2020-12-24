#!/usr/bin/env python
# coding: utf8

import unittest
from parsers.dp_module_parser import DPModuleParser
from parsers.rack_module_parser import RackModuleParser
from models import DPModule, RackModule


class ParserTestCase(unittest.TestCase):

    def do_test(self, str_to_parse, obj_to_compare):
        result = {}
        parser = self.parser_class(result)
        parser.parse(str_to_parse)

        key, modules = result.popitem()
        self.assertTrue(len(modules) == 1)
        self.assertEqual(modules[0], obj_to_compare)


class DPModuleParserTestCase(ParserTestCase):

    def setUp(self):
        self.parser_class = DPModuleParser

    def test_parse_SM321_module(self):
        str_to_parse = """
DPSUBSYSTEM 1, DPADDRESS 3, SLOT 9, "6ES7 321-7BH00-0AB0", "RSU1_A3_8"
BEGIN 
  ASSET_ID "66762747CBD24BB0B7332AE838CD09A2"
  PROFIBUSADDRESS "0"
  CPU_NO "1"
  ALARM_OB_NO "40"
  TIMESTAMP "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
  OBJECT_REMOVEABLE "1"
  POS_X "0"
  POS_Y "0"
  REDUNDANCY
  BEGIN
  END
  SIZE_X "0"
  MODULE_ADD_FLAGS "0"
  SIZE_Y "0"
  CAX_APP_ID ""
  OBJECT_COPYABLE "1"
  CREATOR ""
  COMMENT "DI16"
LOCAL_IN_ADDRESSES 
  ADDRESS  0, 0, 2, 5, 1, 0
SYMBOL  I , 0, "RSU1_1_IN1_OK", "Ввод 1 в норме"
SYMBOL  I , 1, "RSU1_1_IN2_OK", "Ввод 2 в норме"
SYMBOL  I , 2, "RSU1_1_1QF_ON", "Автомат 1QF включен"
SYMBOL  I , 3, "RSU1_1_2QF_ON", "Автомат 2QF включен"
SYMBOL  I , 4, "RSU1_1_S_F", "Неисправность Scalance"
SYMBOL  I , 9, "DE_HS_14702A_C", "Подача пробы на ""Backman"" A закр."
SYMBOL  I , 10, "DE_HS_14702A_O", "Подача пробы на ""Backman"" A откр."
SYMBOL  I , 11, "DE_HS_14702B_C", "Подача пробы на ""Backman"" B закр."
SYMBOL  I , 12, "DE_HS_14702B_O", "Подача пробы на ""Backman"" B откр."
SYMBOL  I , 13, "DE_HS_31701_C", "Ручное закрытие клапана FRCV-31201 на трубопроводе питания колонны С301"
SYMBOL  I , 14, "DE_HS_31701_O", "Ручное открытие клапана FRCV-31201 на трубопроводе питания колонны С301"
SYMBOL  I , 15, "DE_ES_11001", "Not Aus"
PARAMETER 
  INPUT_DELAY_MS, "3_(DC)"
  MISSING_SENSOR_SUPPLY, DI , 0, "1"
  MISSING_SENSOR_SUPPLY, DI , 1, "1"
  MISSING_SENSOR_SUPPLY, DI , 2, "1"
  MISSING_SENSOR_SUPPLY, DI , 3, "1"
  MISSING_SENSOR_SUPPLY, DI , 4, "1"
  MISSING_SENSOR_SUPPLY, DI , 5, "1"
  MISSING_SENSOR_SUPPLY, DI , 6, "1"
  MISSING_SENSOR_SUPPLY, DI , 7, "1"
  HW_INT_ENABLE, "0"
  DIAGNOSTICS, "1"
  RISING_EDGE, DI , 0, "0"
  RISING_EDGE, DI , 1, "0"
  RISING_EDGE, DI , 2, "0"
  RISING_EDGE, DI , 3, "0"
  RISING_EDGE, DI , 4, "0"
  RISING_EDGE, DI , 5, "0"
  RISING_EDGE, DI , 6, "0"
  RISING_EDGE, DI , 7, "0"
  FALLING_EDGE, DI , 0, "0"
  FALLING_EDGE, DI , 1, "0"
  FALLING_EDGE, DI , 2, "0"
  FALLING_EDGE, DI , 3, "0"
  FALLING_EDGE, DI , 4, "0"
  FALLING_EDGE, DI , 5, "0"
  FALLING_EDGE, DI , 6, "0"
  FALLING_EDGE, DI , 7, "0"
END 
        """

        obj_to_compare = DPModule(**{
            'order_num': '6ES7 321-7BH00-0AB0',
            'position_name': 'RSU1_A3_8',
            'slot_num': '9',
            'dp_address': '3',
            'dp_subsystem': '1',
            'channels': {
                0: {'ch_type': 'I', 'ch_number': '0', 'ch_position_name': 'RSU1_1_IN1_OK', 'ch_description': 'Ввод 1 в норме'},
                1: {'ch_type': 'I', 'ch_number': '1', 'ch_position_name': 'RSU1_1_IN2_OK', 'ch_description': 'Ввод 2 в норме'},
                2: {'ch_type': 'I', 'ch_number': '2', 'ch_position_name': 'RSU1_1_1QF_ON', 'ch_description': 'Автомат 1QF включен'},
                3: {'ch_type': 'I', 'ch_number': '3', 'ch_position_name': 'RSU1_1_2QF_ON', 'ch_description': 'Автомат 2QF включен'},
                4: {'ch_type': 'I', 'ch_number': '4', 'ch_position_name': 'RSU1_1_S_F', 'ch_description': 'Неисправность Scalance'},
                13: {'ch_type': 'I', 'ch_number': '13', 'ch_position_name': 'DE_HS_31701_C', 'ch_description': 'Ручное закрытие клапана FRCV-31201 на трубопроводе питания колонны С301'},
                14: {'ch_type': 'I', 'ch_number': '14', 'ch_position_name': 'DE_HS_31701_O', 'ch_description': 'Ручное открытие клапана FRCV-31201 на трубопроводе питания колонны С301'},
                15: {'ch_type': 'I', 'ch_number': '15', 'ch_position_name': 'DE_ES_11001', 'ch_description': 'Not Aus'}
            }
        })
        self.do_test(str_to_parse, obj_to_compare)

    def test_parse_SM322_module(self):
        str_to_parse = """
DPSUBSYSTEM 1, DPADDRESS 3, SLOT 10, "6ES7 322-1BF01-0AA0", "RSU1_A3_9"
BEGIN 
  ASSET_ID "57125DA01B524CE9BD56C9CCD26A79D5"
  PROFIBUSADDRESS "0"
  CPU_NO "1"
  ALARM_OB_NO "40"
  OBJECT_REMOVEABLE "1"
  POS_X "0"
  POS_Y "0"
  REDUNDANCY
  BEGIN
  END
  SIZE_X "0"
  MODULE_ADD_FLAGS "0"
  SIZE_Y "0"
  CAX_APP_ID ""
  OBJECT_COPYABLE "1"
  CREATOR ""
  COMMENT "DO8"
LOCAL_OUT_ADDRESSES 
  ADDRESS  0, 0, 1, 5, 1, 0
SYMBOL  O , 1, "DO_H3_R102A", "Подтверждение открытия HSV14702A"
SYMBOL  O , 2, "DO_H2_R102B", "Подтверждение открытия HSV14702B"
SYMBOL  O , 3, "DO_H7_31101", "Подтверждение открытия HSV31101"
END 
        """
        obj_to_compare = DPModule(**{
            'order_num': '6ES7 322-1BF01-0AA0',
            'position_name': 'RSU1_A3_9',
            'slot_num': '10',
            'dp_address': '3',
            'dp_subsystem': '1',
            'channels': {
                1: {'ch_type': 'O', 'ch_number': '1', 'ch_position_name': 'DO_H3_R102A', 'ch_description': 'Подтверждение открытия HSV14702A'},
                2: {'ch_type': 'O', 'ch_number': '2', 'ch_position_name': 'DO_H2_R102B', 'ch_description': 'Подтверждение открытия HSV14702B'},
                3: {'ch_type': 'O', 'ch_number': '3', 'ch_position_name': 'DO_H7_31101', 'ch_description': 'Подтверждение открытия HSV31101'}
            }
        })

        self.do_test(str_to_parse, obj_to_compare)

    def test_parse_SM331_module(self):
        str_to_parse = """
DPSUBSYSTEM 1, DPADDRESS 3, SLOT 11, "6ES7 331-7KF01-0AB0", "RSU1_A3_10"
BEGIN 
  ASSET_ID "4C3AFED1C47F4D55A7693B7ED399FC44"
  PROFIBUSADDRESS "0"
  CPU_NO "1"
  ALARM_OB_NO "40"
  OBJECT_REMOVEABLE "1"
  POS_X "30"
  POS_Y "30"
  REDUNDANCY
  BEGIN
  END
  SIZE_X "0"
  MODULE_ADD_FLAGS "0"
  SIZE_Y "0"
  CAX_APP_ID ""
  OBJECT_COPYABLE "1"
  CREATOR ""
  COMMENT "AI8"
LOCAL_IN_ADDRESSES 
  ADDRESS  936, 0, 16, 4, 1, 0
SYMBOL  I , 0, "T_PAZ1", "Температура в шкафу ПАЗ"
SYMBOL  I , 2, "T_RSU1_1", "Температура в шкафу РСУ 1.1"
SYMBOL  I , 4, "MT7", "Значение напряжения питания в шкафу ВС Mt7"
SYMBOL  I , 5, "MT9", "Значение напряжения питания в шкафу ВС Mt9"
SYMBOL  I , 6, "MT12", "Значение напряжения питания в шкафу ВС Mt12"
PARAMETER 
  GROUP_DIAGNOSIS, AI , 0, "1"
  GROUP_DIAGNOSIS, AI , 1, "1"
  GROUP_DIAGNOSIS, AI , 2, "1"
  GROUP_DIAGNOSIS, AI , 3, "1"
  WIRE_BREAK, AI , 0, "1"
  WIRE_BREAK, AI , 1, "1"
  WIRE_BREAK, AI , 2, "0"
  WIRE_BREAK, AI , 3, "0"
  LIMIT_VIOLATION, "0"
  DIAGNOSTICS, "1"
  INTEGRATION_TIME, AI , 0, "20_MS"
  INTEGRATION_TIME, AI , 1, "20_MS"
  INTEGRATION_TIME, AI , 2, "20_MS"
  INTEGRATION_TIME, AI , 3, "20_MS"
  AI_TYPE, AI , 0, "THERMAL_RESISTANCE_(LIN.,4-WIRE)"
  AI_TYPE, AI , 1, "THERMAL_RESISTANCE_(LIN.,4-WIRE)"
  AI_TYPE, AI , 2, "VOLTAGE"
  AI_TYPE, AI , 3, "VOLTAGE"
  AI_RANGE, AI , 0, "PT_100_STANDARD_RANGE"
  AI_RANGE, AI , 1, "PT_100_STANDARD_RANGE"
  AI_RANGE, AI , 2, "+/-_10_V"
  AI_RANGE, AI , 3, "+/-_10_V"
  UPPER_LIMIT_VALUE, AI , 0, "3276.700000000001"
  UPPER_LIMIT_VALUE, AI , 1, "3276.700000000001"
  LOWER_LIMIT_VALUE, AI , 0, "-3276.800000000001"
  LOWER_LIMIT_VALUE, AI , 1, "-3276.800000000001"
END 
        """

        obj_to_compare = DPModule(**{
            'order_num': '6ES7 331-7KF01-0AB0',
            'position_name': 'RSU1_A3_10',
            'slot_num': '11',
            'dp_address': '3',
            'dp_subsystem': '1',
            'channels': {
                0: {'ch_type': 'I', 'ch_number': '0', 'ch_position_name': 'T_PAZ1', 'ch_description': 'Температура в шкафу ПАЗ'},
                2: {'ch_type': 'I', 'ch_number': '2', 'ch_position_name': 'T_RSU1_1', 'ch_description': 'Температура в шкафу РСУ 1.1'},
                4: {'ch_type': 'I', 'ch_number': '4', 'ch_position_name': 'MT7', 'ch_description': 'Значение напряжения питания в шкафу ВС Mt7'}, 5: {'ch_type': 'I', 'ch_number': '5', 'ch_position_name': 'MT9', 'ch_description': 'Значение напряжения питания в шкафу ВС Mt9'},
                6: {'ch_type': 'I', 'ch_number': '6', 'ch_position_name': 'MT12', 'ch_description': 'Значение напряжения питания в шкафу ВС Mt12'}
            }
        })

        self.do_test(str_to_parse, obj_to_compare)

    def test_parse_SM332_module(self):
        str_to_parse = """
DPSUBSYSTEM 1, DPADDRESS 19, SLOT 5, "6ES7 332-5HD01-0AB0", "RSU1_A19_4"
BEGIN 
  ASSET_ID "7215CB26EC914AE4AED8FE582E8AC4C5"
  PROFIBUSADDRESS "0"
  CPU_NO "1"
  ALARM_OB_NO "40"
  OBJECT_REMOVEABLE "1"
  POS_X "0"
  POS_Y "0"
  REDUNDANCY
  BEGIN
  END
  SIZE_X "0"
  MODULE_ADD_FLAGS "0"
  SIZE_Y "0"
  CAX_APP_ID ""
  OBJECT_COPYABLE "1"
  CREATOR ""
  COMMENT "AO4"
LOCAL_OUT_ADDRESSES 
  ADDRESS  680, 0, 8, 5, 1, 0
SYMBOL  O , 0, "QW642", "Резерв"
SYMBOL  O , 1, "QW644", "Резерв"
SYMBOL  O , 2, "QW646", "Резерв"
SYMBOL  O , 3, "QW648", "Резерв"
PARAMETER 
  DIAGNOSTICS, "1"
  REACTION_TO_CPU_STOP, AO , 0, "OUTPUTS_WITHOUT_VOLTAGE_OR_CURRENT"
  REACTION_TO_CPU_STOP, AO , 1, "OUTPUTS_WITHOUT_VOLTAGE_OR_CURRENT"
  REACTION_TO_CPU_STOP, AO , 2, "OUTPUTS_WITHOUT_VOLTAGE_OR_CURRENT"
  REACTION_TO_CPU_STOP, AO , 3, "OUTPUTS_WITHOUT_VOLTAGE_OR_CURRENT"
  AO_TYPE, AO , 0, "DEACTIVATED"
  AO_TYPE, AO , 1, "DEACTIVATED"
  AO_TYPE, AO , 2, "DEACTIVATED"
  AO_TYPE, AO , 3, "DEACTIVATED"
  AO_RANGE, AO , 0, "ZERO_VALUE"
  AO_RANGE, AO , 1, "ZERO_VALUE"
  AO_RANGE, AO , 2, "ZERO_VALUE"
  AO_RANGE, AO , 3, "ZERO_VALUE"
  SUBSTITUTE_VALUE, AO , 0, "0.000000000000"
  SUBSTITUTE_VALUE, AO , 1, "0.000000000000"
  SUBSTITUTE_VALUE, AO , 2, "0.000000000000"
  SUBSTITUTE_VALUE, AO , 3, "0.000000000000"
END 
        """
        obj_to_compare = DPModule(**{
            'order_num': '6ES7 332-5HD01-0AB0',
            'position_name': 'RSU1_A19_4',
            'slot_num': '5',
            'dp_address': '19',
            'dp_subsystem': '1',
            'channels': {
                0: {'ch_type': 'O', 'ch_number': '0', 'ch_position_name': 'QW642', 'ch_description': 'Резерв'},
                1: {'ch_type': 'O', 'ch_number': '1', 'ch_position_name': 'QW644', 'ch_description': 'Резерв'},
                2: {'ch_type': 'O', 'ch_number': '2', 'ch_position_name': 'QW646', 'ch_description': 'Резерв'},
                3: {'ch_type': 'O', 'ch_number': '3', 'ch_position_name': 'QW648', 'ch_description': 'Резерв'}
            }
        })
        self.do_test(str_to_parse, obj_to_compare)

    def test_parse_SM326_module(self):
        str_to_parse = """
DPSUBSYSTEM 1, DPADDRESS 3, SLOT 6, "6ES7 326-1BK01-0AB0", "PAZ350_2A2_5"
BEGIN 
  ASSET_ID "9A2D4E2B1EB34A359DC5A32EF7AC4B9A"
  PROFIBUSADDRESS "0"
  CPU_NO "1"
  ALARM_OB_NO "40"
  TIMESTAMP "00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00"
  ATTR_DDX_MODULE ""
  OBJECT_REMOVEABLE "1"
  POS_X "0"
  POS_Y "0"
  REDUNDANCY
  BEGIN
  END
  SIZE_X "0"
  MODULE_ADD_FLAGS "0"
  SIZE_Y "0"
  CAX_APP_ID ""
  OBJECT_COPYABLE "1"
  ATTR_PASSIVATION_TYPE "00 01"
  CREATOR ""
  COMMENT "FDI24"
LOCAL_IN_ADDRESSES 
  ADDRESS  0, 0, 10, 5, 1, 0
LOCAL_OUT_ADDRESSES 
  ADDRESS  0, 0, 4, 5, 1, 0
SYMBOL  I , 0, "PSL350221", "Давление газа к R-3501 (4 южный ряд)"
SYMBOL  I , 1, "XVZH350211", "Клапан подачи топливного газа к R-3501 (открыт)"
SYMBOL  I , 2, "LSHH350304", "Уровень ДХЭ в испарителе V-3512"
SYMBOL  I , 3, "Z3526_ACK", "Разрешение аварийного опорожнения (P52452<ALL)"
SYMBOL  I , 6, "PSL350222", "Давление газа к R-3501 (4 северный ряд)"
SYMBOL  I , 7, "XVZH350212", "Клапан подачи топливного газа к R-3501 (открыт)"
SYMBOL  I , 8, "PSLL350212", "Даления топливного газа к R-3501"
SYMBOL  I , 12, "PSL350223", "Давление газа к R-3501 (3 южный ряд)"
SYMBOL  I , 13, "XVZH350213", "Клапан сброса топливного газа R-3501 (открыт)"
SYMBOL  I , 14, "LSLL350405", "Уровень ДХЭ в колонне закалки С-3501"
SYMBOL  I , 15, "XVZH350204", "Клапан подачи тест газа к R-3501 (открыт)"
SYMBOL  I , 16, "ZSL350215", "Предохранительный клапан тест газа (закрыт)"
SYMBOL  I , 18, "PSL350224", "Давление газа к R-3501 (3 северный ряд)"
SYMBOL  I , 19, "PSLL350214", "Даления топливного газа к R-3501"
SYMBOL  I , 20, "ZSL350221", "Клапан тест газа (3 ряд, юг) (закрыт)"
SYMBOL  I , 21, "ZSL350224", "Клапан тест газа (1 ряд, север) (закрыт)"
SYMBOL  I , 22, "ZSL350226", "Клапан тест газа (4 ряд, юг) (закрыт)"
PARAMETER 
  DIAGNOSTICS, "1"
  F_CHECK_SEQNR, "0"
  F_CHECK_IPAR, "1"
  F_SIL, "2"
  F_CRC_LENGTH, "1"
  F_PRM_FLAG_2, "0"
  F_SOURCE_ADD, "1"
  F_DEST_ADD, "1014"
  F_WD_TIME_MS, "2500"
  F_PAR_CRC1, "1279"
  F_PRM_ID_1, "5"
  F_PRM_ID_2, "0"
  F_MODUL_DEVICE_ADD, "1014"
  F_DATA_SET_CNT, "1"
  MOD_SAFETY_MODE, "1"
  VS1_VS3_SENSOR_SUPPLY_VIA_MODULE, "1"
  VS1_VS3_WITH_SHORT_CIRCUIT_TEST, "1"
  VS2_VS4_SENSOR_SUPPLY_VIA_MODULE, "1"
  VS2_VS4_WITH_SHORT_CIRCUIT_TEST, "1"
  F_CH_00_12_ENABLE_ACTIV, "1"
  F_CH_00_12_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_00_12_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_00_12_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_00_12_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_CH_01_13_ENABLE_ACTIV, "1"
  F_CH_01_13_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_01_13_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_01_13_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_01_13_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_CH_02_14_ENABLE_ACTIV, "1"
  F_CH_02_14_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_02_14_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_02_14_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_02_14_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_CH_03_15_ENABLE_ACTIV, "1"
  F_CH_03_15_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_03_15_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_03_15_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_03_15_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_CH_04_16_ENABLE_ACTIV, "1"
  F_CH_04_16_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_04_16_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_04_16_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_04_16_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_CH_05_17_ENABLE_ACTIV, "1"
  F_CH_05_17_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_05_17_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_05_17_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_05_17_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_CH_06_18_ENABLE_ACTIV, "1"
  F_CH_06_18_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_06_18_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_06_18_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_06_18_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_CH_07_19_ENABLE_ACTIV, "1"
  F_CH_07_19_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_07_19_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_07_19_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_07_19_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_CH_08_20_ENABLE_ACTIV, "1"
  F_CH_08_20_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_08_20_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_08_20_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_08_20_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_CH_09_21_ENABLE_ACTIV, "1"
  F_CH_09_21_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_09_21_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_09_21_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_09_21_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_CH_10_22_ENABLE_ACTIV, "1"
  F_CH_10_22_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_10_22_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_10_22_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_10_22_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_CH_11_23_ENABLE_ACTIV, "1"
  F_CH_11_23_SENSOR_EVALUATION, "1OO1_EVALUATION"
  F_CH_11_23_SENSOR_INTERCONNECTION, "SINGLE_CHANNEL_RELIABLE"
  F_CH_11_23_DISCREPANCY_TIME_MS, "10.000000000000"
  F_CH_11_23_BEHAVIOR_AT_DISCREPANCY, "SUPPLY_LAST_VALID_VALUE"
  F_MODUL_CRC3, "48295"
END 
        """
        obj_to_compare = DPModule(**{
            'order_num': '6ES7 326-1BK01-0AB0',
            'position_name': 'PAZ350_2A2_5',
            'slot_num': '6',
            'dp_address': '3',
            'dp_subsystem': '1',
            'channels': {
                0: {'ch_type': 'I', 'ch_number': '0', 'ch_position_name': 'PSL350221', 'ch_description': 'Давление газа к R-3501 (4 южный ряд)'},
                1: {'ch_type': 'I', 'ch_number': '1', 'ch_position_name': 'XVZH350211', 'ch_description': 'Клапан подачи топливного газа к R-3501 (открыт)'},
                2: {'ch_type': 'I', 'ch_number': '2', 'ch_position_name': 'LSHH350304', 'ch_description': 'Уровень ДХЭ в испарителе V-3512'},
                3: {'ch_type': 'I', 'ch_number': '3', 'ch_position_name': 'Z3526_ACK', 'ch_description': 'Разрешение аварийного опорожнения (P52452<ALL)'},
                6: {'ch_type': 'I', 'ch_number': '6', 'ch_position_name': 'PSL350222', 'ch_description': 'Давление газа к R-3501 (4 северный ряд)'},
                7: {'ch_type': 'I', 'ch_number': '7', 'ch_position_name': 'XVZH350212', 'ch_description': 'Клапан подачи топливного газа к R-3501 (открыт)'},
                8: {'ch_type': 'I', 'ch_number': '8', 'ch_position_name': 'PSLL350212', 'ch_description': 'Даления топливного газа к R-3501'},
                12: {'ch_type': 'I', 'ch_number': '12', 'ch_position_name': 'PSL350223', 'ch_description': 'Давление газа к R-3501 (3 южный ряд)'},
                13: {'ch_type': 'I', 'ch_number': '13', 'ch_position_name': 'XVZH350213', 'ch_description': 'Клапан сброса топливного газа R-3501 (открыт)'},
                14: {'ch_type': 'I', 'ch_number': '14', 'ch_position_name': 'LSLL350405', 'ch_description': 'Уровень ДХЭ в колонне закалки С-3501'},
                15: {'ch_type': 'I', 'ch_number': '15', 'ch_position_name': 'XVZH350204', 'ch_description': 'Клапан подачи тест газа к R-3501 (открыт)'},
                16: {'ch_type': 'I', 'ch_number': '16', 'ch_position_name': 'ZSL350215', 'ch_description': 'Предохранительный клапан тест газа (закрыт)'},
                18: {'ch_type': 'I', 'ch_number': '18', 'ch_position_name': 'PSL350224', 'ch_description': 'Давление газа к R-3501 (3 северный ряд)'},
                19: {'ch_type': 'I', 'ch_number': '19', 'ch_position_name': 'PSLL350214', 'ch_description': 'Даления топливного газа к R-3501'},
                20: {'ch_type': 'I', 'ch_number': '20', 'ch_position_name': 'ZSL350221', 'ch_description': 'Клапан тест газа (3 ряд, юг) (закрыт)'},
                21: {'ch_type': 'I', 'ch_number': '21', 'ch_position_name': 'ZSL350224', 'ch_description': 'Клапан тест газа (1 ряд, север) (закрыт)'},
                22: {'ch_type': 'I', 'ch_number': '22', 'ch_position_name': 'ZSL350226', 'ch_description': 'Клапан тест газа (4 ряд, юг) (закрыт)'}}
            })
        self.do_test(str_to_parse, obj_to_compare)


class RackModuleParserTestCase(ParserTestCase):

    def setUp(self):
        self.parser_class = RackModuleParser

    def test_CPU_module(self):
        str_to_parse = """
RACK 0, SLOT 3, "6ES7 417-4HT14-0AB0" "V4.5", "VC_ESD_CPU0"
BEGIN 
  ASSET_ID "695B5732E89B4B628601BFFB8C1EE2AB"
  ALARM_OB_NO "40"
  YLINK_F_MODULES_CALC "1"
  CBA_USAGE "0"
  RED_LIB_SEL "2"
  CAPABLE_F_SAFETY "0"
  OBJECT_REMOVEABLE "1"
  CAPABLE_FAILSAFE "1"
  POS_X "0"
  POS_Y "0"
  REDUNDANCY
  BEGIN
  END
  SIZE_X "0"
  MODULE_ADD_FLAGS "0"
  SIZE_Y "0"
  KSS_CONNECTION "0"
  REDUNDANT_IO_DB_WORK_IN "1"
  REDUNDANT_IO_DB_WORK_OUT "2"
  CAX_APP_ID ""
  OBJECT_COPYABLE "1"
  CREATOR ""
  UPDATE_RESERVE
  BEGIN
    AUTOCALC "1"
    OB_INTERVAL "200"
    OB_RUNTIME "100"
    MEMORYSIZE "1024"
  END
  MPI_ADDRESS "2"
  COMMENT ""
PARAMETER 
  TEST_ON_COMPLETE_RESTART, "0"
  STARTUP_IF_SETPOINT_CFG_NOT_EQUAL_TO_ACTUAL_CFG, "1"
  DISABLE_HOT_RESTART_ON_MANUAL_STARTUP, "0"
  STARTUP_AFTER_POWER_ON, "COMPLETE_RESTART"
  DELETE_PIQ_ON_HOT_RESTART, "1"
  COLD_RESTART, "WARM_RESTART"
  TIMEBASE, "0"
  TRANSFER_OF_PARAMETERS_TO_MODULES, "60"
  READY_MESSAGE_FROM_MODULES, "6500"
  HOT_RESTART, "0"
  COMMUNICATION, "20"
  UPDATE_PROCESS_IMAGE_TABLE_CYCLICALLY, "1"
  SIZE_OF_PROCESS_IMAGE, "0"
  CALL_OB85_ON_IO_ACCESS_ERROR, "ONLY_FOR_INCOMING_AND_OUTGOING_ERRORS"
  SCAN_CYCLE_MONITORING_TIME, "6000"
  MINIMUM_SCAN_CYCLE_TIME, "0"
  SELF_TEST, "0"
  PRIORITY_CLASS_1, "1024"
  PRIORITY_CLASS_2, "1024"
  PRIORITY_CLASS_3, "256"
  PRIORITY_CLASS_4, "256"
  PRIORITY_CLASS_5, "256"
  PRIORITY_CLASS_6, "256"
  PRIORITY_CLASS_7, "1024"
  PRIORITY_CLASS_8, "1024"
  PRIORITY_CLASS_9, "2048"
  PRIORITY_CLASS_10, "1024"
  PRIORITY_CLASS_11, "1024"
  PRIORITY_CLASS_12, "1024"
  PRIORITY_CLASS_13, "1024"
  PRIORITY_CLASS_14, "1024"
  PRIORITY_CLASS_15, "1024"
  PRIORITY_CLASS_16, "2048"
  PRIORITY_CLASS_17, "256"
  PRIORITY_CLASS_18, "256"
  PRIORITY_CLASS_19, "256"
  PRIORITY_CLASS_20, "256"
  PRIORITY_CLASS_21, "256"
  PRIORITY_CLASS_22, "256"
  PRIORITY_CLASS_23, "256"
  PRIORITY_CLASS_24, "1024"
  PRIORITY_CLASS_25, "1024"
  PRIORITY_CLASS_26, "1024"
  PRIORITY_CLASS_27, "1024"
  PRIORITY_CLASS_28, "1024"
  PRIORITY_CLASS_29, "256"
  SYNC_TYPE_SYNC_IN_PLC, "AS_SLAVE"
  TIME_INTERVAL_SYNC_IN_PLC, "NO"
  SYNC_TYPE_SYNC_ON_MPI, "NONE"
  TIME_INTERVAL_SYNC_ON_MPI, "NO"
  CORRECTION_FACTOR, "100"
  PRIORITY_OB30, "7"
  PRIORITY_OB31, "8"
  PRIORITY_OB32, "9"
  PRIORITY_OB33, "10"
  PRIORITY_OB34, "11"
  PRIORITY_OB35, "16"
  PRIORITY_OB36, "13"
  PRIORITY_OB37, "14"
  PRIORITY_OB38, "15"
  EXECUTION_OB30, "5000"
  EXECUTION_OB31, "2000"
  EXECUTION_OB32, "1000"
  EXECUTION_OB33, "500"
  EXECUTION_OB34, "200"
  EXECUTION_OB35, "200"
  EXECUTION_OB36, "50"
  EXECUTION_OB37, "20"
  EXECUTION_OB38, "10"
  PHASE_OFFSET_OB30, "0"
  PHASE_OFFSET_OB31, "0"
  PHASE_OFFSET_OB32, "0"
  PHASE_OFFSET_OB33, "0"
  PHASE_OFFSET_OB34, "0"
  PHASE_OFFSET_OB35, "0"
  PHASE_OFFSET_OB36, "0"
  PHASE_OFFSET_OB37, "0"
  PHASE_OFFSET_OB38, "0"
  USER_LOCAL_DATA_AREA, "32768"
  SIZE_OF_PROCESS_IMAGE_INPUT, "2048"
  SIZE_OF_PROCESS_IMAGE_OUTPUT, "2048"
  RESERVED, "0"
  MESSAGES, "3000"
  MAX_NUMBER_OF_COMMUNICATION_JOBS, "3000"
  FDL_CONNECTIONS, "64"
  ALARM_S, "200"
  MAX_NUMBER_OF_S7_CONNECTIONS, "0"
  PLANT_DESIGNATION, ""
  LOCAL_DESIGNATION, ""
  PART_PROCESS_IMAGE_INPUTS_OB10, "0"
  PART_PROCESS_IMAGE_INPUTS_OB11, "0"
  PART_PROCESS_IMAGE_INPUTS_OB12, "0"
  PART_PROCESS_IMAGE_INPUTS_OB13, "0"
  PART_PROCESS_IMAGE_INPUTS_OB14, "0"
  PART_PROCESS_IMAGE_INPUTS_OB15, "0"
  PART_PROCESS_IMAGE_INPUTS_OB16, "0"
  PART_PROCESS_IMAGE_INPUTS_OB17, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB10, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB11, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB12, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB13, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB14, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB15, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB16, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB17, "0"
  PART_PROCESS_IMAGE_INPUTS_OB20, "0"
  PART_PROCESS_IMAGE_INPUTS_OB21, "0"
  PART_PROCESS_IMAGE_INPUTS_OB22, "0"
  PART_PROCESS_IMAGE_INPUTS_OB23, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB20, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB21, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB22, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB23, "0"
  PART_PROCESS_IMAGE_INPUTS_OB30, "0"
  PART_PROCESS_IMAGE_INPUTS_OB31, "1"
  PART_PROCESS_IMAGE_INPUTS_OB32, "2"
  PART_PROCESS_IMAGE_INPUTS_OB33, "3"
  PART_PROCESS_IMAGE_INPUTS_OB34, "4"
  PART_PROCESS_IMAGE_INPUTS_OB35, "5"
  PART_PROCESS_IMAGE_INPUTS_OB36, "6"
  PART_PROCESS_IMAGE_INPUTS_OB37, "7"
  PART_PROCESS_IMAGE_INPUTS_OB38, "8"
  PART_PROCESS_IMAGE_OUTPUTS_OB30, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB31, "1"
  PART_PROCESS_IMAGE_OUTPUTS_OB32, "2"
  PART_PROCESS_IMAGE_OUTPUTS_OB33, "3"
  PART_PROCESS_IMAGE_OUTPUTS_OB34, "4"
  PART_PROCESS_IMAGE_OUTPUTS_OB35, "5"
  PART_PROCESS_IMAGE_OUTPUTS_OB36, "6"
  PART_PROCESS_IMAGE_OUTPUTS_OB37, "7"
  PART_PROCESS_IMAGE_OUTPUTS_OB38, "8"
  PART_PROCESS_IMAGE_INPUTS_OB40, "0"
  PART_PROCESS_IMAGE_INPUTS_OB41, "0"
  PART_PROCESS_IMAGE_INPUTS_OB42, "0"
  PART_PROCESS_IMAGE_INPUTS_OB43, "0"
  PART_PROCESS_IMAGE_INPUTS_OB44, "0"
  PART_PROCESS_IMAGE_INPUTS_OB45, "0"
  PART_PROCESS_IMAGE_INPUTS_OB46, "0"
  PART_PROCESS_IMAGE_INPUTS_OB47, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB40, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB41, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB42, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB43, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB44, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB45, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB46, "0"
  PART_PROCESS_IMAGE_OUTPUTS_OB47, "0"
  MAXIMUM_NUMBER_OF_ATTEMPTS, "10"
  CYCLIC_INTERRUPT_OB_WITH_SPECIAL_HANDLING, "35"
  WAITING_TIME_BETWEEN_TWO_ATTEMPTS, "60"
  MAXIMUM_SCAN_CYCLE_TIME_EXTENSION, "8000"
  MAXIMUM_COMMUNICATION_DELAY, "3200"
  MAXIMUM_DISABLING_TIME_FOR_PRIORITY_CLASSES, "800"
  MINIMUM_IO_RETENTION_TIME, "90"
END 
        """
        obj_to_compare = RackModule(**{
            'order_num': '6ES7 417-4HT14-0AB0',
            'module_type': 'CPU 417H',
            'position_name': 'VC_ESD_CPU0',
            'slot_num': '3',
            'rack_num': '0',
            'subslot_num': None,
            'firmware_version': 'V4.5'
        })
        self.do_test(str_to_parse, obj_to_compare)

    def test_PS_module(self):
        str_to_parse = """
RACK 0, SLOT 1, "6ES7 405-0KR02-0AA0", "PS 405 10A"
BEGIN 
  ASSET_ID "CCC075F450B24230A212BCEFA346A39B"
  CPU_NO "1"
  ALARM_OB_NO "40"
  OBJECT_REMOVEABLE "1"
  POS_X "0"
  POS_Y "0"
  SIZE_X "0"
  MODULE_ADD_FLAGS "0"
  SIZE_Y "0"
  CAX_APP_ID ""
  OBJECT_COPYABLE "1"
  CREATOR ""
  COMMENT ""
LOCAL_IN_ADDRESSES 
  ADDRESS  16383, 0, 0, 0, 0, 0
END 
        """
        obj_to_compare = RackModule(**{
            'order_num': '6ES7 405-0KR02-0AA0',
            'module_type': 'PS405',
            'position_name': 'PS 405 10A',
            'slot_num': '1',
            'rack_num': '0',
            'subslot_num': None,
            'firmware_version': None
        })
        self.do_test(str_to_parse, obj_to_compare)

    def test_CP_module(self):
        str_to_parse = """
RACK 0, SLOT 5, "6GK7 443-1EX20-0XE0" "V2.0", "PAZ2_CP0"
BEGIN 
  ASSET_ID "979EBABFF95D481FAA489017A25F75C8"
  IP_ACL_IPADDR ""
  LOCAL_DESIGNATION_A ""
  IP_ACL_IPADDR_RANGE ""
  CPU_NO "1"
  IP_ACL_TEXT ""
  SNDRCV_DATALEN_GR240 "0"
  ALARM_OB_NO "40"
  PRAL_NOT_SUPPORTED "0"
  IP_ADDRESS_VALIDATION_ID "0"
  PLANT_DESIGNATION_A ""
  IP_DHCP_CLIENT_ID ""
  H_PROFILE "1"
  MAX_FDL_CON "0"
  MAX_FMS_CON "0"
  SDB_CARRIER "0"
  TIME_SYNC_DIR "3"
  SNDRCV_CONN_PREFIX "0"
  TIME_SYNC_CORRECTION "0"
  WEB_SERVER_ACTIVE "1"
  SNMP_ACTIVE "1"
  DEACTIVATE_UDP_BUFFERING "1"
  OBJECT_REMOVEABLE "1"
  ACTIVATE_FILESYSTEM_CASESENSITIV "0"
  CP_FAST_SEND_RECV "0"
  IRT_DOMAIN_NAME "syncdomain-default"
  POS_X "0"
  TIME_SYNC_PASSING "0"
  IO_ADDRESS_EQUAL "0"
  POS_Y "0"
  SIZE_X "0"
  ETHERNET_KEEP_ALIVE "30"
  MODULE_ADD_FLAGS "0"
  SIZE_Y "0"
  TIMESYNC_NTP_ACTIVE "1"
  KSS_CONNECTION "0"
  PROTECTION_MODE_LEVEL "0"
  TIMESYNC_NTP_SERVER_ADDR "2A 00 00 00 EE 00 02 00 04 C0 A8 01 65 00 00 00 00 00 00 00 00 00 00 00 00 04 C0 A8 01 66 00 00 00 00 00 00 00 00 00 00 00 00"
  TIMESYNC_NTP_TIMEZONE "65536"
  CAX_APP_ID ""
  TIMESYNC_NTP_INTERVAL "60"
  SIMATIC_TAKEOVER "0"
  OBJECT_COPYABLE "1"
  DEVICE_MUST_BE_COUPLED "0"
  CREATOR ""
  COMMENT ""
  TIMESYNC_NTP_ACTIVE_NEW "1"
  IP_ACL_ACTIVE "0"
  IO_TYPE "65"
LOCAL_IN_ADDRESSES 
  ADDRESS  16378, 0, 0, 0, 0, 0
END 
        """
        obj_to_compare = RackModule(**{
            'order_num': '6GK7 443-1EX20-0XE0',
            'module_type': 'CP443-1',
            'position_name': 'PAZ2_CP0',
            'slot_num': '5',
            'rack_num': '0',
            'subslot_num': None,
            'firmware_version': 'V2.0'
        })
        self.do_test(str_to_parse, obj_to_compare)


if __name__ == '__main__':
    unittest.main()
