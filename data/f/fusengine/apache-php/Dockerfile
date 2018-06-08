FROM fusengine/apaxy:ubuntu-apaxy  
LABEL maintainer="Fusengine <info@fusengine.ch>"  
  
# Add data to osx  
RUN usermod -u 1000 www-data  
  
# Add script install php  
COPY setup/php /root/.install_php  
RUN chmod +x /root/.install_php  
  
# link adminer  
COPY setup/header.html /app/theme  
  
# Run script install php if "sh /root/.install_php" or "./root/.install_php"
--->  
# --> not run write "bash /root/.install_php"  
RUN bash /root/.install_php  
  
# Volume  
VOLUME ["/etc/apache2/sites-enabled", "/var/log/apache2", "/app/web"]  
  
# WORKDIR  
WORKDIR /app/web  
  
EXPOSE 80  

