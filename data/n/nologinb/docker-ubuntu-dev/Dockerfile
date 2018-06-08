FROM nologinb/java8  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
wget \  
easy-rsa \  
net-tools \  
mc \  
iputils-ping \  
dnsutils \  
iperf \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["bash"]  

