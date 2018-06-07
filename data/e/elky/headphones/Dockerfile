FROM phusion/baseimage:0.9.22  
ENV DEBIAN_FRONTEND noninteractive  
  
# Set correct environment variables  
ENV HOME /root  
  
# Use baseimage-docker's init system  
CMD ["/sbin/my_init"]  
  
# Fix a Debianism of the nobody's uid being 65534  
RUN usermod -u 99 nobody  
RUN usermod -g 100 nobody  
  
RUN apt-get update -q  
  
# Install Dependencies  
RUN apt-get install -qy python git-core ffmpeg  
  
# Install Headphones  
RUN git clone -b develop https://github.com/rembo10/headphones.git
/opt/headphones  
RUN chown -R nobody:users /opt/headphones  
  
EXPOSE 8181  
# Headphones Configuration  
VOLUME /config  
  
# Headphones music  
VOLUME /music  
  
# Headphones downloads  
VOLUME /downloads  
  
# Add headphones to runit  
RUN mkdir /etc/service/headphones  
ADD headphones.sh /etc/service/headphones/run  
RUN chmod +x /etc/service/headphones/run

