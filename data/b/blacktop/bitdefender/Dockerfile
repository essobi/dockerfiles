FROM ubuntu:latest  
MAINTAINER blacktop, https://github.com/blacktop  
  
# Upstart Fix  
# https://github.com/dotcloud/docker/issues/446  
ADD policy-rc.d /usr/sbin/policy-rc.d  
RUN /bin/chmod 755 /usr/sbin/policy-rc.d  
  
# Install Requirements  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq wget libc6-i386
supervisor  
RUN wget -O- -q http://download.bitdefender.com/repos/deb/bd.key.asc | apt-key
add -  
RUN sh -c 'echo "deb http://download.bitdefender.com/repos/deb/ bitdefender
non-free" >> /etc/apt/sources.list'  
  
# Install BitBitDefender  
RUN apt-get update -qq  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq bitdefender-scanner  
RUN cat /opt/BitDefender-scanner/etc/bdscan.conf > /opt/BitDefender-
scanner/etc/bdscan.conf.bak  
RUN echo "LicenseAccepted = True" >> /opt/BitDefender-scanner/etc/bdscan.conf  
RUN bdscan --update  
  
# Add Files  
ADD /supervisord-bdscan.conf /etc/supervisor/conf.d/supervisord-bdscan.conf  
ADD /malware/EICAR /malware/EICAR  
ADD /run.sh /run.sh  
RUN chmod 755 /run.sh  
  
WORKDIR /malware  
  
ENTRYPOINT ["bdscan"]

