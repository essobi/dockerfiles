FROM ubuntu:16.04  
MAINTAINER Fabian Köster <fabian.koester@bringnow.com>  
  
# Install runtime dependencies  
RUN export DEBIAN_FRONTEND=noninteractive && apt-get update -qq && apt-get
install -qq -y --no-install-recommends git openssh-client cron  
  
# Install scripts  
COPY sync.sh entrypoint.sh /usr/local/bin/  
  
VOLUME /root/.ssh  
VOLUME /sync-dir  
  
# Run the command on container startup  
ENTRYPOINT ["entrypoint.sh"]  

