FROM debian:jessie  
MAINTAINER Juan Jose Scarafia <jjs@adhoc.com.ar>  
  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y python-uno  
RUN apt-get install -y libreoffice-writer libreoffice-calc  
RUN apt-get install -y openjdk-7-jre  
RUN apt-get clean  
  
EXPOSE 8989  
  
CMD /usr/bin/soffice --nologo --nofirststartwizard --headless --norestore
--invisible "--accept=socket,host=0.0.0.0,port=8100,tcpNoDelay=1;urp;"

