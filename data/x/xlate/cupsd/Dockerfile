FROM ubuntu:17.10  
MAINTAINER Michael Edgar <michael@xlate.io>  
  
RUN apt update && \  
apt-get install \  
\--assume-yes \  
\--no-install-recommends \  
cups \  
cups-bsd \  
printer-driver-all && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY cupsd.conf /etc/cups/  
  
EXPOSE 631  
  
CMD [ "/usr/sbin/cupsd", "-f" ]  

