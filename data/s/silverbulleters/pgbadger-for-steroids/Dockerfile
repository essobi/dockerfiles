# Pull from the ubuntu:14.04 image  
FROM ubuntu:14.04  
# Set the author  
MAINTAINER team@silverbulleters.org  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update cache and install packages  
RUN apt-get update && apt-get -y install \  
software-properties-common \  
# python-software-properties \  
debian-archive-keyring \  
wget \  
curl \  
make \  
cron \  
supervisor \  
rsyslog  
  
# Download Nginx signing key  
RUN apt-key adv --recv-keys --keyserver keyserver.ubuntu.com C300EE8C  
  
# Add to repository sources list  
RUN add-apt-repository ppa:nginx/stable  
  
# Update cache and install Nginx  
RUN apt-get update && apt-get -y install \  
nginx  
  
RUN apt-get clean; \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /var/log/supervisor  
  
RUN sed -i 's/#cron/cron/g' /etc/rsyslog.d/50-default.conf  
  
# Turn off daemon mode  
# Reference: http://stackoverflow.com/questions/18861300/how-to-run-nginx-
within-docker-container-without-halting  
RUN echo "\ndaemon off;" >> /etc/nginx/nginx.conf  
  
# Run nginx and php-fpm as root  
RUN sed -i 's/www-data/root/g' /etc/nginx/nginx.conf  
  
# Backup the default configurations  
RUN mv /etc/nginx/sites-available/default /etc/nginx/sites-
available/default.original  
  
# Copy nginx site conf  
COPY nginx.conf /etc/nginx/sites-available/default  
  
# Remove default page  
RUN rm /var/www/html/index.nginx-debian.html  
  
# Copy the supervisord.conf file  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Add pgbadger  
ENV PGBGRVER=9.2  
ADD https://github.com/dalibo/pgbadger/archive/v${PGBGRVER}.tar.gz /tmp/  
  
WORKDIR /tmp/  
  
RUN tar xzf v${PGBGRVER}.tar.gz && \  
rm v${PGBGRVER}.tar.gz  
  
WORKDIR /tmp/pgbadger-${PGBGRVER}  
  
RUN perl Makefile.PL && make && make install  
  
RUN pgbadger --version  
  
COPY start_analyze.sh /usr/local/bin/start_analyze.sh  
  
# Copy the crontab file  
COPY start-pgbadger-cron /etc/cron.d/start-pgbadger-cron  
RUN chmod 0644 /etc/cron.d/start-pgbadger-cron  
  
# Mount volumes  
VOLUME ["/etc/nginx/certs", "/etc/nginx/conf.d", "/var/www/html"]  
  
# Boot up supervisord when container is started  
CMD ["/usr/bin/supervisord"]  
  
# Set the current working directory  
WORKDIR /var/www/html  
  
EXPOSE 80  

