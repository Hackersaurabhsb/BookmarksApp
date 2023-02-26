from django.contrib.auth.models import User
class EmailAuthBackend:
    def authenticate(self,request,username=None,password=None):
        try:
            get_email=User.objects.get(email=username)
            if get_email.check_password(password):
                return user
            return none
        except (User.DoesNotExist,User.MultipleObjectsReturned):
            return None
    def get_user(self,user_id):
        try:
            get=User.objects.get(id=user_id)
            return get
        except User.DoesNotExist:
            return None