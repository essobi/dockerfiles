FROM base  
MAINTAINER Ladislav Prskavec <ladislav@prskavec.net>  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install curl apache2
libapache2-mod-php5 vim-tiny  
RUN chown -R www-data:www-data /var/www/  
EXPOSE 80  
EXPOSE 22  
CMD ["/bin/bash"]  

