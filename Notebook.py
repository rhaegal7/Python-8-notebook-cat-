# -*- coding: utf-8 -*-
import json
import copy
class Notebook:
    def __init__(self, arg):
        if type(arg) == str:
            with open(arg) as notebook:
                if( arg.split('.')[-1] != 'ipynb' ):
                    raise Exception('参数必须是ipynb类型的文件')
            
                notebook_str = notebook.read()
                self.json = json.loads(notebook_str)
        
        if type(arg) == type({}):
            self.json = arg
    
    
    def  __getitem__(self, index):
        return self.json['cells'][index]
    
    def __add__(self, another):
        target_notebook = {}
        target_notebook['cells'] = self.json['cells'] + another.json['cells']
        temp_json = copy.copy(self.json)
        del temp_json['cells']
        target_notebook.update(temp_json)
        
        return Notebook(target_notebook)
    
    def write(self,path):
        target_str = json.dumps(self.json)
        with open(path, 'w') as target:
            target.write(target_str)

