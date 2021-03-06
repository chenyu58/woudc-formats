# -*- coding: utf-8 -*-
# =================================================================
#
# Terms and Conditions of Use
#
# Unless otherwise noted, computer program source code of this
# distribution is covered under Crown Copyright, Government of
# Canada, and is distributed under the MIT License.
#
# The Canada wordmark and related graphics associated with this
# distribution are protected under trademark law and copyright law.
# No permission is granted to use them outside the parameters of
# the Government of Canada's corporate identity program. For
# more information, see # http://www.tbs-sct.gc.ca/fip-pcim/index-eng.asp
#
# Copyright title to all 3rd party software distributed with this
# software is held by the respective copyright holders as noted in
# those files. Users are asked to read the 3rd Party Licenses
# referenced with those assets.
#
# Copyright (c) 2017 Government of Canada
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the 'Software'), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.
#
# =================================================================

import unittest
from woudc_formats import load
from woudc_formats.util import setup_logger
import logging


class Test(unittest.TestCase):
    """Test suite for Writer"""

    def setUp(self):
        """setup test fixtures, etc."""
        logfile = 'log.log'
        loglevel = 'ERROR'
        setup_logger(logfile, loglevel)
        LOGGER = logging.getLogger(__name__)  # noqa

    def tearDown(self):
        """return to pristine state"""

        pass

    def test_dump_file(self):
        """notification test"""

    def test_shadoz(self):
        """
        Tests for SHADOZ
        """
        shadoz_filename = "tests/reunion_20141210_V05.dat"
        s = load('SHADOZ', shadoz_filename)

        self.assertTrue("CONTENT$1" in s.extcsv_ds.keys())
        self.assertTrue("DATA_GENERATION$1" in s.extcsv_ds.keys())
        self.assertTrue("PLATFORM$1" in s.extcsv_ds.keys())
        self.assertTrue("INSTRUMENT$1" in s.extcsv_ds.keys())
        self.assertTrue("LOCATION$1" in s.extcsv_ds.keys())
        self.assertTrue("TIMESTAMP$1" in s.extcsv_ds.keys())
        self.assertTrue("FLIGHT_SUMMARY$1" in s.extcsv_ds.keys())
        self.assertTrue("AIXILLARY_DATA$1" in s.extcsv_ds.keys())
        self.assertTrue("PROFILE$1" in s.extcsv_ds.keys())
        self.assertTrue("Class" in s.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Category" in s.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Level" in s.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Form" in s.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Date" in s.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Agency" in s.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Version" in s.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("ScientificAuthority" in
                        s.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Type" in s.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("ID" in s.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Name" in s.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Country" in s.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("GAW_ID" in s.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Name" in s.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Model" in s.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Number" in s.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Latitude" in s.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("Longitude" in s.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("Height" in s.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("UTCOffset" in s.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Date" in s.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Time" in s.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("IntegratedO3" in
                        s.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("CorrectionCode" in
                        s.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("SondeTotalO3" in
                        s.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("CorrectionFactor" in
                        s.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("TotalO3" in s.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("WLCode" in s.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("ObsType" in s.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("Instrument" in s.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("Number" in s.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("MeteoSonde" in s.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("ib1" in s.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("ib2" in s.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("PumpRate" in s.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("BackgroundCorr" in
                        s.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("SampleTemperatureType" in
                        s.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("MinutesGroundO3" in
                        s.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("Pressure" in s.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("O3PartialPressure" in s.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("Temperature" in s.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("WindSpeed" in s.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("WindDirection" in s.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("LevelCode" in s.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("Duration" in s.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("GPHeight" in s.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("RelativeHumidity" in s.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("SampleTemperature" in s.extcsv_ds["PROFILE$1"].keys())

        self.assertEqual(s.extcsv_ds["PROFILE$1"]["Pressure"][0], "1014.200")
        self.assertEqual(s.extcsv_ds["PROFILE$1"]["Pressure"][1], "1012.300")
        self.assertEqual(s.extcsv_ds["PROFILE$1"]["Pressure"][10], "1006.300")
        self.assertEqual(s.extcsv_ds["PROFILE$1"]["O3PartialPressure"][10],
                         "2.082")
        self.assertEqual(s.extcsv_ds["PLATFORM$1"]["Type"], ["STN"])
        self.assertEqual(s.extcsv_ds["PLATFORM$1"]["Country"],
                         ["REU"])
        self.assertEqual(s.extcsv_ds["DATA_GENERATION$1"]["Agency"],
                         ["U_LaReunion"])

    def test_bas(self):
        """
        BAS Tests
        """
        bas_filename = "tests/7_Vernadsky_2013-05-16.txt"
        b = load('BAS', bas_filename)

        self.assertTrue("CONTENT$1" in b.extcsv_ds.keys())
        self.assertTrue("DATA_GENERATION$1" in b.extcsv_ds.keys())
        self.assertTrue("PLATFORM$1" in b.extcsv_ds.keys())
        self.assertTrue("INSTRUMENT$1" in b.extcsv_ds.keys())
        self.assertTrue("LOCATION$1" in b.extcsv_ds.keys())
        self.assertTrue("TIMESTAMP$1" in b.extcsv_ds.keys())
        self.assertTrue("PROFILE$1" in b.extcsv_ds.keys())
        self.assertTrue("Class" in b.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Category" in b.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Level" in b.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Form" in b.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Date" in b.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Agency" in b.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Version" in b.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("ScientificAuthority" in
                        b.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Type" in b.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("ID" in b.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Name" in b.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Country" in b.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("GAW_ID" in b.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Name" in b.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Model" in b.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Number" in b.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Latitude" in b.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("Longitude" in b.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("Height" in b.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("UTCOffset" in b.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Date" in b.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Time" in b.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Date" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("WLCode" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("ObsCode" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("ColumnO3" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("StdDevO3" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("UTC_Begin" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("UTC_End" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("UTC_Mean" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("nOBs" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("mMu" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("ColumnSO2" in b.extcsv_ds["PROFILE$1"].keys())

        self.assertEqual(b.extcsv_ds["PROFILE$1"]["ColumnO3"][0], "264")
        self.assertEqual(b.extcsv_ds["PROFILE$1"]["ColumnO3"][1], "264")
        self.assertEqual(b.extcsv_ds["PROFILE$1"]["ColumnO3"][10], "286")
        self.assertEqual(b.extcsv_ds["PROFILE$1"]["StdDevO3"][10], "4")
        self.assertEqual(b.extcsv_ds["PLATFORM$1"]["Type"], ["STN"])
        self.assertEqual(b.extcsv_ds["PLATFORM$1"]["Country"], ["ATA"])
        self.assertEqual(b.extcsv_ds["DATA_GENERATION$1"]["Agency"], ["BAS"])

    def test_AMES(self):
        """
        Tests for AMES-2160
        """
        AMES_filename = "tests/le140101.b11"
        AMES_filename2 = 'tests/bu20170609.b18'
        a = load('AMES-2160', AMES_filename, "Lerwick", "UKMO")
        b = load('AMES-2160', AMES_filename2, "Boulder ESRL HQ (CO)",
                 "NOAA-CMDL")

        self.assertTrue("CONTENT$1" in a.extcsv_ds.keys())
        self.assertTrue("DATA_GENERATION$1" in a.extcsv_ds.keys())
        self.assertTrue("PLATFORM$1" in a.extcsv_ds.keys())
        self.assertTrue("INSTRUMENT$1" in a.extcsv_ds.keys())
        self.assertTrue("LOCATION$1" in a.extcsv_ds.keys())
        self.assertTrue("TIMESTAMP$1" in a.extcsv_ds.keys())
        self.assertTrue("FLIGHT_SUMMARY$1" in a.extcsv_ds.keys())
        self.assertTrue("AIXILLARY_DATA$1" in a.extcsv_ds.keys())
        self.assertTrue("PROFILE$1" in a.extcsv_ds.keys())
        self.assertTrue("Class" in a.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Category" in a.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Level" in a.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Form" in a.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Date" in a.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Agency" in a.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Version" in a.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("ScientificAuthority" in
                        a.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Type" in a.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("ID" in a.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Name" in a.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Country" in a.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("GAW_ID" in a.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Name" in a.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Model" in a.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Number" in a.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Latitude" in a.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("Longitude" in a.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("Height" in a.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("UTCOffset" in a.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Date" in a.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Time" in a.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("IntegratedO3" in
                        a.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("CorrectionCode" in
                        a.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("SondeTotalO3" in
                        a.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("CorrectionFactor" in
                        a.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("TotalO3" in a.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("WLCode" in a.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("ObsType" in a.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("Instrument" in a.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("Number" in a.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("MeteoSonde" in a.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("ib1" in a.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("ib2" in a.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("PumpRate" in a.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("BackgroundCorr" in
                        a.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("SampleTemperatureType" in
                        a.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("MinutesGroundO3" in
                        a.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("Pressure" in a.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("O3PartialPressure" in a.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("Temperature" in a.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("WindSpeed" in a.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("WindDirection" in a.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("LevelCode" in a.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("Duration" in a.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("GPHeight" in a.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("RelativeHumidity" in a.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("SampleTemperature" in a.extcsv_ds["PROFILE$1"].keys())

        self.assertEqual(a.extcsv_ds["PROFILE$1"]["Pressure"][0],
                         "980.2")
        self.assertEqual(a.extcsv_ds["PROFILE$1"]["Pressure"][1],
                         "979.1")
        self.assertEqual(a.extcsv_ds["PROFILE$1"]["Pressure"][10],
                         "969.4")
        self.assertEqual(a.extcsv_ds["PROFILE$1"]["O3PartialPressure"][10],
                         "3.31")
        self.assertEqual(a.extcsv_ds["PLATFORM$1"]["Type"], ["STN"])
        self.assertEqual(a.extcsv_ds["PLATFORM$1"]["Country"],
                         ["GBR"])
        self.assertEqual(a.extcsv_ds["DATA_GENERATION$1"]["Agency"],
                         ["UKMO"])

        self.assertTrue("CONTENT$1" in b.extcsv_ds.keys())
        self.assertTrue("DATA_GENERATION$1" in b.extcsv_ds.keys())
        self.assertTrue("PLATFORM$1" in b.extcsv_ds.keys())
        self.assertTrue("INSTRUMENT$1" in b.extcsv_ds.keys())
        self.assertTrue("LOCATION$1" in b.extcsv_ds.keys())
        self.assertTrue("TIMESTAMP$1" in b.extcsv_ds.keys())
        self.assertTrue("FLIGHT_SUMMARY$1" in b.extcsv_ds.keys())
        self.assertTrue("AIXILLARY_DATA$1" in b.extcsv_ds.keys())
        self.assertTrue("PROFILE$1" in b.extcsv_ds.keys())
        self.assertTrue("Class" in b.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Category" in b.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Level" in b.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Form" in b.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Date" in b.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Agency" in b.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Version" in b.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("ScientificAuthority" in
                        b.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Type" in b.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("ID" in b.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Name" in b.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Country" in b.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("GAW_ID" in b.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Name" in b.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Model" in b.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Number" in b.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Latitude" in b.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("Longitude" in b.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("Height" in b.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("UTCOffset" in b.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Date" in b.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Time" in b.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("IntegratedO3" in
                        b.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("CorrectionCode" in
                        b.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("SondeTotalO3" in
                        b.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("CorrectionFactor" in
                        b.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("TotalO3" in b.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("WLCode" in b.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("ObsType" in b.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("Instrument" in b.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("Number" in b.extcsv_ds["FLIGHT_SUMMARY$1"].keys())
        self.assertTrue("MeteoSonde" in b.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("ib1" in b.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("ib2" in b.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("PumpRate" in b.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("BackgroundCorr" in
                        b.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("SampleTemperatureType" in
                        b.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("MinutesGroundO3" in
                        b.extcsv_ds["AIXILLARY_DATA$1"].keys())
        self.assertTrue("Pressure" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("O3PartialPressure" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("Temperature" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("WindSpeed" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("WindDirection" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("LevelCode" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("Duration" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("GPHeight" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("RelativeHumidity" in b.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("SampleTemperature" in b.extcsv_ds["PROFILE$1"].keys())

        self.assertEqual(b.extcsv_ds["PROFILE$1"]["Pressure"][0],
                         "820.26")
        self.assertEqual(b.extcsv_ds["PROFILE$1"]["Pressure"][1],
                         "820.05")
        self.assertEqual(b.extcsv_ds["PROFILE$1"]["Pressure"][10],
                         "816.04")
        self.assertEqual(b.extcsv_ds["PROFILE$1"]["O3PartialPressure"][10],
                         "4.8607")
        self.assertEqual(b.extcsv_ds["PLATFORM$1"]["Type"], ["STN"])
        self.assertEqual(b.extcsv_ds["PLATFORM$1"]["Country"],
                         ["USA"])
        self.assertEqual(b.extcsv_ds["DATA_GENERATION$1"]["Agency"],
                         ["NOAA-CMDL"])

    def test_vaisala(self):
        """
        Vaisala Tests
        """
        Vaisala_filename = "tests/Ozono000121_14SEG_SKBO.txt"
        Vai = load('Vaisala', Vaisala_filename, "Vaisala", "Vaisala_Agency", {"ID": "666", "SA": "Vaisala_SA", "country": "Vaisala_Country"})  # noqa

        self.assertTrue("CONTENT$1" in Vai.extcsv_ds.keys())
        self.assertTrue("DATA_GENERATION$1" in Vai.extcsv_ds.keys())
        self.assertTrue("PLATFORM$1" in Vai.extcsv_ds.keys())
        self.assertTrue("INSTRUMENT$1" in Vai.extcsv_ds.keys())
        self.assertTrue("LOCATION$1" in Vai.extcsv_ds.keys())
        self.assertTrue("TIMESTAMP$1" in Vai.extcsv_ds.keys())
        self.assertTrue("PROFILE$1" in Vai.extcsv_ds.keys())
        self.assertTrue("Class" in Vai.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Category" in Vai.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Level" in Vai.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Form" in Vai.extcsv_ds["CONTENT$1"].keys())
        self.assertTrue("Date" in Vai.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Agency" in Vai.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Version" in Vai.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("ScientificAuthority" in
                        Vai.extcsv_ds["DATA_GENERATION$1"].keys())
        self.assertTrue("Type" in Vai.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("ID" in Vai.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Name" in Vai.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Country" in Vai.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("GAW_ID" in Vai.extcsv_ds["PLATFORM$1"].keys())
        self.assertTrue("Name" in Vai.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Model" in Vai.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Number" in Vai.extcsv_ds["INSTRUMENT$1"].keys())
        self.assertTrue("Latitude" in Vai.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("Longitude" in Vai.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("Height" in Vai.extcsv_ds["LOCATION$1"].keys())
        self.assertTrue("UTCOffset" in Vai.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Date" in Vai.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Time" in Vai.extcsv_ds["TIMESTAMP$1"].keys())
        self.assertTrue("Pressure" in Vai.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("O3PartialPressure" in Vai.extcsv_ds["PROFILE$1"].keys())  # noqa
        self.assertTrue("Temperature" in Vai.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("WindSpeed" in Vai.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("WindDirection" in Vai.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("LevelCode" in Vai.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("Duration" in Vai.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("GPHeight" in Vai.extcsv_ds["PROFILE$1"].keys())
        self.assertTrue("RelativeHumidity" in Vai.extcsv_ds["PROFILE$1"].keys())  # noqa
        self.assertTrue("SampleTemperature" in Vai.extcsv_ds["PROFILE$1"].keys())  # noqa

        self.assertEqual(Vai.extcsv_ds["PROFILE$1"]["Pressure"][0], "753.2")
        self.assertEqual(Vai.extcsv_ds["PROFILE$1"]["Pressure"][1], "747.3")
        self.assertEqual(Vai.extcsv_ds["PROFILE$1"]["Pressure"][10], "692.1")
        self.assertEqual(Vai.extcsv_ds["PROFILE$1"]["O3PartialPressure"][10], "2.12")  # noqa
        self.assertEqual(Vai.extcsv_ds["PLATFORM$1"]["Type"], ["STN"])
        self.assertEqual(Vai.extcsv_ds["PLATFORM$1"]["Country"], ["Vaisala_Country"])  # noqa
        self.assertEqual(Vai.extcsv_ds["DATA_GENERATION$1"]["Agency"], ["Vaisala_Agency"])  # noqa


# main
if __name__ == '__main__':
    unittest.main()
