FROM tutum/mongodb  
MAINTAINER Javier Jerónimo <jjeronimo@packagepeer.com>  
  
# HowTo build: sudo docker build .  
  
# HowTo run: sudo docker run -e CONFIGDB=... -d packagepeer/mongos  
  
ADD pkgp-run.sh /pkgp-run.sh  
RUN chmod u+x /pkgp-run.sh  
  
#
################################################################################
Entry point  
CMD ["/pkgp-run.sh"]  

