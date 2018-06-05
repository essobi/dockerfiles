# This Dockerfile uses dbuild for consistent builds.  
# https://bitbucket.org/ebsv/docker-build  
#  
# START PRE-BUILD  
#  
# # Image repository name  
# #  
# REPOSITORY="jbulcher/ambassador"  
#  
# # Image tag  
# #  
# TAG="0.1.1"  
#  
# # Perform other pre-build steps here  
#  
# END PRE-BUILD  
#  
# ================================  
#  
# START POST-BUILD  
#  
# # Perform any post-build steps here  
#  
# END POST-BUILD  
  
FROM debian:latest  
  
RUN DEBIAN_FRONTEND=noninteractive; \  
apt-get update && \  
apt-get -y install \  
net-tools \  
rinetd  
  
COPY rinetd.conf.template /etc/rinetd.conf.template  
COPY run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
CMD /usr/local/bin/run.sh  

