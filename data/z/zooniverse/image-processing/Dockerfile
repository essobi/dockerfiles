FROM node:0.12  
RUN apt-get update && \  
apt-get install -y imagemagick graphicsmagick cron tmpreaper supervisor && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /node_app  
  
COPY im_config/policy.xml /etc/ImageMagick-6/policy.xml  
  
COPY docker/supervisor.conf /etc/supervisor/conf.d/static_crop.conf  
COPY docker/static_crop_cron /etc/cron.d/static_crop_cron  
COPY . /node_app  
  
RUN mkdir -p /node_app/log && \  
chmod 0644 /etc/cron.d/static_crop_cron && \  
touch /var/log/cron.log && \  
npm install .  
  
EXPOSE 8080  
ENTRYPOINT /usr/bin/supervisord  

