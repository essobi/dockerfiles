FROM phusion/baseimage  
MAINTAINER Richard Fuller "rcf799@gmail.com"  
RUN apt-get -y update  
RUN apt-get install -y build-essential checkinstall python3 python3-pip \  
ghostscript libgs-dev imagemagick python-zbar libmagickwand-dev libzbar0  
  
COPY requirements.txt .  
RUN pip3 install -r requirements.txt  
COPY /app /app  
WORKDIR /app  
ENTRYPOINT ["python3"]  
CMD ["app.py"]  

