FROM python:3  
MAINTAINER Hunter Chung <hchung@zymoresearch.com>  
  
RUN apt-get update && apt-get -yq install \  
rsync && \  
apt-get clean autoclean && apt-get autoremove -y  
  
RUN pip install \  
boto3 \  
pymongo==2.8 \  
mongoengine  
  
WORKDIR /scripts  
VOLUME /run  
ENV PYTHONPATH=/scripts  
# ENV REMOTE_OUT=~/hiseq  
ENV USERNAME=core  
  
ENTRYPOINT ["python", "bird_watcher/upload.py"]  

