FROM ubuntu:trusty  
MAINTAINER Alan Franzoni <username@franzoni.eu>  
COPY *.deb /tmp/  
RUN dpkg -i /tmp/*.deb && rm -f /tmp/*.deb  
RUN /bin/echo -e
"MAXDELTA=3600\nCLEANUP_DOWNLOADED_PACKAGES=\"true\"\nCLEANUP_DOWNLOADED_LISTS=\"false\""
> /etc/apt-current.conf  
RUN apt-get-current -y install apt-transport-https bash-completion ca-
certificates curl \  
dnsutils groff-base info install-info lsof ltrace man-db manpages strace
tcpdump time unzip vim wget  
RUN apt-get-current -y dist-upgrade  

