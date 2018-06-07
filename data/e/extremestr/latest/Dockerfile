FROM ubuntu:latest  
MAINTAINER beta  
  
# Install components  
RUN useradd -m -s /bin/nologin deluge  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get -qyy install
apache2 deluged deluge-webui && apt-get clean  
# RUN sudo apt-get -y install apache2  
RUN touch /var/log/deluged.log  
RUN touch /var/log/deluge-web.log  
RUN chown deluge:deluge /var/log/deluge*  
# RUN sudo apt-get -y install deluged  
# RUN sudo apt-get -y install deluge-webui  
ADD default /etc/  
ADD init.d /etc/  
COPY settings.sh /usr/sbin/  
  
WORKDIR /home/deluge  
  
# Expose ports  
EXPOSE 80  
EXPOSE 8112  
EXPOSE 58846  
EXPOSE 58847  
EXPOSE 58847/udp  
  
VOLUME /home/deluge  
CMD ["/usr/sbin/settings.sh"]  

