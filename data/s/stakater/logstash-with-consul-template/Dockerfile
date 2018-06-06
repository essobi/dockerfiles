FROM stakater/logstash:5.2  
LABEL authors="Hazim <hazim_malik@hotmail.com>"  
  
# setting a default value to make it work on dockerhub  
ARG CONSUL_TEMPLATE_VERSION=0.18.0  
# Create config dir if it does not exist and  
# remove all default configurations from Logstash if any  
RUN mkdir -p /config-dir \  
&& rm -rf /config-dir/*  
  
# we define an environment variable with the location of our Consul cluster.
By default, it will try to resolve to  
# consul:8500 which would be the behavior if we have Consul running as a
container in the same host and we link it to this  
# Logstash container (with the alias consul, of course). But this environment
variable can also be overridden when we run the  
# container if we want to point somewhere else.  
ENV CONSUL_URL consul:8500  
# download the latest version of Consul Template and we put it on
/usr/local/bin  
ADD https://releases.hashicorp.com/consul-
template/${CONSUL_TEMPLATE_VERSION}/consul-
template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip /usr/bin/  
RUN unzip /usr/bin/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip
&& \  
mv consul-template /usr/local/bin/consul-template &&\  
rm -rf /usr/bin/consul-template_${CONSUL_TEMPLATE_VERSION}_linux_amd64.zip  
  
# we define a volume /templates, which is where we will mount our template
files from the host. This way we can reuse  
# the same image for different services and templates.  
VOLUME /templates  
  
# our container will expose port 5044 & 9600, where Logstash will be running  
EXPOSE 5044 9600  
# Make daemon service dir for filebeat if it doesn't exist, and empty service
directory for filebeat if it already contains a daemon file  
RUN mkdir -p /etc/service/logstash && rm -rf /etc/service/logstash/*  
  
# Add daemon service for filebeat-with-consul  
ADD start.sh /etc/service/logstash/run  
  
# Use base image's entrypoint  

