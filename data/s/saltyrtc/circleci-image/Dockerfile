FROM openjdk:9-slim  
  
# Base dependencies  
RUN apt-get update -qqy \  
&& apt-get install -qqy --no-install-recommends \  
libsodium18 \  
libsodium-dev \  
python3 \  
python3-pip \  
python3-setuptools \  
python3-wheel \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# Add wrapper scripts  
ADD saltyrtc-server-launcher /usr/local/bin/saltyrtc-server-launcher  
RUN chmod +x /usr/local/bin/saltyrtc-server-launcher  
  
# Create test certificates  
ADD generate-cert.sh /saltyrtc/certs/generate-cert.sh  
RUN bash /saltyrtc/certs/generate-cert.sh && \  
chmod a+r /saltyrtc/certs/*  
  
# Update directory permissions  
RUN chmod a+w /saltyrtc  
  
# Install SaltyRTC server  
RUN pip3 install saltyrtc.server[logging]  
  
# Export SaltyRTC test permanent key  
ENV
SALTYRTC_SERVER_PERMANENT_KEY=0919b266ce1855419e4066fc076b39855e728768e3afa773105edd2e37037c20  

