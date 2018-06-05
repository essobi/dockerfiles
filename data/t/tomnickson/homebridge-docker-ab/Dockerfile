FROM alpine:3.3  
  
##################################################  
# Install tools #  
##################################################  
  
RUN apk update && apk add \  
nodejs \  
git \  
avahi-dev \  
make \  
g++ \  
&& rm -rf /var/cache/apk/*  
  
##################################################  
# Install homebridge #  
##################################################  
  
RUN npm install -g homebridge@0.3.4  
  
##################################################  
# Start #  
##################################################  
  
USER root  
  
RUN mkdir -p /var/run/dbus  
  
EXPOSE 5353 51826  
  
ADD install_plugins.sh /root/install_plugins.sh  
ADD run.sh /root/run.sh  
  
VOLUME ["/root/.homebridge"]  
CMD ["/root/run.sh"]  

