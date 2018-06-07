FROM docker.io/mysql:latest  
RUN echo deb http://ftp.it.debian.org/debian jessie main >
/etc/apt/sources.list  
  
# Prepare for nsswitch.  
RUN apt-get update && apt-get -y install libnss-extrausers && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN sed -i 's/passwd: compat/passwd: compat extrausers/' /etc/nsswitch.conf  
RUN grep -v mysql /etc/passwd > /var/lib/extrausers/passwd  
RUN touch /var/lib/extrausers/passwd && chmod a+w /var/lib/extrausers/passwd  
  
RUN mkdir -p /data/mysql  
RUN chmod 777 -R /data/mysql /var/lib/mysql /var/run  
  
COPY docker-entrypoint.sh /usr/local/bin/  
  
USER 27  
ENTRYPOINT /usr/local/bin/docker-entrypoint.sh  

