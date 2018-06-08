FROM python:2  
MAINTAINER Alvaro Lizama <hola@alvarolizama.net>  
ENV PYTHONUNBUFFERED 1  
  
RUN apt-get update && apt-get install unzip \  
&& wget
https://releases.hashicorp.com/envconsul/0.6.1/envconsul_0.6.1_linux_amd64.zip
-O /envconsul.zip \  
&& unzip /envconsul.zip && mv /envconsul /usr/local/bin/envconsul && chmod +x
/usr/local/bin/envconsul \  
&& rm -rf /envconsul.zip  
  

