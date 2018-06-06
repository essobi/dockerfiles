FROM briceburg/node:6  
  
ENV \  
APP_NAME="cop" \  
APP_REPO="https://github.com/jasmith590/COP.git"  
  
# APPLICATION INSTALLATION  
###########################  
  
# clone app  
RUN git clone ${APP_REPO} /var/$APP_NAME && \  
cd /var/$APP_NAME && npm install  
  
# IMAGE RUNTIME  
###############  
  
ENTRYPOINT ["/var/cop/bin/cop"]  

