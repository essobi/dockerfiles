# Build Docker Container for Integration Testing,  
# Performance Testing, Deployment into a QA Environment  
############################################  
# THESE COMMANDS RUN ON CONTAINER CREATION #  
############################################  
# Get Public Docker image created with Debian, .net core, mongo db, apache
bench  
FROM mick8moses/dotnetcore_plusplus:latest  
MAINTAINER Michael Miller, mick8moses@yahoo.com  
  
# Copy Source Code "." from Source Code Repository (bitbucket) and to a
directory  
# in Docker image called Lou  
COPY . /Lou  
  
# Set working directory to the API  
WORKDIR /Lou/src/Lou.Web  
  
# Restore dotnet dependencies & build project  
RUN ["dotnet", "restore"]  
RUN ["dotnet", "build", "--configuration", "Release"]  
  
# Start MongoDB (Eventually move MongoDB to it's own Docker container)  
RUN ["mongod", "--fork","--dbpath","/data/db", "--smallfiles", "--logpath",
"/var/log/mongodb.log", "--logappend"]  
  
# Expose ports: 5000 where the API resides  
EXPOSE 5000  
# set the environment variable for .NET Core in the container  
ENV NETCORE_URLS http://*:5000  
#############################################  
# THESE COMMANDS RUN ON CONTAINER EXECUTION #  
#############################################  
# initial entry point (start the server)  
ENTRYPOINT ["dotnet", "run", "--project", "project.json"]  
  
  

