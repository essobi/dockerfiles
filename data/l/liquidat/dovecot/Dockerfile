FROM centos:centos7  
MAINTAINER liquidat, liquidat@bayz.de  
  
# update yum and install dovecot  
RUN yum -y update && yum -y install dovecot dovecot-pigeonhole && yum clean
all  
  
# add vmail user  
RUN groupadd -g 5000 vmail  
RUN echo "vmail:x:5000:5000::/home/vmail:/sbin/nologin" >> /etc/passwd  
RUN mkdir /home/vmail /var/lib/dovecot/sieve/  
RUN chown vmail:vmail /home/vmail/  
RUN chown root:root /var/lib/dovecot/sieve/  
# compile gobal sieve rule  
ADD default.sieve /var/lib/dovecot/sieve/default.sieve  
RUN /usr/bin/sievec /var/lib/dovecot/sieve/default.sieve  
# add docker entrypoint script to apply necessary dynamic changes  
ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
# start dovecot when container is started  
ENTRYPOINT ["sh","-c","/usr/local/bin/docker-entrypoint.sh"]  
  
EXPOSE 24 993 995 4190  

