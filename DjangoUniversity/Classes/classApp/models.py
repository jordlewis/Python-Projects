from django.db import models


# Creates a model of University Classes
class UniversityClasses(models.Model):
    # Defining the attributes of the 'UniversityClasses' class
    title = models.CharField(max_length=60, default="", blank=True, null=False)  # Set string value, 60 char limit
    course_number = models.IntegerField(default="", blank=True, null=False)  # Defining this attribute as an Integer
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=False, default=None)  # Defining this attribute as a float

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Classes"
