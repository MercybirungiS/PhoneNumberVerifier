import phonenumbers
from phonenumbers import carrier, geocoder, timezone
mobileNo = input("Enter your  phone number with the Country code: ")
mobileNo = phonenumbers.parse(mobileNo) 
print(timezone.time_zones_for_number(mobileNo)) # getting timezone 
print(carrier.name_for_number(mobileNo, "en")) #Getting carrier of a phone number
print(geocoder.description_for_number(mobileNo, "en")) # Getting region information and location
print(phonenumbers.is_valid_number(mobileNo))# validating a phone number
print(phonenumbers.is_possible_number(mobileNo))# Checking possibility of a number
