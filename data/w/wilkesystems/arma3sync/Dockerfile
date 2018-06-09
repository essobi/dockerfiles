FROM debian:stretch  
  
MAINTAINER wilkesystems <maintainer@wilke.systems>  
  
ADD arma3sync.tar.xz /  
  
RUN apt-get update; \  
apt-get install -y bzip2 curl default-jdk p7zip unzip wget xz-utils; \  
rm -rf /var/lib/apt/lists/*;  
  
CMD ["arma3sync"]  

