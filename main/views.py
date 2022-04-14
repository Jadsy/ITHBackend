from .models import IssueComment, Attachment, Profile, Project, Issue, IssueSeverity, IssueType, IssueStatus, Assignees
from .serializers import IssueCommentSerializer, AttachmentSerializer, IssueSerializerWithTitles, ProfileSerializer, IssueSerializer, ProjectSerializer, IssueSeveritySerializer, IssueStatusSerializer, IssueTypeSerializer, AssigneesSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Issue


class ProfileList(APIView):
    def get(self, request, format=None):
        id = request.GET.get("id")
        if id:
            profile = Profile.objects.filter(user=id)
        else:
            profile = Profile.objects.all()

        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)


class ProjectList(APIView):
    def get(self, request, format=None):
        id = request.GET.get("id")
        if id:
            projects = Project.objects.filter(id=id)
        else:
            projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):

        project_data = request.data
        new_project = Project.objects.create(
            title=project_data['title'],
            repo_link=project_data['repo_link'],
            admin=Profile.objects.get(id=project_data['admin']),
        )
        new_project.save()
        for i in project_data['members']:
            new_project.members.add(i)
        serializer = ProjectSerializer(new_project)
        return Response(serializer.data)

    def delete(self, request, format=None):
        projectid = request.GET.get("id")
        project = Project.objects.filter(id=projectid)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IssueList(APIView):
    # api/v1/my-issues/?projectid=
    def get(self, request, format=None):
        projectid = request.GET.get("projectid")
        id = request.GET.get("id")
        if projectid:
            issue = Issue.objects.filter(projectid=projectid)
        elif id:
            issue = Issue.objects.filter(id=id)
        else:
            issue = Issue.objects.all()

        serializer = IssueSerializer(issue, many=True)
        return Response(serializer.data)

    def post(self, request):

        issue_data = request.data
        existing_id = request.GET.get("id")
        if existing_id:
            # update
            Issue.objects.filter(id=existing_id).update(
                title=issue_data['title'],
                description=issue_data['description'],
                issueSeverityId=issue_data['issueSeverityId'],
                issueStatusId=issue_data['issueStatusId'],
                isComplete=issue_data['isComplete'],

            )

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:

            new_issue = Issue.objects.create(


                title=issue_data['title'],
                description=issue_data['description'],
                userid=Profile.objects.get(id=issue_data['userid']),
                projectid=Project.objects.get(id=issue_data['projectid']),
                issueTypeId=IssueType.objects.get(
                    id=issue_data['issueTypeId']),
                issueStatusId=IssueStatus.objects.get(
                    id=issue_data['issueStatusId']),
                issueSeverityId=IssueSeverity.objects.get(
                    id=issue_data['issueSeverityId']),
                isComplete=issue_data['isComplete'],
            )
            serializer = IssueSerializer(data=new_issue)
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
        projectid = request.GET.get("projectid")
        if id:
            issueType = IssueType.objects.filter(projectid=projectid)
        else:
            issueType = IssueType.objects.all()
        serializer = IssueTypeSerializer(issueType, many=True)
        return Response(serializer.data)

    def post(self, request):

        data = request.data
        existing_id = request.GET.get("id")
        if existing_id:
            # update
            IssueType.objects.filter(id=existing_id).update(
                title=data['title'],
                needSeverity=data['needSeverity'],
                projectid=Project.objects.get(id=data['projectid']),
                color=data['color']

            )

            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            new_type = IssueType.objects.create(
                title=data['title'],
                needSeverity=data['needSeverity'],
                projectid=Project.objects.get(id=data['projectid']),
                color=data['color']
            )
            serializer = IssueTypeSerializer(data=new_type)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

    def delete(self, request, format=None):
        typeid = request.GET.get("id")
        type = IssueComment.objects.filter(id=typeid)
        type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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
        id = request.GET.get("id")
        if projectid:
            issues = Issue.objects.filter(projectid=projectid)
        elif id:
            issues = Issue.objects.filter(id=id)
        else:
            issues = Issue.objects.all()
        issuesWithTitles = []
        for i in issues:
            issue = {
                "id": i.id,
                "created": i.created,
                "title": i.title,
                "description": i.description,
                "user": "",
                "project": i.projectid,
                "issueType": i.issueTypeId,
                "issueStatus": i.issueStatusId,
                "issueSeverity": i.issueSeverityId,
                "isComplete": i.isComplete
            }
            issuesWithTitles.append(issue)
        serializer = IssueSerializerWithTitles(issuesWithTitles, many=True)
        return Response(serializer.data)


class IssueCommentList(APIView):
    def get(self, request, format=None):
        issueId = request.GET.get("issueId")
        if issueId:
            comments = IssueComment.objects.filter(issueId=issueId)
        else:
            comments = IssueComment.objects.all()
        serializer = IssueCommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request):

        data = request.data
        new_comment = IssueComment.objects.create(
            userId=Profile.objects.get(id=data['userId']),
            issueId=Issue.objects.get(id=data['issueId']),
            comment=data['comment']
        )
        new_comment.save()
        serializer = IssueCommentSerializer(new_comment)

        return Response(serializer.data)

    def delete(self, request, format=None):
        commentid = request.GET.get("id")
        comment = IssueComment.objects.filter(id=commentid)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IssueAttachementList(APIView):
    def get(self, request, format=None):
        issueId = request.GET.get("issueId")
        if issueId:
            attach = Attachment.objects.filter(issueId=issueId)
        else:
            attach = Attachment.objects.all()
        serializer = AttachmentSerializer(attach, many=True)
        return Response(serializer.data)

    def post(self, request):

        data = request.data
        new_attach = Attachment.objects.create(
            issueId=data['issueId'],
            title=data['title'],
            URI=data['URI'],
        )
        new_attach.save()
        serializer = AttachmentSerializer(new_attach)
        return Response(serializer.data)

    def delete(self, request, format=None):
        attachementid = request.GET.get("id")
        attachement = Attachment.objects.filter(id=attachementid)
        attachement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
