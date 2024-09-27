from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages

from .models import GrammarLesson, LessonCompletion, WritingTopic, ListeningTopic, SpeakingTopic, WeeklyTask

def Homepage(request):
    return render(request, 'conversation/index2.html')

def registerpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')
        
        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')
        
        User.objects.create_user(username, email, password1)
        messages.success(request, "Account created successfully!")
        return redirect('login')
    
    return render(request, 'registration/register.html')
    

def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect!")
            return redirect('login')
    
    return render(request, 'registration/login.html')

def logoutpage(request):
    logout(request)
    return redirect('Homepage')


@login_required
def grammar_list(request):
    lessons = GrammarLesson.objects.all()
    return render(request, 'registration/grammar_list.html', {'lessons': lessons})

@login_required
def writing_topics(request):
    topics = WritingTopic.objects.all()
    return render(request, 'registration/writing_topics.html', {'topics': topics})

@login_required
def listening_topics(request):
    topics = ListeningTopic.objects.all()
    return render(request, 'registration/listening_topic.html', {'topics': topics})

@login_required
def speaking_topics(request):
    topics = SpeakingTopic.objects.all()
    return render(request, 'registration/speaking_topic.html', {'topics': topics})

@login_required
def weekly_tasks_view(request):
   
    # Fetch all weekly tasks
    weekly_tasks = WeeklyTask.objects.all()
    return render(request, 'conversation/home.html',{'weekly_tasks': weekly_tasks})


@login_required
def course(request):
    user = request.user

    # Get the same context as the dashboard
    total_listening_topics = ListeningTopic.objects.count()
    completed_listening_topics = ListeningTopic.objects.filter(lessoncompletion__user=user, is_completed=True).count()
    
    total_writing_topics = WritingTopic.objects.count()
    completed_writing_topics = WritingTopic.objects.filter(lessoncompletion__user=user, is_completed=True).count()
    
    total_speaking_topics = SpeakingTopic.objects.count()
    completed_speaking_topics = SpeakingTopic.objects.filter(lessoncompletion__user=user, is_completed=True).count()
    
    total_grammar_lessons = GrammarLesson.objects.count()
    completed_grammar_lessons = GrammarLesson.objects.filter(lessoncompletion__user=user, is_completed=True).count()

    total_weekly_tasks = WeeklyTask.objects.count()
    completed_weekly_tasks = WeeklyTask.objects.filter(lessoncompletion__user=user, is_completed=True).count()

    completed_courses = completed_grammar_lessons + completed_writing_topics + completed_listening_topics + completed_speaking_topics
    total_courses = total_grammar_lessons + total_writing_topics + total_listening_topics + total_speaking_topics
    in_progress_courses = total_courses - completed_courses
    total_points = completed_courses * 10
    weekly_tasks = WeeklyTask.objects.all()

    course_completion_percentage = (completed_courses / total_courses * 100) if total_courses > 0 else 0
    listening_completion_percentage = (completed_listening_topics / total_listening_topics * 100) if total_listening_topics > 0 else 0
    writing_completion_percentage = (completed_writing_topics / total_writing_topics * 100) if total_writing_topics > 0 else 0
    speaking_completion_percentage = (completed_speaking_topics / total_speaking_topics * 100) if total_speaking_topics > 0 else 0
    grammar_completion_percentage = (completed_grammar_lessons / total_grammar_lessons * 100) if total_grammar_lessons > 0 else 0
    weekly_task_completion_percentage = (completed_weekly_tasks / total_weekly_tasks * 100) if total_weekly_tasks > 0 else 0

    context = {
        'user': user,
        'total_listening_topics': total_listening_topics,
        'completed_listening_topics': completed_listening_topics,
        'total_writing_topics': total_writing_topics,
        'completed_writing_topics': completed_writing_topics,
        'total_speaking_topics': total_speaking_topics,
        'completed_speaking_topics': completed_speaking_topics,
        'total_grammar_lessons': total_grammar_lessons,
        'completed_grammar_lessons': completed_grammar_lessons,
        'completed_courses': completed_courses,
        'total_courses': total_courses,
        'in_progress_courses': in_progress_courses,
        'total_points': total_points,
        'completed_tasks': completed_weekly_tasks,
        'total_weekly_tasks': total_weekly_tasks,
        'weekly_tasks': weekly_tasks,
        'course_completion_percentage': course_completion_percentage,
        'listening_completion_percentage': listening_completion_percentage,
        'writing_completion_percentage': writing_completion_percentage,
        'speaking_completion_percentage': speaking_completion_percentage,
        'grammar_completion_percentage': grammar_completion_percentage,
        'weekly_task_completion_percentage': weekly_task_completion_percentage,
    }
    return render(request, 'registration/course.html', context)

@login_required
def resource(request):
    return render(request, 'registration/resource.html')



# views.py
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import GrammarLesson, LessonCompletion, WritingTopic, ListeningTopic, SpeakingTopic, WeeklyTask

