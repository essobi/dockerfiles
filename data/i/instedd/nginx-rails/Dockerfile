FROM ruby:2.3  
# Install prerequisites  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y runit nginx nodejs && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Prepare application directory  
RUN mkdir /app  
WORKDIR /app  
  
# Adding scripts and configuration files  
ADD files/runit-bootstrap /usr/local/sbin/runit-bootstrap  
ADD files/runit-nginx-run /etc/service/nginx/run  
ADD files/nginx-app.conf /etc/nginx/sites-enabled/app.conf  
RUN rm /etc/nginx/sites-enabled/default  
  
# Set environment and expose port  
ENV RAILS_ENV production  
EXPOSE 80  
CMD ["/usr/local/sbin/runit-bootstrap"]  

