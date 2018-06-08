FROM rojima1/base  
  
USER root  
WORKDIR /home/root  
  
RUN apt-get update && \  
apt-get install -y \  
openjdk-8-jdk && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN wget -q -O lein -q
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein &&
chmod 755 lein && mv lein /usr/local/bin  
  
USER developer  
WORKDIR /home/developer  

