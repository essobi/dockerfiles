FROM microsoft/aspnetcore-build  
RUN groupadd mygroup && useradd -m -g mygroup myuser  
WORKDIR /home/myuser  
RUN mkdir app  
WORKDIR app  
COPY project.json .  
RUN dotnet restore  
  
# copy and build everything else  
COPY . .  
RUN dotnet publish --output /home/myuser/out/. --configuration Release  
RUN chmod -R +w /home/myuser  
USER myuser  
WORKDIR /home/myuser/out  
#EXPOSE 80 5000  
EXPOSE 5000  
ENTRYPOINT ["dotnet", "app.dll"]  

