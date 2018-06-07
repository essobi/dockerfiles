FROM phusion/passenger-full:0.9.22  
MAINTAINER Martin Fenner "mfenner@datacite.org"  
# Set correct environment variables  
ENV HOME /home/app  
  
# Allow app user to read /etc/container_environment  
RUN usermod -a -G docker_env app  
  
# Use baseimage-docker's init process  
CMD ["/sbin/my_init"]  
  
# Install Ruby 2.4.1  
RUN bash -lc 'rvm --default use ruby-2.4.1'  
  
# Update installed APT packages, clean up when done  
RUN apt-get update && \  
apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \  
apt-get install ntp wget -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install phantomjs  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
&& \  
bzip2 -d phantomjs-2.1.1-linux-x86_64.tar.bz2 && \  
tar -xvf phantomjs-2.1.1-linux-x86_64.tar && \  
cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/phantomjs  
  
# Remove unused SSH service  
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh  
  
# Enable Passenger and Nginx and remove the default site  
# Preserve env variables for nginx  
RUN rm -f /etc/service/nginx/down && \  
rm /etc/nginx/sites-enabled/default  
COPY vendor/docker/webapp.conf /etc/nginx/sites-enabled/webapp.conf  
COPY vendor/docker/00_app_env.conf /etc/nginx/conf.d/00_app_env.conf  
  
# send logs to STDOUT and STDERR  
RUN ln -sf /dev/stdout /var/log/nginx/access.log && \  
ln -sf /dev/stderr /var/log/nginx/error.log  
  
# Use Amazon NTP servers  
COPY vendor/docker/ntp.conf /etc/ntp.conf  
  
# Copy webapp folder  
COPY . /home/app/webapp/  
RUN mkdir -p /home/app/webapp/tmp/pids && \  
mkdir -p /home/app/webapp/vendor/bundle && \  
chown -R app:app /home/app/webapp && \  
chmod -R 755 /home/app/webapp  
  
# Install npm and bower packages  
WORKDIR /home/app/webapp/vendor  
RUN /sbin/setuser app npm install  
  
# Install Ruby gems  
WORKDIR /home/app/webapp  
RUN gem install bundler && \  
/sbin/setuser app bundle install --path vendor/bundle  
  
# Add Runit script for sidekiq workers  
RUN mkdir /etc/service/sidekiq  
ADD vendor/docker/sidekiq.sh /etc/service/sidekiq/run  
  
# Run additional scripts during container startup (i.e. not at build time)  
RUN mkdir -p /etc/my_init.d  
COPY vendor/docker/70_precompile.sh /etc/my_init.d/70_precompile.sh  
COPY vendor/docker/80_cron.sh /etc/my_init.d/80_cron.sh  
COPY vendor/docker/90_migrate.sh /etc/my_init.d/90_migrate.sh  
COPY vendor/docker/100_flush_cache.sh /etc/my_init.d/100_flush_cache.sh  
  
# Expose web  
EXPOSE 80  

