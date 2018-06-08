#Here we create application  
FROM microsoft/dotnet as build  
WORKDIR /docker  
RUN dotnet new mvc --name HelloMVC  
WORKDIR /docker/HelloMVC  
RUN dotnet build  
RUN dotnet publish  
RUN echo "just published"  
RUN pwd  
RUN ls -R -lrt  
ENTRYPOINT [ "dotnet" ]  
  
# What is a stage build ?  
# The ability to run a piece of code when you don't need anything  
# In Jenkins pipeline, you only deployed just the application  
# We do not need to attach to application the build tools  
# We need aspnetcore to create application  
# but we only need runtime to deploy.#Here we install runtime  
FROM microsoft/aspnetcore  
WORKDIR /publish  
COPY \--from=build /docker/HelloMVC/bin/Debug/netcoreapp2.0/publish .  
RUN pwd  
RUN ls -R -lrt  
ENV ASPNET_URLS="http://*:4200"  
EXPOSE 4200 80  
CMD [ "dotnet", "HelloMVC.dll" ]  
  
# EOF

