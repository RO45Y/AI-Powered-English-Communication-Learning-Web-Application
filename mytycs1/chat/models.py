
from django.db import models
from django.contrib.auth.models import User

class GrammarLesson(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class WritingTopic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class ListeningTopic(models.Model):
    title = models.CharField(max_length=200)
    transcript = models.TextField()
    audio_file = models.FileField(upload_to='audio/')
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class SpeakingTopic(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class WeeklyTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    audio_file = models.FileField(upload_to='audio/',default='audio/nightfall-future-bass-music-228100_nTLraq7.mp3')
    date = models.DateField()
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class LessonCompletion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(GrammarLesson, on_delete=models.CASCADE, null=True, blank=True)
    writing_topic = models.ForeignKey(WritingTopic, on_delete=models.CASCADE, null=True, blank=True)
    listening_topic = models.ForeignKey(ListeningTopic, on_delete=models.CASCADE, null=True, blank=True)
    speaking_topic = models.ForeignKey(SpeakingTopic, on_delete=models.CASCADE, null=True, blank=True)
    weekly_task = models.ForeignKey(WeeklyTask, on_delete=models.CASCADE, null=True, blank=True)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'lesson', 'writing_topic', 'listening_topic', 'speaking_topic', 'weekly_task')
