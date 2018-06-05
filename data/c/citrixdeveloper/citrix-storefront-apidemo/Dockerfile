ARG version='1.0'  
#start from the base dotnet core SDK  
#FROM microsoft/aspnetcore-build  
FROM microsoft/dotnet:sdk  
  
#set LABEL  
LABEL Description="This image contains the sample web app that shows how to
interact with the storefront API"  
#Make a directory to store the sample web app  
RUN mkdir /sampleweb  
  
#copy the site to the docker image  
COPY . /sampleweb  
  
#change the working directory  
WORKDIR /sampleweb/  
  
#clean out any reminants of artifacts  
RUN ["dotnet", "clean"]  
#restoring any dependencies  
RUN ["dotnet", "restore"]  
#building the web site.  
RUN ["dotnet","build"]  
  
#expose port 5000 as the website will be listening on this port.  
EXPOSE 5000/tcp  
  
ENV ASPNETCORE_URLS http://*:5000  
ENTRYPOINT [ "dotnet","run" ]  
  

