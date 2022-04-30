from django.db import models

from django.db import models
from django.contrib.auth.models import User
import uuid
from djangoHexadecimal.fields import HexadecimalField


class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(null=True, blank=True, max_length=255)
    profile_pic = models.ImageField(
        null=True, blank=True, default="default.png",
        # upload_to=''
    )
    social_github = models.CharField(max_length=50, null=True, blank=True)
    social_twitter = models.CharField(max_length=50, null=True, blank=True)
    social_linkedin = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(
        max_length=255, null=True, blank=True, unique=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    repo_link = models.CharField(max_length=255, null=True, blank=True)
    members = models.ManyToManyField(
        Profile,  related_name="members", blank=True)
    admin = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="project_admin", null=True, blank=True)

    def __str__(self):
        return self.title


class IssueStatus(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class IssueSeverity(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class IssueType(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    needSeverity = models.BooleanField(default=True)
    projectid = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True)
    color = models.CharField(max_length=100, null=True, blank=True)

    # def __str__(self):
    #     return self.title


class Issue(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True, max_length=1024, )

    userid = models.ForeignKey(Profile, on_delete=models.CASCADE)
    projectid = models.ForeignKey(
        Project, on_delete=models.CASCADE, null=True, blank=True)
    issueTypeId = models.ForeignKey(
        IssueType, on_delete=models.CASCADE, null=True, blank=True)
    issueStatusId = models.ForeignKey(IssueStatus, on_delete=models.CASCADE, )
    issueSeverityId = models.ForeignKey(
        IssueSeverity, on_delete=models.CASCADE, null=True, blank=True)
    isComplete = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class UserRole(models.Model):

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Assignees(models.Model):
    issueId = models.ForeignKey(
        Issue, on_delete=models.CASCADE, null=True, blank=True)
    userId = models.ForeignKey(
        Profile, on_delete=models.CASCADE, null=True, blank=True)
    userRoleId = models.ForeignKey(
        UserRole, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (("issueId", "userId"), )

    def __str__(self):
        return 'Assignee'


class IssueComment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    userId = models.ForeignKey(Profile, on_delete=models.CASCADE)
    issueId = models.ForeignKey(Issue, on_delete=models.CASCADE)
    comment = models.TextField(max_length=2048)


class Attachment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    issueId = models.ForeignKey(Issue, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    URI = models.CharField(
        max_length=255,
        null=True,
        blank=True
    )


class IssueWithTitles(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    time_estimate = models.FloatField(null=True, blank=True)
    user = models.JSONField()
    project = models.JSONField()
    issueType = models.JSONField()
    issueStatus = models.JSONField()
    issueSeverity = models.JSONField()
    isComplete = models.BooleanField(default=True)

    def __str__(self):
        return self.title
