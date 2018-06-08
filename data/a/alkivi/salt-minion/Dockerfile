FROM debian:stretch  
  
ARG version=2017.7  
ENV VERSION $version  
  
# Install salt  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y wget apt-utils gnupg && \  
wget -O - https://repo.saltstack.com/apt/debian/9/amd64/latest/SALTSTACK-GPG-
KEY.pub | apt-key add - && \  
echo "deb http://repo.saltstack.com/apt/debian/9/amd64/${VERSION} stretch
main" > /etc/apt/sources.list.d/saltstack.list && \  
DEBIAN_FRONTEND=noninteractive apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y salt-minion  
  
# Clean image  
RUN apt-get -yqq clean && \  
apt-get -yqq purge && \  
rm -rf /tmp/* /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
# Add config files  
COPY minion /etc/salt/  
  
# Entry point  
ADD start.sh /start.sh  
CMD ["bash", "start.sh"]  

