from rest_framework import serializers
from excel_api.models import ExcelDocument


class ExcelDocumentSerializer(serializers.HyperlinkedModelSerializer):
    file_url = serializers.FileField(source="file")
    file_name = serializers.SerializerMethodField()
    summary = serializers.HyperlinkedIdentityField(
        view_name="exceldocument-summary",
    )

    def get_file_name(self, obj):
        return obj.file.name.split("/")[-1]

    class Meta:
        model = ExcelDocument
        fields = ["url", "file_name", "summary", "file_url"]


class ExcelSummarySerializer(serializers.Serializer):
    columns = serializers.ListField(child=serializers.CharField())
