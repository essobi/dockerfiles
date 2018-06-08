From ubuntu:14.04  
MAINTAINER Javier Jerónimo <jjeronimo@packageper.com>  
  
#
################################################################################
Setup  
RUN apt-get update && apt-get -yq install postfix libsasl2-modules  
  
ADD etc/mailname /etc/mailname  
ADD etc/postfix/main.cf /etc/postfix/main.cf  
  
  
  
ADD pkgp-run.sh /pkgp-run.sh  
RUN chmod u+x /pkgp-run.sh  
  
EXPOSE 25  
  
#
################################################################################
Entry point  
CMD ["/pkgp-run.sh"]  

