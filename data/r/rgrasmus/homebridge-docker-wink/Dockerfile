FROM nodesource/jessie  
#FROM nodesource/jessie:5.8.0  
MAINTAINER Christian Brandlehner <christian@brandlehner.at>  
  
##################################################  
# Set environment variables #  
##################################################  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TERM xterm  
  
##################################################  
# Install tools #  
##################################################  
  
RUN apt-get update  
RUN apt-get install -y apt-utils  
RUN apt-get install -y apt-transport-https  
RUN apt-get install -y locales  
RUN apt-get install -y curl wget git python build-essential make g++ libavahi-
compat-libdnssd-dev libkrb5-dev vim net-tools nano  
RUN curl -L https://deb.nodesource.com/setup_5.x | bash - && \  
apt-get install -y nodejs  
  
RUN alias ll='ls -alG'  
  
# Install Homebridge  
##################################################  
RUN npm install -g homebridge --unsafe-perm  
  
# Final settings  
##################################################  
COPY avahi-daemon.conf /etc/avahi/avahi-daemon.conf  
  
USER root  
RUN mkdir -p /var/run/dbus  
  
ADD image/run.sh /root/run.sh  
  
# Run container  
##################################################  
EXPOSE 5353 51826  
CMD ["/root/run.sh"]  

