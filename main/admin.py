from django.contrib import admin

from .models import Profile, Project, Issue, IssueStatus, IssueSeverity, IssueComment, IssueType, Attachment, Assignees, UserRole

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(Issue)
admin.site.register(IssueStatus)
admin.site.register(IssueSeverity)
admin.site.register(IssueComment)
admin.site.register(IssueType)
admin.site.register(Attachment)
admin.site.register(Assignees)
admin.site.register(UserRole)
