FROM lysender/ubuntu-php  
MAINTAINER Leonel Baer <leonel@lysender.com>  
  
RUN apt-get -y install git pwgen && apt-get clean  
  
# Configure servicies  
ADD ./deploy.sh /deploy.sh  
RUN chmod 0775 /deploy.sh  
  
VOLUME ["/var/www/html", "/root/.ssh"]  
  
CMD ["/bin/bash", "/deploy.sh"]  
  

