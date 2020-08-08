import sys
import yaml
from datalane.exceptions import YMLParserException


class YML:
    def __init__(self, yml_loc, context_variables):
        self.context_variables = context_variables
        self.raw_yml = self.parse(yml_loc)
        self.wf_name = self.get_wf_name()
        self.wf_order = self.get_wf_order()

    def parse(self, yml_loc):
        with open(yml_loc, 'r') as stream:
            data = yaml.safe_load(stream)
            return data

    @property
    def wf_name(self):
        return self._wf_name

    @wf_name.setter
    def wf_name(self, val):
        self._wf_name = val

    def get_wf_name(self):
        try:
            return self.raw_yml['wf_name']
        except YMLParserException as e:
            print(e)
            sys.exit(1)

    @property
    def wf_order(self):
        return self._wf_order

    @wf_order.setter
    def wf_order(self, val):
        self._wf_order = val

    def get_wf_order(self):
        data = self.raw_yml['wf_order']
        try:
            for item in data:
                if not isinstance(item, str) and not isinstance(item, list):
                    raise YMLParserException("wf_order needs to be a list or a list of lists"
                                             "e.g:['task1', 'task2', ['task3', 'task4'], 'task5']")
        except YMLParserException as e:
            print(e)
            sys.exit(1)
        else:
            return [[task] if isinstance(task, str) else task for task in data]
