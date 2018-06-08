FROM phusion/baseimage:0.9.11  
MAINTAINER pinion <pinion@gmail.com>  
  
# Set correct environment variables.  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
RUN apt-get -q update  
  
# Install dependencies  
RUN apt-get install -qy wget python2.7  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python2.7 get-pip.py  
RUN pip install requests HTMLParser  
  
# wget the current master release  
RUN mkdir /opt/yoink  
RUN wget https://github.com/phracker/yoink/archive/master.tar.gz  
RUN tar -xvf master.tar.gz -C /opt/yoink --strip-components=1  
RUN ls /opt/yoink  
  
VOLUME /root  
VOLUME /blackhole  
VOLUME /media  
  
# Add run.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD yoink.sh /etc/my_init.d/yoink.sh  
RUN chmod +x /etc/my_init.d/yoink.sh  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

