from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from investments.models import Investor, Investment, Asset
from investments.serializers import InvestorListingSerializer, InvestmentListingSerializer, AssetSerializer, \
    InvestorRetrieveSerializer


class GetSerializerClassMixin(object):
    serializer_action_classes = dict()

    def get_serializer_class(self):
        """
        A class which inherits this mixins should have variable
        `serializer_action_classes`.
        Look for serializer class in self.serializer_action_classes, which
        should be a dict mapping action name (key) to serializer class (value),
        i.e.:
        class SampleViewSet(viewsets.ViewSet):
            serializer_class = DocumentSerializer
            serializer_action_classes = {
               'upload': UploadDocumentSerializer,
               'download': DownloadDocumentSerializer,
            }
            @action
            def upload:
                ...
        If there's no entry for that action then just fallback to the regular
        get_serializer_class lookup: self.serializer_class, DefaultSerializer.
        """
        try:
            return self.serializer_action_classes[self.action]
        except (KeyError, AttributeError):
            return super().get_serializer_class()


class InvestorViewSet(GetSerializerClassMixin, viewsets.ModelViewSet):
    queryset = Investor.objects.all()
    serializer_class = InvestorListingSerializer
    serializer_action_classes = {
        'list': InvestorListingSerializer,
        'retrieve': InvestorRetrieveSerializer,
    }


class InvestmentViewSet(viewsets.ModelViewSet):
    queryset = Investment.objects.select_related("investor").all()
    serializer_class = InvestmentListingSerializer


class AssetViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer
