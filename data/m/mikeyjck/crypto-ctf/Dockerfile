FROM python:2.7  
ADD /src /src  
  
MAINTAINER Michael Jack <cryptoCTF@mikeyjck.io>  
LABEL version="0.1"  
  
EXPOSE 1337  
RUN chmod +x /src/server.py  
  
CMD [ "python", "-u", "./src/server.py" ]  

