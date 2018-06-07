# The `FROM` instruction specifies the base image. You are  
# extending the `microsoft/aspnet` image.  
FROM microsoft/aspnet  
COPY ./bin/Release/PublishOutput/ /inetpub/wwwroot  
#  
#ARG source="/bin/Release/PublishOutput"  
#WORKDIR /app  
# The final instruction copies the site you published earlier into the
container.  
#COPY $source .  
# Open the port  
# EXPOSE 80  
# Commands:  
#  
# docker build -t dogemvc .  
# docker run -d --name doge dogemvc  
#  
# -p 8080:8080  
# Find IP address of local docker image  
# docker inspect -f "{{ .NetworkSettings.Networks.nat.IPAddress }}" doge  
#  
# See all images  
# docker images  
# Restore the necessary packages -- If we are not using publish  
## RUN dotnet restore  
##ENTRYPOINT ["dotnet", "run"]  
# Define environment variable  
#ENV NAME World  
# Run app.py when the container launches  
#CMD ["python", "app.py"]  
# \-----------------  
# Expose port 80 for the Web API traffic  
#ENV ASPNETCORE_URLS http://+:80  
#EXPOSE 80  
# Build and run the dotnet application from within the container  
#ENTRYPOINT ["dotnet", "run"]  
#  
# git fetch origin master && git merge origin/master && git push origin
stage:master

