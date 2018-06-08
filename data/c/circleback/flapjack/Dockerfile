FROM ubuntu:14.04  
MAINTAINER Circleback "http://circleback.com"  
# Fix for docker HUB  
RUN ln -s -f /bin/true /usr/bin/chfn  
  
RUN echo 'deb http://packages.flapjack.io/deb precise main' | sudo tee
/etc/apt/sources.list.d/flapjack.list  
RUN apt-get update -y  
RUN RUNLEVEL=1 DEBIAN_FRONTEND=noninteractive apt-get install -y --force-yes
supervisor redis-server flapjack nginx  
  
RUN mkdir -p /etc/flapjack /var/{run,log,lib}/flapjack  
  
ADD flapjack/flapjack_config.yaml.erb /etc/flapjack/  
ADD flapjack/nginx.conf /etc/nginx/nginx.conf  
ADD flapjack/supervisord.conf /etc/supervisor/conf.d/flapjack.conf  
ADD flapjack/run.sh /tmp/run.sh  
  
EXPOSE 80 3080 3081  
CMD ["/tmp/run.sh"]  

