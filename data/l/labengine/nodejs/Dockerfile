FROM labengine/ubuntu  
LABEL maintainer="Fusengine <info@fusengine.ch>"  
  
# add version nodejs  
ENV NODE_VERSION setup_9.x  
  
# Add buildpack  
COPY install-node.sh /root/install-node.sh  
RUN chmod 775 /root/install-node.sh  
  
# Run buildpack install and update  
RUN ./root/install-node.sh  
  
# Create directory  
RUN mkdir /data  
  
# Volume and workdir  
VOLUME ["/data"]  
WORKDIR /data  
  
# version Nodejs  
RUN echo Node Version && node --version  
RUN npm --version  

