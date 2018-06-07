FROM node:6  
MAINTAINER Roman Atachiants "roman@misakai.com"  
# Make sure we have git  
RUN apt-get update -qq && apt-get install -y git  
  
# Application will be in app folder  
WORKDIR /app  
ADD deploy.sh /  
  
# Expose healtcheck port  
EXPOSE 5000  
# Volumes for faster deploy  
VOLUME /app  
CMD ["/bin/bash", "/deploy.sh"]

