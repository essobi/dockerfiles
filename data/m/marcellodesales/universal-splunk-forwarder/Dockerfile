FROM outcoldman/splunk:6.2.4-forwarder  
MAINTAINER Marcello_deSales@intuit.com  
  
# Use the root user by default  
ENV SPLUNK_USER=root  
ENV SPLUNK_GROUP=root  
  
# Copy the default config files for the service  
COPY ./etc-system-local /tmp/splunk  
  
# Copy the custom entrypoint that replaces envs  
# https://github.com/outcoldman/docker-
splunk/blob/master/universalforwarder/Dockerfile#L53  
# Replaces FORWARDER_HOSTNAME and SPLUNK_INDEX  
COPY ./patch-entrypoint.sh /sbin/entrypoint.sh  

