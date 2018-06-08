#Here we create application  
FROM microsoft/dotnet as build  
WORKDIR /docker  
RUN git clone https://github.com/1803-mar12-net/proj2-derek-joseph-tim.git  
RUN ls -lrt proj2-derek-joseph-tim  
RUN dotnet build proj2-derek-joseph-
tim/WeatherApp/WeatherApp.ClientMVC/WeatherApp.ClientMVC.sln  
RUN dotnet publish proj2-derek-joseph-tim/WeatherApp/WeatherApp.ClientMVC
--output ./bin  
ENTRYPOINT [ "dotnet" ]  
  
# What is a stage build ?  
# The ability to run a peice of code when you don't need anything  
# In Jenkins pipeline, you only deployed just the application  
# We do not need to attach to application the build tools  
# We need aspnetcore to create application  
# but we only need runtime to deploy.  
#Here we install runtime  
FROM microsoft/aspnetcore  
WORKDIR /publish  
COPY \--from=build /docker/proj2-derek-joseph-
tim/WeatherApp/WeatherApp.ClientMVC/WeatherApp.ClientMVC/bin .  
RUN pwd  
RUN ls -lrt  
ENV ASPNET_URLS="http://*:4200"  
EXPOSE 4200 80  
CMD [ "dotnet", "WeatherApp.ClientMVC.dll" ]  
  
# We want dotnet run when we call the image

