FROM debian:jessie  
MAINTAINER Carles Amigó, fr3nd@fr3nd.net  
  
RUN apt-get update && apt-get install -y \  
libdbd-mysql-perl \  
libdbi-perl \  
libio-socket-ssl-perl \  
libterm-readkey-perl \  
perl \  
wget \  
&& rm -rf /usr/share/doc/* && \  
rm -rf /usr/share/info/* && \  
rm -rf /tmp/* && \  
rm -rf /var/tmp/*  
  
ENV PERCONA_VERSION 2.2.14  
WORKDIR /tmp  
RUN wget https://www.percona.com/downloads/percona-
toolkit/${PERCONA_VERSION}/deb/percona-toolkit_${PERCONA_VERSION}_all.deb && \  
dpkg -i percona-toolkit_${PERCONA_VERSION}_all.deb && \  
rm -f percona-toolkit_${PERCONA_VERSION}_all.deb  
  
WORKDIR /  

