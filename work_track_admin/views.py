from django.db.models.fields import return_None
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .models import Tasks, Projects


# Create your views here.
@csrf_exempt
def Add_Tasks(request):
    if request.method=='POST':
        try:
            task_name=request.POST.get('task-name')
            priority=request.POST.get('priority')
            due_date=request.POST.get('due-date')
            status=request.POST.get('status')
            assigned_by=request.POST.get('assigned-by')
            working_hours=request.POST.get('working-hours')
            description=request.POST.get('description')
            discussion=request.POST.get('discussion')
            links=request.POST.get('links')
            attachments=request.POST.get('attachments')
            if task_name and priority and due_date and assigned_by:
                user=Tasks.objects.create(
                    Task_Name=task_name,
                    Priority=priority,
                    Due_Date=due_date,
                    Status=status,
                    Assigned_By=assigned_by,
                    Working_Hours=working_hours,
                    Description=description,
                    Discussion=discussion,
                    Links=links,
                    Attachments=attachments
                )
                return JsonResponse({'message':'successfully added','user':user.id})
        except Exception as e:
            return JsonResponse({'error':f'added field{str(e)}'})
    return JsonResponse({'error':'invalid request method'})

def View_Tasks(request):
    if request.method=="GET":
        try:
            tasks=Tasks.objects.all()
            task_list=[]
            for i in tasks:
                task_list.append({
                    'Task Name':i.Task_Name,
                    'Priority':i.Priority,
                    'Due Date':i.Due_Date,
                    'Staus':i.Status,
                    'Assigned_by':i.Assigned_By
                })
            return JsonResponse({'message':'Successfully viewed','id':task_list})
        except Exception as e:
            return JsonResponse({'error':f'view object{str(e)}'})
    return JsonResponse({'error':'invalid request method'})


@csrf_exempt
def Update_Tasks(request,id):
    tasks=get_object_or_404(Tasks,id=id)
    if request.method=='GET':
        return JsonResponse({
            'Task_Name':tasks.Task_Name,
            'Priority':tasks.Priority,
            'Due_Date':tasks.Due_Date,
            'Status':tasks.Status,
            'Assigned to':tasks.Assigned_By,
            'Description':tasks.Description,
            'Effort Hours':tasks.Working_Hours,
            'Discussion':tasks.Discussion,
            'Links':tasks.Links,
            'Attachments':tasks.Attachments
        })
    elif request.method=='POST':
        try:
            update_taskname=request.POST.get('task-name',tasks.Task_Name)
            update_priority=request.POST.get('priority',tasks.Priority)
            update_duedate=request.POST.get('due-date',tasks.Due_Date)
            update_status=request.POST.get('status',tasks.Status)
            update_assignedto=request.POST.get('assigned-by',tasks.Assigned_By)
            update_description=request.POST.get('description',tasks.Description)
            update_efforthrs=request.POST.get('working-hours',tasks.Working_Hours)
            update_discussion=request.POST.get('discussion',tasks.Discussion)
            update_links=request.POST.get('links',tasks.Links)
            update_attachments=request.POST.get('attachments',tasks.Attachments)

            tasks.Task_Name=update_taskname
            tasks.Priority=update_priority
            tasks.Due_Date=update_duedate
            tasks.Status=update_status
            tasks.Assigned_By=update_assignedto
            tasks.Description=update_description
            tasks.Working_Hours=update_efforthrs
            tasks.Discussion=update_discussion
            tasks.Links=update_links
            tasks.Attachments=update_attachments

            tasks.save()
            return JsonResponse({'message':'successfully updated','id':tasks.id})
        except Exception as e:
            return JsonResponse({'error':f'updated filled{str(e)}'})
    return JsonResponse({'error':'invalid request method'})

@csrf_exempt
def Delete_Task(request,id):
    if request.method=='DELETE':
        try:
            del_task=get_object_or_404(Tasks,id=id)
            del_task.delete()
            return JsonResponse({'message':'successfully deleted'})
        except Exception as e:
            return JsonResponse({'error':f'Deleted data{str(e)}'})
    return JsonResponse({'error':'invalid request method'})

# Projects(CRUD)

