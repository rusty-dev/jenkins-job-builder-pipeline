import xml.etree.ElementTree as XML
import jenkins_jobs.modules.base
from jenkins_jobs.modules.scm import SCM


class Pipeline(jenkins_jobs.modules.base.Base):
    sequence = 0

    component_type = 'pipeline'
    component_list_type = 'pipeline'

    def gen_xml(self, xml_parent, data):
        definition = data.get(self.component_type, {})

        scm_definition = 'scm' in definition
        definition_type = 'CpsScmFlowDefinition' if scm_definition else 'CpsFlowDefinition'

        xml_definition = XML.SubElement(
            xml_parent,
            'definition',
            {
                'plugin': 'workflow-cps',
                'class': 'org.jenkinsci.plugins.workflow.cps.' + definition_type
            }
        )

        if scm_definition:
            scm_module = next(module for module in self.registry.modules if isinstance(module, SCM))
            scm_module.gen_xml(xml_definition, definition)
            XML.SubElement(xml_definition, 'scriptPath').text = definition.get('script-path', 'Jenkinsfile')
        else:
            XML.SubElement(xml_definition, 'script').text = definition.get('script', '')
            XML.SubElement(xml_definition, 'sandbox').text = str(definition.get('sandbox', False)).lower()
