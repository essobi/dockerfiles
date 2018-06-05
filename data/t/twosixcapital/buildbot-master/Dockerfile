FROM python:2.7  
RUN apt-get update  
# Install make  
RUN apt-get -y install build-essential  
  
# Install other required Python packages  
ADD requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
  
# Start buildbot  
ADD buildbot_startup.sh /buildbot/buildbot_startup.sh  
RUN chmod +x /buildbot/buildbot_startup.sh  

