####################################################################################  
# Creates a container with Graphviz and OpenJDK 8  
####################################################################################  
  
# Command reference:  
# docker build -t avanzabank/ubuntu-graphviz-openjdk8:0.0.1 -t
avanzabank/ubuntu-graphviz-openjdk8:latest .  
# docker run -it avanzabank/ubuntu-graphviz-openjdk8 /bin/bash  
  
  
FROM avanzabank/ubuntu-openjdk8:0.1.2  
  
RUN apt-get update && apt-get install -y \  
graphviz \  
ttf-freefont && \  
rm -rf /var/lib/apt/lists  
  
WORKDIR /opt  

