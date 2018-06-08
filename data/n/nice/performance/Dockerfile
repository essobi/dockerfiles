FROM google/python  
MAINTAINER Lee Smith <leesmith110@googlemail.com>  
  
RUN apt-get install -y apt-utils build-essential libssl-dev libffi-dev  
  
WORKDIR /app  
RUN virtualenv /env  
COPY /requirements.txt /app/requirements.txt  
RUN /env/bin/pip install -r /app/requirements.txt  
COPY app/ /app/  
  
#Add in your .p12 Key to the repository this is installed locally on the
server and in a private github repo  
#COPY /usr/share/performance_secure_key/secure_key.p12 /app/  
EXPOSE 5000  
CMD ["/env/bin/python", "/app/index.py"]  

