class ParentIDMixin:
    parent_field = ''
    model = None

    def get_queryset(self, *args, **kwargs):
        queryset = self.model.objects.filter(**self._get_filter_key())
        return queryset

    def _get_filter_key(self):
        parent_id = self.kwargs.get(self.parent_field)
        return {self.parent_field: parent_id}
