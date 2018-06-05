#  
# Docker ambassador pattern linking docker image  
#  
# http://github.com/tenstartups/ambassador-docker  
#  
FROM tenstartups/alpine:latest  
  
LABEL maintainer="Marc Lennox <marc.lennox@gmail.com>"  
  
# Set environment variables.  
ENV \  
AMBASSADOR_USER=ambassador \  
AUTOSSH_GATETIME=0 \  
CHAPERONE_CONFIG_DIR=/etc/chaperone.d \  
SOCAT_DEBUG_LEVEL=2 \  
SSH_AUTHORIZED_KEYS_FILE=/keys/host.pem.pub \  
SSH_CLIENT_ALIVE_INTERVAL=30 \  
SSH_DEBUG_LEVEL=0 \  
SSH_HOST_KEY_FILE=/keys/host.pem \  
SSH_LISTEN_PORT=22 \  
SSH_PORT=2222 \  
SSH_SERVER_ALIVE_INTERVAL=30 \  
TUNNEL_BIND_ADDRESS=0.0.0.0  
# Install packages.  
RUN \  
apk --update add autossh openssh python3 ruby ruby-bigdecimal ruby-json socat
sshpass && \  
rm -rf /var/cache/apk/*  
  
# Install ruby libraries.  
RUN \  
gem install activesupport awesome_print colorize --no-document  
  
# Install python libraries.  
RUN \  
pip3 install --upgrade pip && \  
pip3 install chaperone  
  
# Define working directory.  
WORKDIR /root  
  
# Add files to the container.  
COPY entrypoint.sh /docker-entrypoint  
COPY create_service_configs.rb /usr/local/bin/create_service_configs  
COPY logging.conf ${CHAPERONE_CONFIG_DIR}/logging.conf  
COPY service.conf.erb /usr/share/chaperone/service.conf.erb  
  
# Set the entrypoint script.  
ENTRYPOINT ["/docker-entrypoint"]  
  
# Expose ports.  
EXPOSE ${SSH_LISTEN_PORT}  

