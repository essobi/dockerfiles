FROM python:3  
RUN apt-get update && apt-get install -y vim libsasl2-dev python-dev
libldap2-dev libssl-dev libsasl2-modules  
  
RUN mkdir -p /code/  
WORKDIR /code/  
ADD requirements.txt .  
  
RUN pip install -r requirements.txt  
  
ENV TZ=Asia/Shanghai  
  

