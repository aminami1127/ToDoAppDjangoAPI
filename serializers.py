from rest_framework import serializers
from todo.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
        pk = serializers.IntegerField(read_only=True)
        name = serializers.CharField(max_length=200)
        date = serializers.DateTimeField()
        completed = serializers.BooleanField(default=False)
    """
    class Meta:
        model = Task
        fields = ('id', 'name', 'date', 'completed')

    def create(self, validated_data):
        return Task.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date = validated_data.get('date', instance.date)
        instance.completed = \
            validated_data.get('completed', instance.completed)
        instance.save()
        return instance
