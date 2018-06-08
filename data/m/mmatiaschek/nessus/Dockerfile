FROM debian:jessie  
  
MAINTAINER Markus Matiaschek <mmatiaschek@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y wget && \  
rm -rf /var/lib/apt/lists/*  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV NESSUS_VERSION 6.9.1  
RUN wget -O /tmp/Nessus-$NESSUS_VERSION-debian6_amd64.deb \  
"https://downloads.nessus.org/nessus3dl.php?file=Nessus-$NESSUS_VERSION-
debian6_amd64.deb&licence_accept=yes&t=13db91cbbc71883a269783312ead0aef"  
  
RUN dpkg -i /tmp/Nessus-$NESSUS_VERSION-debian6_amd64.deb  
  
# persistent volumes currently don't work :(  
#VOLUME /opt/nessus/etc/  
#VOLUME /opt/nessus/var/  
EXPOSE 8834  
ENTRYPOINT [ "/opt/nessus/sbin/nessusd" ]

