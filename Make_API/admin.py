from django.contrib import admin
from .models import GetVm, ComposeVM


@admin.register(ComposeVM)
class ComposeAdmin(admin.ModelAdmin):
    list_display = ('vm_name', 'creation_of_vm')
    list_filter = ('vm_name', )
    ordering = ['vm_name']
    search_fields = ('vm_name', )

    def get_queryset(self, request):
        queryset = super(ComposeAdmin, self).get_queryset(request)
        return queryset


# admin.site.register(ComposeVM,ComposeAdmin)
admin.site.register(GetVm)

