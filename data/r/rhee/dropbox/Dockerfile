FROM rhee/unpam-centos-6  
MAINTAINER Sang-Hoon RHEE <shr386+github@hotmail.com>  
  
# dumb-init  
COPY dumb-init_1.0.1_amd64 /dumb-init  
RUN chmod 755 /dumb-init  
  
# start script  
COPY start.sh /  
RUN chmod 755 /start.sh  
COPY status /  
RUN chmod 755 /status  
  
# wrapper  
ADD https://www.dropbox.com/download?dl=packages/dropbox.py /dropbox.py  
#COPY copy-2016-06-14/dropbox.py /dropbox.py  
RUN chmod 755 /dropbox.py  
  
# https://www.dropbox.com/ko/install?os=lnx  
ADD https://www.dropbox.com/download?plat=lnx.x86_64 /tmp/dropbox.tar.gz  
#COPY copy-2016-06-14/dropbox-plat-lnx.x86_64.tar.gz /tmp/dropbox.tar.gz  
RUN tar xz -f /tmp/dropbox.tar.gz -C / ; chmod -R 755 /.dropbox-dist ; rm -f
/tmp/dropbox.tar.gz  
  
EXPOSE 17500  
VOLUME ["/dbox/.dropbox", "/dbox/Dropbox"]  
  
CMD [ "/dumb-init", "/start.sh" ]  

