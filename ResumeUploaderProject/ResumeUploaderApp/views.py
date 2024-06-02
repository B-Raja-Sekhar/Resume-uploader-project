from django.http import HttpResponseRedirect
from django.shortcuts import render
from ResumeUploaderApp.forms import ResumeForm
from ResumeUploaderApp.models import Resume
from django.views import View
from django.contrib import messages

# Create your views here.
class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        candidates = Resume.objects.all()
        return render(request,'home.html',
                      {'form':form,'candidates':candidates})

    def post(self, request):
        form = ResumeForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Profile has posted successfully")
            return render(request,'home.html',{'form':form})
class CandidateView(View):
    def get(self,request,pk):
        candidate = Resume.objects.get(pk=pk)
        return render(request,'candidate.html',{'candidate':candidate})



