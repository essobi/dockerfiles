FROM microsoft/dotnet:2.0.0-sdk-jessie  
  
RUN apt-get update && apt-get install make gcc -y  
  
RUN wget https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-debian81-3.4.9.tgz -q && tar xzf mongodb-
linux-x86_64-debian81-3.4.9.tgz  
  
RUN mkdir -p /data/db  
  
RUN mkdir -p /dotnetapp  
  
COPY . /dotnetapp  
WORKDIR /dotnetapp/HiP-Achievements  
  
EXPOSE 5000  
RUN dotnet build  
RUN chmod +x /dotnetapp/HiP-Achievements/run.sh  
CMD /dotnetapp/HiP-Achievements/run.sh  

