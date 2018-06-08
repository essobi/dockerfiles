################################################################################  
# #  
# {o,o} #  
# |)__) #  
# -"-"\- #  
# #  
################################################################################  
#  
# Apache docker image  
#  
##################################---BASE---####################################  
  
FROM pricepilotio/base:latest  
  
################################################################################  
  
################################---MAINTAINER---################################  
  
MAINTAINER Price pilot <hello@pricepilot.io>  
  
################################################################################  
  
ADD confs/alias.conf /etc/apache2/mods-enabled/alias.conf  
ADD www-data-limited-access.prepend.php /etc/php/7.0/cli/www-data-limited-
access.prepend.php  
ADD configure.sh configure.sh  
RUN chmod +x configure.sh; \  
sleep 5 && ./configure.sh; \  
rm configure.sh  
RUN echo "echo -e \"\e[0;31mWARNING\e[0m you are running as root user. exec
into the container with '-u www-data' instead. \n\" " >> /root/.bashrc  
  
################################################################################  
  
#################################---EXPOSE---###################################  
  
EXPOSE 80  
  
################################################################################  
  
#################################---COMMAND---##################################  
  
CMD apache2ctl -D FOREGROUND  
  
################################################################################  

