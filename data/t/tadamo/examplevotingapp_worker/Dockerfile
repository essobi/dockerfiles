FROM dockersamples/examplevotingapp_worker  
# When trying to run this in OpenShift, I can't get postgres running w/o  
# an admin password. I need a way to set it.  
COPY Program.cs /code/src/Worker/  
  
RUN dotnet restore -v minimal src/Worker \  
&& dotnet publish -c Release -o "./" "src/Worker/"  
  
CMD dotnet src/Worker/Worker.dll  

