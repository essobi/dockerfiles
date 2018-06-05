FROM ubuntu:xenial  
  
ENV NIMBLE_VERSION=3.4.0-3  
## Install nimble and move all config files to /etc/nimble.conf  
##  
RUN echo "deb http://nimblestreamer.com/ubuntu xenial/" >
/etc/apt/sources.list.d/nimblestreamer.list \  
&& apt-key adv --fetch-keys http://nimblestreamer.com/gpg.key \  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y nimble=$NIMBLE_VERSION \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& mkdir -p /var/log/nimble && ln -sf /dev/stdout /var/log/nimble/nimble.log \  
&& cp /etc/nimble/nimble.conf /etc/nimble.conf.default \  
&& rm -f /etc/nimble/* \  
&& chown -R nimble:root /etc/nimble  
  
## Configuration volume  
##  
VOLUME /etc/nimble  
  
## Cache volume  
##  
VOLUME /var/cache/nimble  
  
EXPOSE 1935 8081  
USER nimble  
  
COPY start /  
  
CMD ["/start"]  

