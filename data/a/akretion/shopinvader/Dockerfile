FROM phusion/passenger-ruby24:0.9.23  
# Set correct environment variables.  
ENV HOME /root  
  
  
# Use baseimage-docker's init process.  
CMD ["/sbin/my_init"]  
RUN DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get install -y imagemagick && \  
apt-get upgrade -y -o Dpkg::Options::="--force-confold" && \  
apt-get clean  
RUN rm -f /etc/service/nginx/down  
RUN rm /etc/nginx/sites-enabled/default  
ADD webapp.conf /etc/nginx/sites-enabled/webapp.conf  
ADD rails.conf /etc/nginx/main.d/rails.conf  
RUN mkdir /home/app/webapp  
ADD . /home/app/webapp  
WORKDIR /home/app/webapp  
RUN bundle install --without development && mkdir -p tmp log && chown
9999:9999 tmp log  
RUN bundle exec rake assets:precompile  
RUN rm -rf log/* tmp/*  

