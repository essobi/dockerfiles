FROM ruby:2.4  
MAINTAINER Andres Torres andres.torresduran@gmail.com  
# Install prerequisites  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y runit nginx nano nodejs
postgresql-client-9.4 libpq-dev && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Prepare application directory  
RUN mkdir /app  
WORKDIR /app  
ADD Gemfile /app/Gemfile  
ADD Gemfile.lock /app/Gemfile.lock  
RUN /bin/bash -c -l 'bundle install'  
ADD ./application /app  
ADD entrypoint.sh /app/entrypoint.sh  
# Adding scripts and configuration files  
ADD files/runit-bootstrap /usr/local/sbin/runit-bootstrap  
ADD files/runit-nginx-run /etc/service/nginx/run  
ADD files/nginx-app.conf /etc/nginx/sites-enabled/app.conf  
RUN rm /etc/nginx/sites-enabled/default  
  
# Set environment and expose port  
ENV RAILS_ENV development  
EXPOSE 80  
CMD ["/usr/local/sbin/runit-bootstrap"]  

