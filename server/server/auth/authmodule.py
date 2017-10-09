import django

class OnlyOne:
    class __OnlyOne:
        def __init__(self, arg):
            self.val = arg
        def __str__(self):
            return repr(self) + self.val
    instance = None
    def __init__(self, arg):
        if not OnlyOne.instance:
            OnlyOne.instance = OnlyOne.__OnlyOne(arg)
        else:
            OnlyOne.instance.val = arg
    def __getattr__(self, name):
        return getattr(self.instance, name)
    def createuser(username, password):
        user = User.object.create_user(username, password)
        user = authenticate(username, password)
        if user is not None:
            login(request, user)
            #backend authenticates
        #else:
            
    def userlogin(request, username, password):
        user = authenticate(username, password)
        if user is not None:
            login(request, user)
            #backend authenticates
        #else:
    
    def passwordchange(username, password):
        user = User.objects.get(username)
        user.set_password(password)
        user.save()
    def logout_view(request):
        logout(request)
        #redirect goes here
    
