FROM scorpil/rust  
USER root  
  
RUN apt-get update && apt-get install -y git libssl-dev libpcap-dev  
  
# Clean up.  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# Install the Arrow client.  
WORKDIR "/"  
RUN git clone https://github.com/angelcam/arrow-client  
WORKDIR "/arrow-client"  
RUN cargo build --release  
  
# Setup the Arrow client.  
RUN mkdir /etc/arrow && cp mjpeg-paths /etc/arrow/mjpeg-paths && cp rtsp-paths
/etc/arrow/rtsp-paths  
RUN mkdir /var/lib/arrow  
RUN mv /arrow-client/target/release/arrow-client /usr/bin  
RUN mv /arrow-client/ca.pem /etc/arrow  
WORKDIR "/"  
RUN rm -rf /arrow-client  
  
COPY run.sh /  
  
VOLUME ["/arrow-config"]  
  
CMD "/run.sh"  

