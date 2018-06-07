FROM java:8  
MAINTAINER snowmoon6467  
  
  
ENV JOBSCHEDULER_VERSION 1.9.2  
RUN mkdir -p /opt/jobscheduler && cd /opt/jobscheduler; curl -L
http://sourceforge.net/projects/jobscheduler/files/JobScheduler.1.9/JobScheduler.$JOBSCHEDULER_VERSION/jobscheduler_linux-x64.$JOBSCHEDULER_VERSION.tar.gz
-o - | tar -xz --strip-components=1  
  
# SSH, API/HTTP, API/HTTPS, JOC  
EXPOSE 22 44440 8443 4444  
USER root  
  
COPY scheduler_install.xml /opt/jobscheduler/scheduler_install.xml  
  
# Set the default command to run when starting the container  
COPY startup-jobscheduler.sh /opt/startup-jobscheduler.sh  
CMD ["/opt/startup-jobscheduler.sh"]  

