from django.contrib.auth.models import BaseUserManager



class CustomUserManager(BaseUserManager):

    def create_user(self,email,password,**extrafields):

        if not email:
            raise ValueError("An Email must be set")
        email = self.normalize_email(email)

        user = self.model(email=email,**extrafields)
        if not password:
            raise ValueError("Password must be set")
        user.set_password(password)
        user.save(using= self._db)
        
        return user
    
    def create_superuser(self,email,password,**extrafields):

        extrafields.setdefault('is_staff',True)
        extrafields.setdefault('is_superuser',True)

        if not extrafields['is_staff']:
            raise ValueError("superuser must have is_staff = True")
        
        if not extrafields['is_superuser']:
            raise ValueError("superuser must have is_superuser = True")
        
        return self.create_user(email=email,password=password,**extrafields)



