import string
import math

def calculate_entropy(password):
     pool_size = 0
         if any(c.islower() for c in password):
        pool_size += 26
    if any(c.isupper() for c in password):
        pool_size += 26
    if any(c.isdigit() for c in password):
        pool_size += 10
    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    entropy = len(password) * math.log2(pool_size) if pool_size > 0 else 0
    return entropy

 def check_password_strength(password):  
     length_criteria = len(password) >= 8
     upper_criteria = any(c.isupper() for c in password) 
     lower_criteria = any(c.islower() for c in password)
     digit_criteria = any(c.isdigit() for c in password)
     special_criteria = any(c in string.punctuation for c in password)

     criteria_met = sum([length_criteria, upper_criteria, lower_criteria, digit_criteria, special_criteria])

      entropy = calculate_entropy(password)

      if criteria_met == 5 and entropy >= 60:
        strength = "Very Strong"
      elif criteria_met >= 4 and entropy >= 50:
        strength = "Strong"
      elif criteria_met >= 3 and entropy >= 40:
        strength = "Moderate"
      else:
        strength = "Weak"


