FROM microsoft/dotnet:1.1.1-sdk  
COPY . /app  
WORKDIR /app  
  
RUN ["useradd", "-u", "1001", "-r", "-g", "0", "-m", "-d", "/home/default",
"-s", "/bin/bash", "default"]  
RUN ["chown", "-R", "1001:0", "/app"]  
USER 1001  
ENV HOME /home/default  
ENV NUGET_XMLDOC_MODE skip  
RUN ["dotnet", "restore"]  
RUN ["dotnet", "build"]  
USER 0  
RUN ["chown", "-R", "1001:0", "/app"]  
RUN ["chmod", "-R", "og+rwx", "/app"]  
USER 1001  
ENV HOME /home/default  
  
EXPOSE 5000/tcp  
ENV ASPNETCORE_URLS http://*:5000  
ENTRYPOINT ["dotnet", "run"]  

