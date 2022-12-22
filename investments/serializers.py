from rest_framework import serializers

from investments.models import Investor, Investment, Asset


class InvestorListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = ("id", "full_legal_name", )


class InvestmentListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investment
        fields = (
            "id",
            "asset",
            "investor",
            "invested_since",
            "created_at",
            "shares",
            "purchase_price",
            "current_price",
        )


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ("name", "type", )


class InvestmentSerializer(serializers.ModelSerializer):
    asset = AssetSerializer()

    class Meta:
        model = Investment
        fields = (
            "id",
            "asset",
            "invested_since",
            "created_at",
            "shares",
            "purchase_price",
            "current_price",
        )


class InvestorRetrieveSerializer(serializers.ModelSerializer):
    investments = InvestmentSerializer(many=True)

    class Meta:
        model = Investor
        fields = ("id", "full_legal_name", "investments")
