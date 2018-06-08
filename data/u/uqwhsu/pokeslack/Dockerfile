############################################################  
# Dockerfile to build a PokeSlack notification bot  
############################################################  
  
FROM centos:7  
  
MAINTAINER Will Hsu <uqwhsu@gmail.com>  
  
# Add repo, install packages  
RUN yum -y update && \  
yum -y install epel-release && \  
yum -y install python-devel python-pip git gcc supervisor && \  
yum clean all  
  
# clone PokeSlack and install dependencies  
RUN cd /opt && \  
git clone https://github.com/timwah/pokeslack.git . && \  
pip --disable-pip-version-check --no-cache-dir install -r requirements.txt  
  
# copy setting file  
COPY .env /opt  
  
# copy custom init and restart scripts  
COPY run.sh /opt  
COPY restart.sh /opt  
  
# Copy supervisor config over to the container  
COPY supervisord.conf /etc/supervisord.conf  
  
WORKDIR /opt  
  
# fix permission  
RUN chmod 755 /opt/run.sh /opt/restart.sh  
  
CMD ["/opt/run.sh"]  
  
VOLUME ["/opt"]  

