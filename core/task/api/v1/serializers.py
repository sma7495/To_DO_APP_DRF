from rest_framework import serializers

from ...models import Task, SubProject, Project


class TaskSerializer(serializers.ModelSerializer):
    snipet_description = serializers.ReadOnlyField(source="get_snipet_description")
    absolute_url = serializers.SerializerMethodField(method_name="get_absolute_url")

    class Meta:
        model = Task
        fields = [
            "title",
            "sub_project",
            "description",
            "snipet_description",
            "dead_time",
            "start_time",
            "spending_time",
            "status",
            "priority",
            "related_user",
            "manager",
            "absolute_url",
        ]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get("request")
        rep["sub_project"] = SubProjectSerializer(
            instance=instance.sub_project,
            many=False,
            context={"request": request},
        ).data.get("title")
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snipet_description")
            rep.pop("absolute_url")
        else:
            rep.pop("description")
        return rep

    def validate(self, attrs):
        if attrs.get("start_time") >= attrs.get("dead_time"):
            raise serializers.ValidationError(
                {"dead_time": "dead time must be greater than start time"}
            )
        return super().validate(attrs)


class SubProjectSerializer(serializers.ModelSerializer):
    snipet_description = serializers.ReadOnlyField(source="get_snipet_description")
    absolute_url = serializers.SerializerMethodField(method_name="get_absolute_url")

    class Meta:
        model = SubProject
        fields = [
            "title",
            "project",
            "description",
            "snipet_description",
            "dead_time",
            "start_time",
            "spending_time",
            "status",
            "priority",
            "related_user",
            "manager",
            "absolute_url",
        ]
        read_only_fields = [
            "status",
            "spending_time",
        ]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get("request")
        rep["project"] = ProjectSerializer(
            instance=instance.project,
            many=False,
            context={"request": request},
        ).data.get("title")
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snipet_description")
            rep.pop("absolute_url")
        else:
            rep.pop("description")
        return rep

    def validate(self, attrs):
        if attrs.get("start_time") >= attrs.get("dead_time"):
            raise serializers.ValidationError(
                {"dead_time": "dead time must be greater than start time"}
            )
        return super().validate(attrs)


class ProjectSerializer(serializers.ModelSerializer):
    snipet_description = serializers.ReadOnlyField(source="get_snipet_description")
    absolute_url = serializers.SerializerMethodField(method_name="get_absolute_url")

    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "snipet_description",
            "dead_time",
            "start_time",
            "spending_time",
            "status",
            "priority",
            "related_user",
            "manager",
            "absolute_url",
        ]
        read_only_fields = [
            "status",
            "spending_time",
        ]

    def get_absolute_url(self, obj):
        request = self.context.get("request")
        return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        request = self.context.get("request")
        if request.parser_context.get("kwargs").get("pk"):
            rep.pop("snipet_description")
            rep.pop("absolute_url")
        else:
            rep.pop("description")
        return rep

    def validate(self, attrs):
        if attrs.get("start_time") >= attrs.get("dead_time"):
            raise serializers.ValidationError(
                {"dead_time": "dead time must be greater than start time"}
            )
        return super().validate(attrs)
