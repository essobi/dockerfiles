FROM rust:1.23  
# Base dependencies  
RUN apt-get update -qqy \  
&& apt-get install -qqy --no-install-recommends \  
locales \  
libsodium18 \  
libsodium-dev \  
python3 \  
python3-pip \  
python3-setuptools \  
python3-wheel \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# Fix locales  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LANG=en_US.UTF-8  
ENV LC_ALL=en_US.UTF-8 \  
LANG=en_US.UTF-8  
# Add wrapper scripts  
ADD saltyrtc-server-launcher /usr/local/bin/saltyrtc-server-launcher  
RUN chmod +x /usr/local/bin/saltyrtc-server-launcher  
  
# Create test certificates  
ADD generate-cert.sh /saltyrtc/certs/generate-cert.sh  
  
# Update directory permissions  
RUN chmod a+w /saltyrtc  
  
# Install SaltyRTC server  
RUN pip3 install saltyrtc.server[logging]  
  
# Install cargo-audit  
RUN cargo install cargo-audit  
  
# Export SaltyRTC test permanent key  
ENV
SALTYRTC_SERVER_PERMANENT_KEY=0919b266ce1855419e4066fc076b39855e728768e3afa773105edd2e37037c20  

