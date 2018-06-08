  
FROM rhche/centos_jdk8  
USER root  
RUN sudo yum update -y && \  
sudo yum install -y wget  
RUN wget -qO- "https://github.com/apache/incubator-openwhisk-
cli/releases/download/latest/OpenWhisk_CLI-latest-linux-amd64.tgz" | tar -zx
-C /usr/local/bin/ && \  
wget -qO- "https://github.com/apache/incubator-openwhisk-
wskdeploy/releases/download/0.9.0/wskdeploy-0.9.0-linux-amd64.tgz" | tar -zx
-C /usr/local/bin/  
USER user  
COPY ["init-maven.sh","/tmp/init-maven.sh"]  
  
ADD https://api.github.com/repos/apache/incubator-openwhisk-
devtools/git/refs/heads/master /tmp/current-sha1  
  
RUN sudo chown user:user /tmp/init-maven.sh && \  
chmod +x /tmp/init-maven.sh && \  
/tmp/init-maven.sh && \  
sudo rm -f /tmp/init-maven.sh  
  
# Give write access to /home/user for  
RUN sudo chgrp -R 0 /home/user && sudo chmod -R g+rwX /home/user  