@csrf_exempt
def Add_Projects(request):
    if request.method=='POST':
        try:
            project_Name=request.POST.get('project_name')
            print(project_Name)
            company_name=request.POST.get('company_name')
            description=request.POST.get('description')
            assigned_to=request.POST.get('assigned_by')
            due_date=request.POST.get('due_date')
            est_hour=request.POST.get('est_hr')
            priority=request.POST.get('priority')
            links = request.POST.get('links')
            attachments = request.POST.get('attachments')
            status = request.POST.get('status')
            if project_Name and company_name:
                proj=Projects.objects.create(
                    Project_Name=project_Name,
                    Company_Name=company_name,
                    Description=description,
                    Assigned_to=assigned_to,
                    Due_Date=due_date,
                    Est_Hour=est_hour,
                    Priority=priority,
                    Links=links,
                    Attachments=attachments,
                    Status=status
                )
                return JsonResponse({'message':'Successfully added','id':proj.id})
        except Exception as e:
            return JsonResponse({'errror':f'added field{str(e)}'})
    return JsonResponse({'error':'Invalid request method'})

def View_Projects(request):
    if request.method=="GET":
        try:
            proj=Projects.objects.all()
            proj_list=[]
            for i in proj:
                proj_list.append({
                    "Project_Name":i.Project_Name,
                    "Company_Name":i.Company_Name,
                    'Description':i.Description,
                    'Assigned_to':i.Assigned_to,
                    'Due_Date':i.Due_Date,
                    'Est_Hour':i.Est_Hour,
                    'Priority':i.Priority,
                    'Links':i.Links,
                    'Attachments':i.Attachments,
                    'Status':i.Status
                })
            return JsonResponse({'message':'successfully viewed','id':proj_list})
        except Exception as e:
            return JsonResponse({'error':f'viewed data{str(e)}'})
    return JsonResponse({'error':'invalid request method'})

@csrf_exempt
def update_projects(request,id):
    proj = get_object_or_404(Projects,id=id)
    if request.method=='GET':
        return JsonResponse({
            "Project_Name":proj.Project_Name,
            "Company_Name": proj.Company_Name,
            'Description': proj.Description,
            'Assigned_to': proj.Assigned_to,
            'Due_Date': proj.Due_Date,
            'Est_Hour': proj.Est_Hour,
            'Priority': proj.Priority,
            'Links': proj.Links,
            'Attachments': proj.Attachments,
            'Status': proj.Status
        })
    elif request.method=="POST":
        try:
            update_projectname = request.POST.get('task-name', proj.Project_Name)
            update_companyname=request.POST.get('company_name',proj.Company_Name)
            update_description = request.POST.get('description', proj.Description)
            update_assignedto = request.POST.get('assigned-by', proj.Assigned_to)
            update_duedate = request.POST.get('due-date', proj.Due_Date)
            update_esthrs = request.POST.get('working-hours', proj.Est_Hour)
            update_priority=request.POST.get('priority',proj.Priority)
            update_links = request.POST.get('links', proj.Links)
            update_attachments = request.POST.get('attachments', proj.Attachments)
            update_status = request.POST.get('status', proj.Status)

            proj.Project_Name=update_projectname
            proj.Company_Name = update_companyname
            proj.Description = update_description
            proj.Assigned_By = update_assignedto
            proj.Due_Date = update_duedate
            proj.Est_Hour = update_esthrs
            proj.Priority = update_priority
            proj.Links = update_links
            proj.Attachments = update_attachments
            proj.Status = update_status

            proj.save()

            return JsonResponse({'message':'successfully updated','id':proj.id})
        except Exception as e:
            return JsonResponse({'error':f'updated field{str(e)}'})
    return JsonResponse({'error':'invalid request method'})

@csrf_exempt
def Delete_Projects(request,id):
    if request.method=='DELETE':
        try:
            projs=get_object_or_404(Projects,id=id)
            projs.delete()
            return JsonResponse({'message':'Successfully deleted datas'})
        except Exception as e:
            return JsonResponse({'error':f'deleted field    {str(e)}'})
    return JsonResponse({'error':'invalid request method'})





















