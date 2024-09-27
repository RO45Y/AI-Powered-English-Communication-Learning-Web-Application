
# admin.py
from django.contrib import admin
from .models import GrammarLesson, WritingTopic, ListeningTopic, SpeakingTopic, LessonCompletion, WeeklyTask

@admin.register(GrammarLesson)
class GrammarLessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_completed')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)

@admin.register(WritingTopic)
class WritingTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_completed')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

@admin.register(ListeningTopic)
class ListeningTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'audio_file', 'created_at', 'is_completed')
    search_fields = ('title', 'transcript')
    ordering = ('-created_at',)

@admin.register(SpeakingTopic)
class SpeakingTopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_completed')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

@admin.register(WeeklyTask)
class WeeklyTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'audio_file', 'date', 'is_completed')
    list_filter = ('date', 'is_completed')
    search_fields = ('title', 'description')
    ordering = ('-date',)

@admin.register(LessonCompletion)
class LessonCompletionAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'writing_topic', 'listening_topic', 'speaking_topic', 'weekly_task', 'completed_at')
    search_fields = ('user__username',)
    ordering = ('-completed_at',)
