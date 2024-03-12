from rest_framework import serializers

GENDER_CHOICES = [
    ('male', 'Мужской'),
    ('female', 'Женский')
]

ENGLISH_LEVEL_CHOICES = [
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('B1', 'B1'),
    ('B2', 'B2'),
    ('C1', 'C1'),
    ('C2', 'C2')
]


class RecruiterSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    age = serializers.IntegerField()
    english_level = serializers.ChoiceField(choices=ENGLISH_LEVEL_CHOICES)

    def validate(self, data):

        if (data['gender'] == 'male' and data['age'] >= 20 and data['english_level'] in ['B2', 'C1', 'C2']) or \
                (data['gender'] == 'female' and data['age'] >= 22 and data['english_level'] in ['B1', 'B2', 'C1',
                                                                                                'C2']):

            return data, 'suitable.html'
        raise serializers.ValidationError("You do not meet the requirements for the position.")
