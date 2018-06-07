# Use phusion/baseimage as base image. To make your builds  
# reproducible, make sure you lock down to a specific version, not  
# to `latest`! See  
# https://github.com/phusion/baseimage-docker/blob/master/Changelog.md  
# for a list of version numbers.  
FROM phusion/baseimage:0.10.1  
# Set correct environment variables.  
ENV HOME /root  
  
# Update OS.  
RUN sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list  
RUN apt-get update  
  
# upgrade  
# RUN apt-get -y upgrade  
# Install basic packages.  
RUN apt-get install -y curl git htop unzip vim wget byobu make xz-utils sudo
file  
  
# Install Eclipse dependency packages  
RUN apt-get install -y openjdk-8-jdk libcanberra-gtk-module  
  
# Download and install Eclipse Oxygen  
RUN wget
http://eclipse.c3sl.ufpr.br/technology/epp/downloads/release/oxygen/3a/eclipse-
cpp-oxygen-3a-linux-gtk-x86_64.tar.gz -O /tmp/eclipse.tar.gz -q && \  
echo "Instaling Eclipse" && \  
tar -xf /tmp/eclipse.tar.gz -C /opt && \  
rm /tmp/eclipse.tar.gz  
  
# use bash instead of dash  
RUN echo "dash dash/sh boolean false" | debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive dpkg-reconfigure dash  
  
# Copy entrypoint script. Sets up Yocto SDK environment  
COPY run.sh /  
RUN chmod +x /run.sh  
  
# Create developer user  
RUN mkdir /home/developer && \  
echo "developer:x:1000:1000:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:1000:" >> /etc/group && \  
chown developer:developer -R /home/developer && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
USER developer  
ENV HOME /home/developer  
WORKDIR /home/developer  
  
ENTRYPOINT ["/run.sh"]  
CMD ["/opt/eclipse/eclipse"]  

