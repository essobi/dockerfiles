################################################################################  
# Base image  
################################################################################  
  
FROM andrewmclagan/nginx-hhvm  
  
MAINTAINER "Ahmed Adel" <a.azab@neutrinos.io>  
  
################################################################################  
# Update Composer  
################################################################################  
  
RUN composer self-update  
  
RUN composer global require "laravel/installer"  
  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
  
EXPOSE 80 443  
  
CMD ["/usr/bin/supervisord"]  

