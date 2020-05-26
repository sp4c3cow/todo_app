from django.db import models

class Make_ToDo(models.Model):
    STATUS = [
        ("To Do", "To Do"),
        ("In Progress", "In Progress"),
        ("Done", "Done"),
    ]
    task_name = models.CharField(max_length=255)
    status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return self.task_name

    