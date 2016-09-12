#!/usr/bin/env python
from jenkins_jobs.builder import Builder
from jenkins_jobs.config import JJBConfig
from jenkins_jobs.xml_config import XmlJobGenerator
from jenkins_jobs.parser import YamlParser
from jenkins_jobs.registry import ModuleRegistry
import xml.etree.ElementTree as ET
import os


BASE_PATH = os.path.dirname(os.path.realpath(__file__))


def assert_case(case_name):
    case_source, case_result = (os.path.join(BASE_PATH, case_name + ext) for ext in ['.yml', '.xml'])
    jjb_config = JJBConfig()
    builder = Builder(jjb_config)

    # Generate XML
    parser = YamlParser(jjb_config)
    registry = ModuleRegistry(jjb_config, builder.plugins_list)
    xml_generator = XmlJobGenerator(registry)

    parser.load_files(case_source)
    registry.set_parser_data(parser.data)

    job_data_list = parser.expandYaml(registry, [])

    xml_jobs = xml_generator.generateXML(job_data_list)

    result_xml = ET.XML(xml_jobs[0].output())
    expected_xml = ET.XML(open(case_result).read())
    assert ET.tostring(result_xml) == ET.tostring(expected_xml)
