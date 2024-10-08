from django.contrib.auth.models import User, Permission, Group
from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.get(pk=4)
        group, created = Group.objects.get_or_create(
            name='profile_manager',
        )
        permission_profile = Permission.objects.get(
            codename='view_profile',
        )
        permission_logentry = Permission.objects.get(
            codename='view_logentry',
        )

        # Add permission in Group
        group.permissions.add(permission_profile)

        # Join user to group
        user.groups.add(group)

        # associate the user directly with the permission
        user.user_permissions.add(permission_logentry)

        group.save()
        user.save()
