# Dockerfile for Beacon  
FROM python:2.7  
MAINTAINER Alexandros Sigaras <als2076@med.cornell.edu>  
#=====================#  
# Setup Prerequisites #  
#=====================#  
RUN apt-get update \  
&& apt-get -y install apache2 \  
git \  
vim \  
&& a2enmod cgi \  
&& service apache2 restart \  
&& rm -rf /var/lib/apt/lists/*  
#=====================#  
# Install Beacon #  
#=====================#  
ENV BEACON_DIR /var/www/html/beacon  
RUN mkdir -p $BEACON_DIR \  
&& git clone https://github.com/maximilianh/ucscBeacon.git \  
&& cd ucscBeacon/ \  
&& sed -i "s/'server.socket_port': port/'server.socket_port': port,
'server.socket_host': '0.0.0.0'/g" query  
#=====================#  
# Configure Beacon #  
#=====================#  
RUN echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf \  
&& a2enconf fqdn  
COPY config/beacon.conf $BEACON_DIR/beacon.conf  
COPY config/apache2.conf /etc/apache2/apache2.conf  
COPY app $BEACON_DIR  
#=====================#  
# Beacon Startup #  
#=====================#  
CMD /usr/sbin/apache2ctl -D FOREGROUND  

