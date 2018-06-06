FROM zans/discourse_docker_base  
  
MAINTAINER Zenon Skuza  
  
# Add samsaffron's configs and run  
RUN mkdir /config  
RUN mkdir /config/samples  
RUN mkdir /config/templates  
  
ADD /samples/* /config/samples/  
  
ADD /templates/* /config/templates/  
  
ADD /launcher /  
  
VOLUME /config  
  
# Install Plex  
#ADD install.sh /  
#RUN bash /install.sh

