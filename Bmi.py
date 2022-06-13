import os
import json

class BMI:

    def __init__(self, bmi_mapping:list=None, fname:str=None):
        
        if bmi_mapping is None:
            self.mapping = self.load_mapping(fname)
        else:
            self.mapping = bmi_mapping

    def load_mapping(self,fname:str)->list:
        """Loads a json mapping file."""

        if fname is not None and os.path.exists(fname):
            with open(fname, "rb" ) as f:
                mapping = json.load(f)
            return mapping
        else:
            raise ValueError

    def calc_bmi(self, weight_kg:float, height_cm:float)->float:
        """Given a weight nd height calculates BMI."""

        if weight_kg is None or height_cm is None:
            return -1.0
        
        height_metres = height_cm / 100.0
        
        return round(weight_kg / (height_metres*height_metres),2)
    
    def score_bmi(self,bmi:float)->tuple:
        """Using the given mapping table returns the health risk and category for that BMI."""

        if bmi is None or bmi < 0:
            return "Error","Error"
        
        for entry in self.mapping:
            if bmi <= entry["bmi"]:
                return entry["health"], entry["category"]            

        return entry["health"], entry["category"] 
        
    def process_json(self,input_json:list=None)->list:
        """Given a list of dict objects calculates the BMI, health risk and health category for each
         and returns a new list of dicts with the new information"""

        if input_json is None:
            return None

        for case in input_json:
            bmi =self.calc_bmi(case["WeightKg"],case["HeightCm"])
            risk,category = self.score_bmi(bmi)

            case["BMI"]=bmi
            case["Risk"]=risk
            case["Category"]=category

        return input_json 