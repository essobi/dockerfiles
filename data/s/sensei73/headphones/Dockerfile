FROM phusion/baseimage:0.9.15  
MAINTAINER needo <sensei73@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody \  
&& usermod -g 100 nobody  
  
# Install Dependencies & Dependencies  
RUN apt-get update -q \  
&& apt-get install -qy python git  
&& apt-get clean  
  
# Install headphones  
RUN mkdir /opt/headphones  
&& git clone https://github.com/rembo10/headphones.git /opt/headphones \  
&& chown nobody:users /opt/headphones  
  
EXPOSE 8181  
# headphones Configuration  
VOLUME /config  
  
# Downloads directory  
VOLUME /downloads  
  
# Music directory  
VOLUME /music  
  
# Add edge.sh to execute during container startup & Add headphones to runit  
RUN mkdir -p /etc/my_init.d \  
&& mkdir -p /etc/service/headphone  
ADD edge.sh /etc/my_init.d/edge.sh  
ADD headphones.sh /etc/service/headphones/run  
RUN chmod +x /etc/my_init.d/edge.sh \  
&& chmod +x /etc/service/headphones/run  

