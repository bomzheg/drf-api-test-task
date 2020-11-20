
class ParentIDMixin:
    model = None

    def get_queryset(self, *_, **__):
        queryset = self.model.objects.filter(**self.get_filter_key())
        return queryset

    def get_filter_key(self):
        raise NotImplemented