@login_required
def dashboard(request):

    user = request.user

    total_listening_topics = ListeningTopic.objects.count()
    completed_listening_topics = ListeningTopic.objects.filter(lessoncompletion__user=user, is_completed=True).count()
    
    total_writing_topics = WritingTopic.objects.count()
    completed_writing_topics = WritingTopic.objects.filter(lessoncompletion__user=user, is_completed=True).count()
    
    total_speaking_topics = SpeakingTopic.objects.count()
    completed_speaking_topics = SpeakingTopic.objects.filter(lessoncompletion__user=user, is_completed=True).count()
    
    total_grammar_lessons = GrammarLesson.objects.count()
    completed_grammar_lessons = GrammarLesson.objects.filter(lessoncompletion__user=user, is_completed=True).count()

    total_weekly_tasks = WeeklyTask.objects.count()
    completed_weekly_tasks = WeeklyTask.objects.filter(lessoncompletion__user=user, is_completed=True).count()

    completed_courses = completed_grammar_lessons + completed_writing_topics + completed_listening_topics + completed_speaking_topics
    total_courses = total_grammar_lessons + total_writing_topics + total_listening_topics + total_speaking_topics
    in_progress_courses = total_courses - completed_courses
    total_points = completed_courses * 10
    weekly_tasks = WeeklyTask.objects.all()
    completed_task_ids = set(
        LessonCompletion.objects.filter(user=user).values_list('weekly_task_id', flat=True).exclude(weekly_task_id=None)
    )

    course_completion_percentage = (completed_courses / total_courses * 100) if total_courses > 0 else 0
    listening_completion_percentage = (completed_listening_topics / total_listening_topics * 100) if total_listening_topics > 0 else 0
    writing_completion_percentage = (completed_writing_topics / total_writing_topics * 100) if total_writing_topics > 0 else 0
    speaking_completion_percentage = (completed_speaking_topics / total_speaking_topics * 100) if total_speaking_topics > 0 else 0
    grammar_completion_percentage = (completed_grammar_lessons / total_grammar_lessons * 100) if total_grammar_lessons > 0 else 0
    weekly_task_completion_percentage = (completed_weekly_tasks / total_weekly_tasks * 100) if total_weekly_tasks > 0 else 0

    context = {
        'user': user,
        'total_listening_topics': total_listening_topics,
        'completed_listening_topics': completed_listening_topics,
        'total_writing_topics': total_writing_topics,
        'completed_writing_topics': completed_writing_topics,
        'total_speaking_topics': total_speaking_topics,
        'completed_speaking_topics': completed_speaking_topics,
        'total_grammar_lessons': total_grammar_lessons,
        'completed_grammar_lessons': completed_grammar_lessons,
        'completed_courses': completed_courses,
        'total_courses': total_courses,
        'in_progress_courses': in_progress_courses,
        'total_points': total_points,
        'completed_tasks': completed_weekly_tasks,
        'total_weekly_tasks': total_weekly_tasks,
        'weekly_tasks':weekly_tasks,
        'course_completion_percentage': course_completion_percentage,
        'listening_completion_percentage': listening_completion_percentage,
        'writing_completion_percentage': writing_completion_percentage,
        'speaking_completion_percentage': speaking_completion_percentage,
        'grammar_completion_percentage': grammar_completion_percentage,
        'weekly_task_completion_percentage': weekly_task_completion_percentage,
        'completed_task_ids': completed_task_ids
    }
    return render(request, 'conversation/home.html', context)



@login_required
def mark_lesson_complete(request, lesson_id, lesson_type):
    if lesson_type == 'grammar':
        lesson = get_object_or_404(GrammarLesson, id=lesson_id)
        LessonCompletion.objects.update_or_create(
            user=request.user, 
            lesson=lesson,
            defaults={'completed_at': timezone.now()}
        )
        lesson.is_completed = True
        lesson.save()
    elif lesson_type == 'writing':
        topic = get_object_or_404(WritingTopic, id=lesson_id)
        LessonCompletion.objects.update_or_create(
            user=request.user, 
            writing_topic=topic,
            defaults={'completed_at': timezone.now()}
        )
        topic.is_completed = True
        topic.save()
    elif lesson_type == 'listening':
        topic = get_object_or_404(ListeningTopic, id=lesson_id)
        LessonCompletion.objects.update_or_create(
            user=request.user, 
            listening_topic=topic,
            defaults={'completed_at': timezone.now()}
        )
        topic.is_completed = True
        topic.save()
    elif lesson_type == 'speaking':
        topic = get_object_or_404(SpeakingTopic, id=lesson_id)
        LessonCompletion.objects.update_or_create(
            user=request.user, 
            speaking_topic=topic,
            defaults={'completed_at': timezone.now()}
        )
        topic.is_completed = True
        topic.save()
    elif lesson_type == 'weeklytask':
        task = get_object_or_404(WeeklyTask, id=lesson_id)
        LessonCompletion.objects.update_or_create(
            user=request.user, 
            weekly_task=task,
            defaults={'completed_at': timezone.now()}
        )
        task.is_completed = True
        task.save()
    else:
        return redirect('homepage')  # Handle unknown type

    return redirect(request.META.get('HTTP_REFERER', 'dashboard'))
