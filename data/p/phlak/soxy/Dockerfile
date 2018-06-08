FROM alpine:3.7  
MAINTAINER Chris Kankiewicz <Chris@ChrisKankiewicz.com>  
  
# Create non-root user  
RUN adduser -Ds /sbin/nologin soxy  
  
# Create key directory  
RUN mkdir -pv /vol/key \  
&& chown soxy:soxy -R /vol \  
&& chmod 700 /vol/key  
  
# Create Soxy SSH directory & config file  
# RUN mkdir -pv /home/soxy/.ssh  
COPY files/config /home/soxy/.ssh/config  
RUN chown soxy:soxy -R /home/soxy/.ssh \  
&& chmod 700 /home/soxy/.ssh \  
&& chmod 600 /home/soxy/.ssh/config  
  
# Create keygen command  
COPY files/keygen /usr/local/bin/keygen  
RUN chmod +x /usr/local/bin/keygen  
  
# Install OpenSSH Client  
RUN apk add --update openssh-client \  
&& rm -rf /var/cache/apk/*  
  
# Set running user  
USER soxy  
  
# Define volumes  
VOLUME /vol/key  
  
# Set the working dir  
WORKDIR /home/soxy  
  
# Set the entrypoint  
ENTRYPOINT ["ssh", "-v", "-C", "-N", "-D", "0.0.0.0:1080"]  

