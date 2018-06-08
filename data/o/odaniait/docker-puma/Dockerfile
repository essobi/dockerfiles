FROM odaniait/docker-base:ubuntu  
MAINTAINER Mike Petersen <mike@odania-it.de>  
  
# Create app user  
RUN addgroup --gid 9999 app  
RUN adduser --uid 9999 --gid 9999 --disabled-password --gecos "Application"
app  
RUN usermod -L app  
  
# Prepare nginx  
RUN apt-get update && apt-get install -y nginx && apt-get clean && rm -rf
/var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN sed -i -e 's/# server_names_hash_bucket_size
64;/server_names_hash_bucket_size 64;/' /etc/nginx/nginx.conf  
RUN sed -i -e 's/user www-data;/# user www-data;/' /etc/nginx/nginx.conf  
RUN rm /var/log/nginx/access.log && ln -sf /dev/stdout
/var/log/nginx/access.log  
RUN rm /var/log/nginx/error.log && ln -sf /dev/stderr /var/log/nginx/error.log  
RUN touch /run/nginx.pid  
RUN chown app:app /run/nginx.pid  
RUN chown -R app:app /var/lib/nginx/  
  
# Prepare /srv directory  
RUN mkdir -p /srv/app  
RUN mkdir -p /srv/.ssh  
RUN chmod 700 /srv/.ssh  
RUN chown app:app /srv/.ssh  
RUN chown -R app:app /srv  
ENV HOME /srv  
WORKDIR /srv/app  
  
# Add startup script  
COPY startup.sh /startup.sh  
COPY default.conf /etc/nginx/sites-enabled/default  
RUN chown -R app:app /startup.sh  
  
CMD '/startup.sh'  
EXPOSE 3000  
USER app  

