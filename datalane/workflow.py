from datalane.ymlparser import YML


class Workflow:
    def __init__(self, yml_loc, rerun, context_variables):
        self.yml_loc = yml_loc
        self.rerun = rerun
        self.ctx = context_variables
        self.yml_parser = YML(yml_loc,context_variables)
        self.yml_content = self.yml_parser.raw_yml
        self.wf_name = self.yml_parser.wf_name
        self.wf_order = self.yml_parser.wf_order


    def execute(self):
        print('I am in workflow')
        print(self.yml_content, self.rerun, self.ctx)
        print(self.wf_name, self.wf_order)