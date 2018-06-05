#  
# Nasqueron - Jenkins slave Docker image, not customized  
#  
  
FROM debian:jessie  
MAINTAINER Sébastien Santoro aka Dereckson <dereckson+nasqueron-docker@espace-
win.org>  
  
#  
# Prepare the container  
#  
  
RUN apt-get update && apt-get install -y \  
openjdk-7-jdk ant openssh-server openssh-client locales \  
\--no-install-recommends && rm -r /var/lib/apt/lists/* && \  
mkdir -p /var/run/sshd && \  
sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
echo 'LANG="en_US.UTF-8"' > /etc/default/locale && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
#  
# Docker properties  
#  
  
ENV LANG en_US.UTF-8  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

