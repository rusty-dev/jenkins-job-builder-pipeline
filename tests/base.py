#!/usr/bin/env python
from jenkins_jobs.builder import Builder
from cStringIO import StringIO
import xml.etree.ElementTree as ET
import os


BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def assert_case(case_name):
    case_source, case_result = (os.path.join(BASE_PATH, case_name + ext) for ext in ['.yml', '.xml'])
    xml_output = StringIO()
    builder = Builder('http://localhost:8080/', '', '', ignore_cache=True)
    builder.update_jobs(case_source, output=xml_output, n_workers=1)
    result_xml = ET.XML(xml_output.getvalue())
    expected_xml = ET.XML(open(case_result).read())
    assert ET.tostring(result_xml) == ET.tostring(expected_xml)
