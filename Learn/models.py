from django.db import models


STATUS = (
    ('adept', 'Never done this before'),
    ('padawan', 'I wrote some code'),
    ('jedi', 'I can use it'),
    ('jedi_master', "I'm expert")
)


class Learn(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    github_url = models.URLField(null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=50, default='adept')

    def __str__(self):
        return self.title


class Comments(models.Model):
    learn = models.ForeignKey(Learn, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f' Comment id: {self.id}'
