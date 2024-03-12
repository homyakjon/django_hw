from myapp.serializer import RecruiterSerializer

data = {
    'name': 'Yurii',
    'gender': 'male',
    'age': 34,
    'english_level': 'B2'
}

serializer = RecruiterSerializer(data=data)

if serializer.is_valid():
    validated_data, suitable_file = serializer.validated_data
    print("Validation successful:", validated_data)
    with open(suitable_file, 'r') as file:
        print(file.read())
else:
    errors = serializer.errors
    print("Validation errors:", errors)


