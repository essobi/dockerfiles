# Ubuntu with MultiMC Buildbot  
#  
# VERSION 1.0  
FROM ubuntu  
MAINTAINER Andrew Okin, forkk@forkk.net  
  
# Install pip  
RUN apt-get update && apt-get install -y \  
python-dev \  
python-pip  
  
# Install Buildbot  
RUN pip install buildbot  
  
# Create the master  
RUN buildbot create-master -c /etc/buildbot.cfg -r /buildbot/  
  
# Install Python 3 tools  
RUN apt-get install -y \  
python3-dev \  
python3-pip  
  
# Install git  
RUN apt-get install -y \  
git  
  
RUN pip3 install 'git+https://github.com/MultiMC/repoman2.git'  
  
# Symlink Boto config (this file will be injected into the container in the  
# /buildbot/private folder.  
RUN ln -s /buildbot/private/boto.cfg /etc/boto.cfg  
  
VOLUME ["/buildbot/"]  
EXPOSE 8010 9989  
# We need this in a different folder because the buildbot folder will be in a  
# volume.  
COPY master.cfg /etc/buildbot.cfg  
  
CMD ["buildbot", "start", "--nodaemon", "/buildbot"]  

