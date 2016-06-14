import xml.etree.ElementTree as XML
import jenkins_jobs.modules.base


class Pipeline(jenkins_jobs.modules.base.Base):
    sequence = 0

    def root_xml(self, data):
        xml_parent = XML.Element('flow-definition', {'plugin': 'workflow-job'})
        return xml_parent
