FROM centos:7  
EXPOSE 34197/udp  
  
WORKDIR /opt  
RUN mkdir -p /opt/factorio  
VOLUME /opt/factorio/saves  
  
RUN yum install -y wget  
  
ENV FACTORIO_VERSION 0.12.33  
COPY start-server.sh /opt/start-server.sh  
COPY config /opt/config  
  
# Download factorio headless server  
RUN wget --no-check-certificate -O
factorio_headless_x64_${FACTORIO_VERSION}.tar.gz https://www.factorio.com/get-
download/${FACTORIO_VERSION}/headless/linux64 && \  
tar xvzf factorio_headless_x64_${FACTORIO_VERSION}.tar.gz && \  
rm factorio_headless_x64_${FACTORIO_VERSION}.tar.gz  
  
CMD ["bash", "/opt/start-server.sh"]  

