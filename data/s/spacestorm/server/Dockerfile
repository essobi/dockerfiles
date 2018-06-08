FROM php:7.2.0  
#  
# Install dependencies  
#  
RUN apt-get update  
RUN apt-get install -y git  
  
ADD composer.json /server/  
WORKDIR /server  
  
#  
# Install PHP with required extensions for PMMP  
#  
RUN curl \  
https://jenkins.pmmp.io/job/PHP-7.2-Linux-x86_64/20/artifact/PHP_Linux-x86_64.tar.gz
\  
\--output linux.tar.gz  
RUN tar -zxf linux.tar.gz  
  
#  
# Install PHP  
#  
RUN bin/composer install  
  
#  
# Pull, install and configure PMMP server  
#  
RUN curl \  
https://jenkins.pmmp.io/job/PocketMine-MP/586/artifact/PocketMine-
MP_1.7dev-586_5f48433c_API-3.0.0-ALPHA10.phar \  
\--output PocketMine-MP.phar  
RUN cp vendor/pmmp/pocketmine-mp/start.sh .  
RUN chmod +x start.sh  
RUN touch en  
  
#  
# Install plugins  
#  
RUN mkdir plugins  
RUN curl \  
https://poggit.pmmp.io/r/18159/MOTDShuffle.phar \  
\--output /server/plugins/MOTDShuffle.phar  
  
EXPOSE 19132/TCP 19132/UDP  
#  
# Start PMMP server  
#  
CMD /server/start.sh --no-wizard  

