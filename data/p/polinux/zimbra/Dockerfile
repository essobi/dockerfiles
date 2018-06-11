FROM million12/ssh  
MAINTAINER Przemyslaw Ozgo <linux@ozgo.info>  
  
ENV HOSTNAME=mail \  
DOMAIN=example.org \  
ATOM_SUPPORT=false  
  
RUN \  
rpm --rebuilddb && yum clean all && \  
yum install -y nmap-ncat sudo libidn gmp libaio libstdc++ unzip perl-core perl
sysstat sqlite rsyslog bind && \  
yum clean all  
  
ADD container-files/ /  
  
EXPOSE 25 110 143 389 456 587 993 995 7025 7071 7780 9071 80 443 10022  

