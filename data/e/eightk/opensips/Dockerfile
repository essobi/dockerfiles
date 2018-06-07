FROM debian  
MAINTAINER Eightk <company@eigh.tk>  
  
ENV DBENGINE=DBTEXT  
  
##install opensips  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 049AD65B && echo
"deb http://apt.opensips.org jessie 2.3-releases" >>/etc/apt/sources.list \  
&& apt-get update && apt-get install -y opensips opensips-http-modules  
#&& touch /var/run/opensips.pid  
##configure db  
COPY conf /etc/opensips  
RUN opensipsdbctl create  
  
EXPOSE 8888 5060/udp  
USER opensips  
CMD opensips -f /etc/opensips/opensips.cfg -w /var/tmp -P /run/opensips.pid  
##TODO split in two containers  

