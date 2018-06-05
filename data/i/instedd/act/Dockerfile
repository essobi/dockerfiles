FROM phusion/passenger-ruby21:0.9.12  
MAINTAINER Juan Edi <jedi@manas.com.ar>  
  
# Set correct environment variables.  
ENV HOME /root  
ENV RAILS_ENV production  
  
RUN rm -f /etc/service/nginx/down  
RUN rm /etc/nginx/sites-enabled/default  
  
# Install rsync  
RUN apt-get update && apt-get install -y rsync  
  
# Install node for NNDD  
RUN apt-get install -y nodejs  
  
# Tell npm to avoid using self-signed certificates (see
stackoverflow.com/a/22089950 )  
RUN npm config set ca ""  
  
# Install bower & grunt for NNDD  
RUN npm install -g bower grunt-cli  
  
# topojson for converting shapefiles for NNDD  
RUN npm install -g topojson  
  
# Prepare folders  
RUN mkdir /home/app/webapp  
  
# Copy configuration and init files  
ADD deploy/nginx-site.conf /etc/nginx/sites-enabled/webapp.conf  
ADD deploy/nginx-env.conf /etc/nginx/main.d/nginx-env.conf  
ADD deploy/rrsync /act/rrsync  
  
# /etc/my_init.d/00_regen_ssh_host_keys.sh present in base image  
ADD deploy/01_serve_ssh_public_key.sh /etc/my_init.d/  
ADD deploy/02_setup_sync_dir.sh /etc/my_init.d/  
ADD deploy/03_setup_sshd.sh /etc/my_init.d/  
ADD deploy/04_migrate_db.sh /etc/my_init.d/  
ADD deploy/05_precompile_assets.sh /etc/my_init.d/  
  
# Add background daemons  
RUN mkdir /etc/service/act-file-monitor /etc/service/act-keys-import  
ADD deploy/act-file-monitor.sh /etc/service/act-file-monitor/run  
ADD deploy/act-keys-import.sh /etc/service/act-keys-import/run  
  
RUN git clone https://github.com/instedd/notifiable-diseases /tmp/notifiable-
diseases  
WORKDIR /tmp/notifiable-diseases  
RUN gem install compass  
RUN npm install  
RUN bower --allow-root install  
ADD config/nndd-production-settings.json /tmp/notifiable-
diseases/conf/settings.local.json  
ADD config/nndd-production-custom.scss /tmp/notifiable-
diseases/conf/custom.local.scss  
RUN grunt build  
  
WORKDIR /home/app/webapp  
  
# Install bundle and copy app files  
ADD Gemfile /home/app/webapp/  
ADD Gemfile.lock /home/app/webapp/  
RUN bundle install --without development test  
ADD . /home/app/webapp  
  
RUN cp -r /tmp/notifiable-diseases/dist/nndd /home/app/webapp/public/nndd  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
VOLUME /etc/ssh  
VOLUME /act/sync  
  
EXPOSE 22  
EXPOSE 80  

