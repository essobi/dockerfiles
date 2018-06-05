FROM debian:stable  
LABEL maintainer Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
RUN apt-get -q -y update  
RUN apt-get -q -y -o Dpkg::Options::=--force-confdef -o
Dpkg::Options::=--force-confold --purge install git libfile-slurp-perl libnet-
dns-perl perl perl-base  
  
RUN /usr/bin/git clone https://github.com/tonnerre/dnsutils/  
  
VOLUME ["/dns"]  
  
COPY ["fetch-regularly.sh", "/root/fetch-regularly.sh"]  
  
CMD ["/bin/sh", "-x", "/root/fetch-regularly.sh"]  

