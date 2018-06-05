FROM phusion/baseimage:latest  
  
MAINTAINER Mrunal Nachankar "mrunal4888@gmail.com"  
# set environment variable USER as ka-lite  
RUN export USER=ka-lite  
  
# Add ppa for ka-lite and install the same  
RUN echo "deb http://ppa.launchpad.net/learningequality/ka-lite/ubuntu `awk
-F'[= ]' '/VERSION_CODENAME=/{print $2}' /etc/os-release` main " >>
/etc/apt/sources.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3194DD81  
  
# Install the ka-lite and clean apt cache  
RUN apt-get update && apt-get install -y -q ka-lite net-tools \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/tmp/* \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add startup.sh to execute during startup  
RUN mkdir -p /etc/my_init.d  
COPY start_ka-lite.sh /etc/my_init.d/start_ka-lite.sh  
RUN chmod +x /etc/my_init.d/start_ka-lite.sh  
  
# Attach data volume - content, database and custom confs and data  
RUN mkdir -p /var/ka-lite/.kalite  
VOLUME /var/ka-lite/.kalite  
  
#expose port for https service  
EXPOSE 8008  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  

