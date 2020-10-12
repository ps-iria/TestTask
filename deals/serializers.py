from django.db.models import Sum, Q
from rest_framework import serializers

from deals.models import DealFile, Deals


class DealFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DealFile
        fields = ('deal',)


class GemSerializer(serializers.ModelSerializer):
    item = serializers.DictField(source='GetGem')

    class Meta:
        model = Deals
        fields = ['item']


class DealVeiwSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='get_username')
    spent_money = serializers.SerializerMethodField('total_spend')
    gems = serializers.SerializerMethodField('get_gems')

    def total_spend(self, object):
        spend = 0
        queryset = Deals.objects.values('total').filter(
            username=object.username).all()
        for item in queryset:
            spend += item['total']
        return spend

    def get_gems(self, object):
        dict_name = []
        query_names = Deals.objects.values('username')
        query_names = query_names.annotate(spend_money=Sum('total'))
        query_names = query_names.order_by('-spend_money')
        query_names = query_names.all()[:5]
        queryset = query_names
        for i in queryset:
            dict_name.append(i['username'])

        query_gems_top = Deals.objects.values('username').distinct()
        query_gems_top = query_gems_top.values('item')
        q = Q()
        for i in range(len(dict_name)):
            if dict_name[i] == object.username:
                if i == 0:
                    q = (Q(username=dict_name[1]) |
                         Q(username=dict_name[2]) |
                         Q(username=dict_name[3]) |
                         Q(username=dict_name[4]))
                if i == 1:
                    q = (Q(username=dict_name[0]) |
                         Q(username=dict_name[2]) |
                         Q(username=dict_name[3]) |
                         Q(username=dict_name[4]))
                if i == 2:
                    q = (Q(username=dict_name[0]) |
                         Q(username=dict_name[1]) |
                         Q(username=dict_name[3]) |
                         Q(username=dict_name[4]))
                if i == 3:
                    q = (Q(username=dict_name[0]) |
                         Q(username=dict_name[1]) |
                         Q(username=dict_name[2]) |
                         Q(username=dict_name[4]))
                if i == 4:
                    q = (Q(username=dict_name[0]) |
                         Q(username=dict_name[1]) |
                         Q(username=dict_name[2]) |
                         Q(username=dict_name[3]))
        query_gems_top = query_gems_top.filter(q)
        query_gems_top = query_gems_top.all()

        dict_gems_another = []
        for item in query_gems_top:
            dict_gems_another.append(item['item'])

        query_gems_1 = Deals.objects.values('username').distinct()
        query_gems_1 = query_gems_1.values('item')
        query_gems_1 = query_gems_1.filter(Q(username=object.username))
        query_gems_1 = query_gems_1.all()

        dict_gems_this = []
        for item in query_gems_1:
            dict_gems_this.append(item['item'])
        foo = []
        for item in dict_gems_this:
            if item in dict_gems_another:
                foo.append(item)
        return foo

    class Meta:
        model = Deals
        fields = ['username', 'spent_money', 'gems']
