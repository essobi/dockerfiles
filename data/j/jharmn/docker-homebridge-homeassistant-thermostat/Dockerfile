FROM python  
  
MAINTAINER Jason Harmon <jason.harmon@gmail.com>  
  
RUN apt-get update && apt-get install -y python-pip  
  
VOLUME ["/config"]  
RUN mkdir /server  
WORKDIR /server  
  
COPY requirements.txt requirements.txt  
COPY server.py server.py  
RUN ["pip", "install", "-r", "requirements.txt"]  
  
EXPOSE 8124  
ENTRYPOINT ["python", "/server/server.py", "-c", "/config/config.yaml"]  

