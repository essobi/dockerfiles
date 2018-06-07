FROM mono:4.2.3.4  
RUN mkdir -p release  
RUN apt-get update  
RUN apt-get install mono-mcs -y  
COPY webserver.cs .  
RUN mcs ./webserver.cs -out:release/webserver.exe  
  
EXPOSE 8080  
CMD [ "mono", "release/webserver.exe" ]  

