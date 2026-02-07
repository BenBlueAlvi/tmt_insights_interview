from rest_framework import serializers


class InventoryListAfterDateViewSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField()

    def get_date(self):
        return self.date


class DeactivateOrderViewSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    def get_id(self):
        return self.id


class GetOrdersBetweenEmbargoDatesSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField()
    embargo_date = serializers.DateTimeField()

    def get_start_date(self):
        return self.start_date

    def get_embargo_date(self):
        return self.embargo_date