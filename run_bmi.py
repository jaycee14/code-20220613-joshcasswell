from Bmi import BMI
from bmi_tests import test_calc_bmi
from bmi_tests import test_mapping
from bmi_tests import test_process_bmi
from bmi_tests import test_score_bmi


test_cases =[{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
{ "Gender": "Male", "HeightCm": 161, "WeightKg": 85 },
{ "Gender": "Male", "HeightCm": 180, "WeightKg": 77 },
{ "Gender": "Female", "HeightCm": 166, "WeightKg": 62},
{"Gender": "Female", "HeightCm": 150, "WeightKg": 70},
{"Gender": "Female", "HeightCm": 167, "WeightKg": 82}]

def run_tests():

    test_calc_bmi()
    test_score_bmi()
    test_process_bmi()
    test_mapping()

    print("All tests passed")

if __name__ == "__main__":
    
    run_tests()

    bmi= BMI(fname='config_bmi_english.json')

    results =bmi.process_json(test_cases)

    overweight_count=0
    for res in results:
        if res["Category"]=="Overweight":
            overweight_count+=1

    print(f"Number of overweight cases: {overweight_count}")
    
    
