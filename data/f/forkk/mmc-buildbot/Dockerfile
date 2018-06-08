# Buildbot Master for MultiMC  
#  
# VERSION 1.0  
FROM forkk/buildbot  
MAINTAINER Andrew Okin, forkk@forkk.net  
  
RUN pip install lazy_reload boto paramiko  
  
VOLUME /var/lib/buildbot/  
VOLUME /root/.ssh/  
  
COPY bbot-config /etc/buildbot/config/  
  
COPY init-buildbot /bin/init-buildbot  
  
COPY run-buildbot /bin/run-buildbot  
  
EXPOSE 80 9989  

