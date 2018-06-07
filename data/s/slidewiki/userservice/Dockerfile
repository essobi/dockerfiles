FROM node:6.11-slim  
MAINTAINER Kurt Junghanns <kjunghanns@informatik.uni-leipzig.de>  
  
RUN mkdir /nodeApp  
WORKDIR /nodeApp  
  
# --------------------- #  
# Installation Cron #  
# --------------------- #  
RUN apt-get update  
RUN apt-get install -y cron supervisor  
  
# ----------------------- #  
# Installation NodeJS #  
# ----------------------- #  
ADD ./application/ ./  
RUN npm install --production  
  
# ---------------------- #  
# Configuration Cron #  
# ---------------------- #  
RUN mkdir -p /var/log/supervisor && touch /var/log/cron.log  
  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Add crontab file in the cron directory  
ADD crontab /etc/cron.d/simple-cron  
ADD application/cleanup.sh /cleanup.sh  
  
RUN chmod +x /cleanup.sh && chmod 0644 /etc/cron.d/simple-cron  
  
# ----------- #  
# Cleanup #  
# ----------- #  
RUN apt-get autoremove -y && apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
# -------- #  
# Run! #  
# -------- #  
Entrypoint []  
CMD supervisord  

