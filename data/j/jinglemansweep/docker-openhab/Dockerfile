FROM ubuntu:latest  
MAINTAINER JingleManSweep <jinglemansweep@gmail.com>  
  
# Install dependencies  
RUN apt-get update -y && \  
apt-get upgrade -y && \  
apt-get dist-upgrade -y && \  
apt-get install -y openjdk-8-jre unzip && \  
update-ca-certificates -f  
  
# Download Openhab  
ADD
https://bintray.com/artifact/download/openhab/bin/distribution-1.8.3-runtime.zip
/tmp/distribution-runtime.zip  
ADD
https://bintray.com/artifact/download/openhab/bin/distribution-1.8.3-addons.zip
/tmp/distribution-addons.zip  
  
# Install Openhab  
RUN mkdir -p /opt/openhab/addons-avail  
RUN unzip -d /opt/openhab /tmp/distribution-runtime.zip  
RUN unzip -d /opt/openhab/addons-avail /tmp/distribution-addons.zip  
RUN chmod +x /opt/openhab/start.sh  
  
# Add boot script  
ADD files/boot.sh /usr/local/bin/boot.sh  
RUN chmod +x /usr/local/bin/boot.sh  
  
EXPOSE 8080 8443  
CMD /usr/local/bin/boot.sh  

