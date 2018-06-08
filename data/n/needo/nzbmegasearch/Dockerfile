FROM phusion/baseimage:0.9.11  
MAINTAINER needo <needo@superhero.org>  
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
RUN apt-get install -qy wget python  
  
# Install nzbmegasearch v0.46  
RUN mkdir /opt/NZBmegasearch  
RUN wget -P /tmp/ https://github.com/pillone/usntssearch/archive/v0.46.tar.gz  
RUN tar -C /opt -xvf /tmp/v0.46.tar.gz --strip-components 1  
RUN chown -R nobody:users /opt/NZBmegasearch  
  
# Path to nzbmegasearch's custom_params.ini  
VOLUME /config  
  
# megasearch doesn't have a handy config file command line argument  
RUN ln -s /config/custom_params.ini /opt/NZBmegasearch/custom_params.ini  
  
EXPOSE 5000  
# Add edge.sh to execute during container startup  
RUN mkdir -p /etc/my_init.d  
ADD edge.sh /etc/my_init.d/edge.sh  
RUN chmod +x /etc/my_init.d/edge.sh  
  
# Add nzbmegasearch to runit  
RUN mkdir /etc/service/nzbmegasearch  
ADD nzbmegasearch.sh /etc/service/nzbmegasearch/run  
RUN chmod +x /etc/service/nzbmegasearch/run  

