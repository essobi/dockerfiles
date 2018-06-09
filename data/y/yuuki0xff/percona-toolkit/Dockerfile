FROM debian:stable  
LABEL maintainer "yuuki0xff <yuuki0xff@gmail.com>"  
  
ENV PERCONA_VERSION 3.0.6  
ENV RELEASE_VERSION 3.0.6-1  
  
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
rm -rf /var/tmp/* && \  
wget -O percona-toolkit.deb https://www.percona.com/downloads/percona-
toolkit/${PERCONA_VERSION}/binary/debian/stretch/x86_64/percona-
toolkit_${RELEASE_VERSION}.stretch_amd64.deb && \  
dpkg -i percona-toolkit.deb && \  
rm -f percona-toolkit.deb  

