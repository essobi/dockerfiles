FROM debian:latest  
  
MAINTAINER treadie.io  
  
ENV LICENCE AddYourLicenceHere  
  
RUN apt-get update && apt-get install -y wget  
RUN wget -O nessus.deb --user-agent='Mozillqa/5.0 (Windows NT 10.0; WOW64;
rv:48.0) Gecko/20100101 Firefox/48.0' \--header='Upgrade-Insecure-Requests: 1'
'http://downloads.nessus.org/nessus3dl.php?file=Nessus-6.10.7-debian6_amd64.deb&licence_accept=yes&t=c1318602f47f498479483ca3a64a0ff5'  
RUN dpkg -i nessus.deb && rm nessus.deb  
  
EXPOSE 8834  
ENTRYPOINT ["/opt/nessus/sbin/nessusd"]  
  
VOLUME ["/opt/nessus/etc/nessus/"]  

