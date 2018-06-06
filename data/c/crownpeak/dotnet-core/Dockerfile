##########################################################################  
# Image: crownpeak/dotnet-core:1.0  
# Maintained by: CrownPeak Advanced Solutions Group <asg@crownpeak.com>  
##########################################################################  
FROM crownpeak/ubuntu:14.04  
MAINTAINER Crownpeak Advanced Solutions Group <asg@crownpeak.com>  
ENV REFRESHED_AT 2016-12-19  
  
EXPOSE 5000  
  
ADD startcontainer.sh /opt/container/  
RUN apt-get -yqq update && \  
apt-get -yqq install apt-transport-https && \  
sh -c 'echo "deb [arch=amd64] https://apt-mo.trafficmanager.net/repos/dotnet-
release/ trusty main" > /etc/apt/sources.list.d/dotnetdev.list' && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893 &&
\  
apt-get -yqq update && \  
apt-get -yqq install dotnet-dev-1.0.0-preview2.1-003177 && \  
chmod u+x /opt/container/startcontainer.sh  
  
ENTRYPOINT [ "/bin/bash", "/opt/container/startcontainer.sh" ]

