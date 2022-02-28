from .models import Issue

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import IssueSerializerWithTitles, ProfileSerializer, IssueSerializer, ProjectSerializer, IssueSeveritySerializer, IssueStatusSerializer, IssueTypeSerializer, AssigneesSerializer
from .models import Profile, Project, Issue, IssueSeverity, IssueType, IssueStatus, Assignees


class ProfileList(APIView):
    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializer = ProjectSerializer(profile, many=True)
        return Response(serializer.data)


class ProjectList(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):

        project_data = request.data
        new_project = Project.objects.create(
            title=project_data['title'],
        )
        new_project.save()
        serializer = ProjectSerializer(new_project)
        return Response(serializer.data)


class IssueList(APIView):
    # api/v1/my-issues/?projectid=
    def get(self, request, format=None):
        projectid = request.GET.get("projectid")
        if projectid:
            issue = Issue.objects.filter(projectid=projectid)
        else:
            issue = Issue.objects.all()

        serializer = IssueSerializer(issue, many=True)
        return Response(serializer.data)

    def post(self, request):

        issue_data = request.data
        new_issue = Issue.objects.create(


            title=issue_data['title'],
            description=issue_data['description'],
            time_estimate=issue_data['time_estimate'],
            userid=Profile.objects.get(id=issue_data['userid']),
            projectid=Project.objects.get(id=issue_data['projectid']),
            issueTypeId=IssueType.objects.get(id=issue_data['issueTypeId']),
            issueStatusId=IssueStatus.objects.get(
                id=issue_data['issueStatusId']),
            issueSeverityId=IssueSeverity.objects.get(
                id=issue_data['issueSeverityId']),
        )
        serializer = IssueSerializer(new_issue)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    def put(self, request, format=None):
        updatedIssue = request.data
        oldIssue = Issue.objects.filter(id=updatedIssue.id)
        serializer = IssueSerializer(oldIssue, data=updatedIssue)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        issueid = request.GET.get("id")
        issue = Issue.objects.filter(id=issueid)
        issue.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SeverityList(APIView):
    def get(self, request, format=None):
        id = request.GET.get("id")
        if id:
            severity = IssueSeverity.objects.filter(id=id)
        else:
            severity = IssueSeverity.objects.all()
        serializer = IssueSeveritySerializer(severity, many=True)
        return Response(serializer.data)


class StatusList(APIView):
    def get(self, request, format=None):
        id = request.GET.get("id")
        if id:
            status = IssueStatus.objects.filter(id=id)
        else:
            status = IssueStatus.objects.all()

        serializer = IssueStatusSerializer(status, many=True)
        return Response(serializer.data)


class TypeList(APIView):
    def get(self, request, format=None):
        id = request.GET.get("id")
        if id:
            issueType = IssueType.objects.filter(id=id)
        else:
            issueType = IssueType.objects.all()
        serializer = IssueTypeSerializer(issueType, many=True)
        return Response(serializer.data)


class AssigneesList(APIView):
    def get(self, request, format=None):
        userId = request.GET.get("userId")
        if userId:
            assignee = Assignees.objects.filter(userId=userId)
        else:
            assignee = Assignees.objects.all()

        serializer = AssigneesSerializer(assignee, many=True)
        return Response(serializer.data)


class IssueListWithTitles(APIView):
    # api/v1/my-issues/?projectid=
    def get(self, request, format=None):
        projectid = request.GET.get("projectid")
        if projectid:
            issues = Issue.objects.filter(projectid=projectid)
        else:
            issues = Issue.objects.all()
        issuesWithTitles = []
        for i in issues:
            issue = {
                "id": i.id,
                "created": i.created,
                "title": i.title,
                "description": i.description,
                "time_estimate": i.time_estimate,
                "user": "",
                "project": i.projectid,
                "issueType": i.issueTypeId,
                "issueStatus": i.issueStatusId,
                "issueSeverity": i.issueSeverityId
            }
            issuesWithTitles.append(issue)
        serializer = IssueSerializerWithTitles(issuesWithTitles, many=True)
        return Response(serializer.data)
