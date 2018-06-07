FROM debian:testing  
LABEL maintainer Tonnerre LOMBARD <tonnerre@ancient-solutions.com>  
  
RUN apt-get -q -y update && apt-get -q -y -o Dpkg::Options::=--force-confdef
-o Dpkg::Options::=--force-confold --purge install bind9-host tcpdump
traceroute  

