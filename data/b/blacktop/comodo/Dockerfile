FROM ubuntu:latest  
MAINTAINER blacktop, https://github.com/blacktop  
  
# Make sure that Upstart won't try to start avgd after dpkg installs it  
# https://github.com/dotcloud/docker/issues/446  
ADD policy-rc.d /usr/sbin/policy-rc.d  
RUN /bin/chmod 755 /usr/sbin/policy-rc.d  
  
# Install Requirements  
RUN apt-get update && apt-get install -y gdebi  
# Get AVG Installer  
ADD http://download.comodo.com/cavmgl/download/installs/1000/standalone/cav-
linux_1.1.268025-1_amd64.deb /comodo/  
# Install Comodo  
RUN DEBIAN_FRONTEND=noninteractive gdebi -n /comodo/cav-
linux_1.1.268025-1_amd64.deb  
# Run Post Install Script and Accept Defaults  
RUN DEBIAN_FRONTEND=noninteractive /opt/COMODO/post_setup.sh  
# Update Comodo AV Definitions  
ADD http://download.comodo.com/av/updates58/sigs/bases/bases.cav
/opt/COMODO/scanners/bases.cav  
  
# Add Files  
ADD /malware /malware  
#ADD /supervisord-avast.conf /etc/supervisor/conf.d/supervisord-avast.conf  
# ADD /run.sh /run.sh  
# RUN chmod 755 /*.sh  
WORKDIR /malware  
  
ENTRYPOINT ["/opt/COMODO/cmdscan"]  
  
CMD ["-h"]  

