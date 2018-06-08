FROM python:alpine  
LABEL maintainer Morten Abildgaard <morten@abildgaard.org>  
ADD requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
ADD main.py .  
EXPOSE 8081  
ENTRYPOINT ["./main.py"]  

