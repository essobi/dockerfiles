FROM microsoft/aspnet:1.0.0-rc1-update1-coreclr  
  
MAINTAINER Jeremy Cade <me@jeremycade.com>  
LABEL Description="This is an example of sending Email from an ASP.NET Core
1.0 Application.. Changed"  
  
COPY . /app  
WORKDIR /app  
  
RUN ["dnu", "restore"]  
RUN ["dnu", "build"]  
  
EXPOSE 5000  
ENTRYPOINT ["dnx", "-p", "project.json", "web"]

