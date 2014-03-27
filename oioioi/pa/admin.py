from oioioi.base import admin
from oioioi.participants.admin import ParticipantAdmin
from oioioi.pa.models import PARegistration
from oioioi.pa.forms import PARegistrationForm


class PARegistrationInline(admin.StackedInline):
    model = PARegistration
    fk_name = 'participant'
    form = PARegistrationForm
    can_delete = False
    inline_classes = ('collapse open',)


class PARegistrationParticipantAdmin(ParticipantAdmin):
    list_display = ParticipantAdmin.list_display
    inlines = ParticipantAdmin.inlines + [PARegistrationInline]
    readonly_fields = ['user']

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

    def get_actions(self, request):
        actions = super(PARegistrationParticipantAdmin, self) \
                .get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
