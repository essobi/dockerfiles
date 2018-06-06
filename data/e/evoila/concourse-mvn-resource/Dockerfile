FROM maven:latest  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y \  
apt-utils xmlstarlet jq python python-yaml\  
&& rm -rf /var/lib/apt/lists/*  
RUN echo "#!/bin/bash\nRES=\"/opt/resource\"\nexport RES\nexport
PATH=\"$PATH:/opt/resource\"" >> ~/.bashrc  
RUN mkdir -p /root/.m2  
ADD asserts/ /opt/resource/  
RUN chmod +x /opt/resource/*  

