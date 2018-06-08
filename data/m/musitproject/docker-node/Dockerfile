FROM library/node:7  
# Install locales package  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive && \  
apt-get install -y locales apt-transport-https ca-certificates software-
properties-common  
  
# Set locale to be en_US.UTF-8  
RUN \  
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"'>/etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
  
# Set the LANG environment  
ENV LANG en_US.UTF-8  
# Install docker-engine  
RUN \  
curl -fsSL https://yum.dockerproject.org/gpg | apt-key add - && \  
add-apt-repository "deb https://apt.dockerproject.org/repo/
debian-$(lsb_release -cs) main" && \  
apt-get update && \  
apt-get -y install docker-engine  
  
# Define working directory  
WORKDIR /root

