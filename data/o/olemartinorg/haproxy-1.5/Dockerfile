#  
# Haproxy Dockerfile  
#  
# https://github.com/olemartinorg/haproxy-1.5  
#  
# Pull base image.  
FROM dockerfile/ubuntu  
  
# These are the only two lines i should need to change from the official
dockerfile/haproxy:  
RUN apt-add-repository --yes ppa:vbernat/haproxy-1.5  
RUN apt-get update  
  
# Install Haproxy.  
RUN \  
apt-get install -y haproxy && \  
sed -i 's/^ENABLED=.*/ENABLED=1/' /etc/default/haproxy  
  
# Add files.  
ADD haproxy.cfg /etc/haproxy/haproxy.cfg  
ADD start.bash /haproxy-start  
  
# Define mountable directories.  
VOLUME ["/data", "/haproxy-override"]  
  
# Define working directory.  
WORKDIR /etc/haproxy  
  
# Define default command.  
CMD ["bash", "/haproxy-start"]  
  
# Expose ports.  
EXPOSE 80  
EXPOSE 443  

