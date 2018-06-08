FROM confluentinc/cp-kafka-connect  
  
RUN \  
apt-get update \  
&& apt-get upgrade -y  
  
RUN \  
apt-get autoremove -y \  
&& apt-get remove \--purge -y \  
&& rm -rf /var/lib/apt/lists/*  

