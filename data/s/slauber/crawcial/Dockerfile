FROM java:8-jdk  
  
MAINTAINER Sebastian Lauber <mail@crawcial.de>  
  
# Install Maven, clone Crawcial repository and add start up / update script  
# -------------------------------------------------------------------------  
WORKDIR /data  
RUN apt-get update && apt-get upgrade -y && apt-get install maven -y --no-
install-recommends && apt-get autoclean -y  
ADD start.sh /start.sh  
RUN chmod 555 /start.sh && cd /data && git clone
https://github.com/slauber/crawcial  
  
# Default command to run on container boot  
ENTRYPOINT ["/start.sh"]  
  
# Expose HTTPS  
EXPOSE 8443  
# Expose HTTP (do not use for anything but Facebook Callbacks!)  
EXPOSE 8080

