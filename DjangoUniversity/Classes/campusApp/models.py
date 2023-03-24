from django.db import models


# Creates a model of University Campuses
class UniversityCampus(models.Model):
    # Defining the attributes of the 'UniversityCampus' class
    campus_name = models.CharField(max_length=60, default="", blank=True, null=False)  # Set string value, 60 char limit
    state = models.CharField(max_length=2, default="", blank=True, null=False)  # Set string value, 2 char limit
    campus_id = models.IntegerField(default="", blank=True, null=False)  # Defining this attribute as an Integer

    # Creates model manager
    object = models.Manager()

    # Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the campus name and campus id
        # field as a tuple to display in the browser
        display_campus = '{0.campus_name}: {0.campus_id}'
        return display_campus.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Campus"
