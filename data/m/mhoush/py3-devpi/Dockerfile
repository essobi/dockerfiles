FROM mhoush/py3:latest  
  
ARG index="m.housh/dev"  
ARG host  
  
# below adapted from https://hub.docker.com/r/muccg/devpi/  
RUN apk --no-cache add \--virtual build_deps \  
netcat-openbsd && \  
[ $host != "" ] && export HOST_IP=$host || \  
export HOST_IP=$(ip route | awk '/^default/ { print $3 }') && \  
mkdir -p ~/.pip && \  
echo [global] >> ~/.pip/pip.conf && \  
echo extra-index-url = http://$HOST_IP:3141/$index/+simple >> ~/.pip/pip.conf
&& \  
echo [install] >> ~/.pip/pip.conf && \  
echo trusted-host = $HOST_IP >> ~/.pip/pip.conf && \  
cat ~/.pip/pip.conf && \  
apk del build_deps  

