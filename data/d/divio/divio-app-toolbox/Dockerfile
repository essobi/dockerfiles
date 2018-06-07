FROM divio/base:4.5-py3.6-alpine3.6  
COPY stack /stack/base  
RUN chmod +x /stack/base/install.sh  
RUN /stack/base/install.sh  
  
RUN mkdir -p /etc/divio && ssh-keyscan $(getent hosts git.divio.com | awk
'{print $2 "," $1}') > /etc/divio/known_hosts  
  
ENTRYPOINT ["/bin/bash", "-c"] # TODO: Kill it with fire  

