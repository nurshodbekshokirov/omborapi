
from unittest import TestCase
from asosiy.serializers import *

class TESTMahsulotSerializer(TestCase):
    def test_mahsulot(self):
        mahsulot = {

                "id": 1,
                "nom": "Pepsi (1.5)",
                "brend": "Pepsi",
                "miqdor": 1,
                "narx": 123,
                "olchov": "dona",
                "kelgan_sana": "2023-03-30T15:04:24.916447Z",
                "ombor": 1

        }
        serializer = MahsulotSerializers(data=mahsulot)

        assert serializer.is_valid() == True
    def test_client(self):
        client = {

                "id": 1,
                "nom": "Pepsilar",
                "manzil": "frunszki",
                "ism": "Javohir",
                "tel": "991283812",
                "qarz": 0,
                "ombor": 1

        }
        serializer = ClientSerializers(data=client)

        assert serializer.is_valid()==True




