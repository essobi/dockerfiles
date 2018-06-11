FROM python:3.5  
MAINTAINER Michael Yuen <michael.yuen@mac.com>  
  
RUN mkdir -p /text  
RUN pip install restview  
  
EXPOSE 8080  
CMD [ "/usr/bin/nohup", "/bin/bash", "-c", "restview --listen=*:8080 /text >
/dev/stdout 2>&1" ]  
  

