FROM ubuntu:14.04  
MAINTAINER Firestack <me@stackfire.io>  
  
# Install required packages  
RUN apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
ca-certificates \  
wget \  
apt-transport-https \  
vim \  
nano \  
python3 \  
python3-pip \  
git \  
python3-psycopg2  
  
  
  
# Copy assets  
COPY assets/ /assets/  
RUN /assets/setup.sh  
  
# Allow to access embedded tools  
# ENV PATH /opt/gitlab/embedded/bin:/opt/gitlab/bin:/assets:$PATH  
# Resolve error: TERM environment variable not set.  
# ENV TERM xterm  
# Expose web  
EXPOSE 8443 8080  
# Define data volumes  
VOLUME ["/etc/maskoftruth", "/var/log/maskoftruth"]  
  
# Wrapper to handle signal, trigger runit and reconfigure GitLab  
CMD ["/assets/start.sh"]  

