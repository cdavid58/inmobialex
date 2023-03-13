from django.db import models

class Resident(models.Model):
	name = models.CharField(max_length = 60)
	name_user = models.CharField(max_length = 60, null= True, blank = True)
	email = models.EmailField(unique=True)
	phone = models.CharField(max_length = 15, unique = True, null= True, blank = True)
	date_brithday = models.CharField(max_length = 12, null= True, blank = True)
	nationality = models.CharField(max_length = 40, null= True, blank = True)
	gender = models.CharField(max_length = 20, null= True, blank = True)
	address = models.CharField(max_length = 250, null= True, blank = True)
	psswd = models.CharField(max_length = 20)
	photo = models.ImageField(upload_to = "Profile",default = "Profile/photo.png")

	def __str__(self):
		return self.email


class Social(models.Model):
	facebook = models.URLField(null= True, blank = True)
	twitter = models.URLField(null= True, blank = True)
	instagram = models.URLField(null= True, blank = True)
	resident = models.ForeignKey(Resident, on_delete = models.CASCADE)


