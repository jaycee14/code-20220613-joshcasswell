from Bmi import BMI

test_bmi_config=[
    {"bmi":18.4,"health":"Malnutrition risk", "category":"Underweight"},
    {"bmi":24.9,"health":"Low risk", "category":"Normal weight"},
    {"bmi":29.9,"health":"Enhanced risk", "category":"Overweight"},
    {"bmi":34.9,"health":"Medium risk", "category":"Moderately obese"},
    {"bmi":39.9,"health":"High risk", "category":"Severely obese"},
    {"bmi":-1,"health":"Very high risk", "category":"Very severely obese"},
    ]

def test_calc_bmi():
    
    bmi = BMI(test_bmi_config)
    result = bmi.calc_bmi(75,175)
    
    assert result == 24.49

    result2 = bmi.calc_bmi(None,None)

    assert result2 ==-1.0

    
def test_score_bmi():
    
    bmi = BMI(test_bmi_config)
    
    result1 = bmi.score_bmi(0)
    assert result1 == ("Malnutrition risk", "Underweight")
    
    result2 = bmi.score_bmi(18)
    assert result2 == ("Malnutrition risk", "Underweight")
    
    result3 = bmi.score_bmi(40)
    assert result3 == ("Very high risk", "Very severely obese")
    
    result4 = bmi.score_bmi(100)
    assert result4 ==  ("Very high risk", "Very severely obese")
    
    result5 = bmi.score_bmi(-1)
    assert result5 == ("Error", "Error")
    
    result6 = bmi.score_bmi(None)
    assert result6 == ("Error", "Error")
    
def test_process_bmi():

    bmi=BMI(test_bmi_config)

    cases = [{"Gender": "Male", "HeightCm": 171, "WeightKg": 96 },
    { "Gender": "Male", "HeightCm": 161, "WeightKg": 85 }]

    result =bmi.process_json(cases)
    assert len(result)==2
    assert set(result[0].keys()) == {"Gender", "HeightCm","WeightKg", "BMI", "Risk", "Category"}


def test_mapping():

    try:
        bmi = BMI()
    except ValueError:
        pass