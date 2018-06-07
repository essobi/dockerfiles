FROM microsoft/dotnet:2.0.0-sdk-jessie  
  
RUN wget https://fastdl.mongodb.org/linux/mongodb-
linux-x86_64-debian81-3.4.9.tgz -q && tar xzf mongodb-
linux-x86_64-debian81-3.4.9.tgz  
  
RUN mkdir -p /data/db  
  
RUN mkdir -p /dotnetapp  
  
COPY . /dotnetapp  
WORKDIR /dotnetapp/HiP-DataStore  
  
EXPOSE 5000  
RUN dotnet build  
  
CMD /dotnetapp/HiP-DataStore/run.sh  

