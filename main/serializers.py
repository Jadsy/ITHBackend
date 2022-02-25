from dataclasses import fields
from rest_framework import serializers

from .models import Profile, Project, Issue, IssueStatus, IssueSeverity, IssueComment, IssueType, Attachment, Assignees, UserRole, IssueWithTitles


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            "id",
            "user",
            "bio",
            "profile_pic",
            "social_github",
            "social_twitter",
            "social_linkedin",
            "created"
        )


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = (
            "id",
            "title",
            "repo_link",
            "created",
        )


class IssueStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueStatus
        fields = (
            "id",
            "title",
        )


class IssueSeveritySerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueSeverity
        fields = (
            "id",
            "title",
        )


class IssueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueType
        fields = (
            "id",
            "title",
        )


class IssueSerializerWithTitles(serializers.ModelSerializer):
    class Meta:
        model = IssueWithTitles
        fields = (
            "id",
            "created",
            "title",
            "description",
            "time_estimate",
            "user",
            "project",
            "issueType",
            "issueStatus",
            "issueSeverity",
        )


class IssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Issue
        fields = (
            "id",
            "created",
            "title",
            "description",
            "time_estimate",
            "userid",
            "projectid",
            "issueTypeId",
            "issueStatusId",
            "issueSeverityId",
        )


class UserRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRole
        fields = (
            "id",
            "title",
        )


class AssigneesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignees
        fields = (
            "userRoleId",
            "created",
        )


class IssueCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueComment
        fields = (
            "id",
            "created",
            "userId",
            "issueId",
            "comment",
        )


class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        fields = (
            "id",
            "created",
            "issueId",
            "title",
        )