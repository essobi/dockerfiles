FROM nvidia/opencl:runtime-ubuntu16.04  
  
RUN apt update && \  
apt install -y --no-install-recommends libssl-dev mono-devel mono-runtime
nvidia-opencl-dev && \  
apt install -y --no-install-recommends curl unzip ca-certificates && \  
curl -L
https://github.com/lachesis/scallion/releases/download/v2.1/scallion-v2.1.zip
-o /tmp/scallion-v2.1.zip && \  
unzip -j /tmp/scallion-v2.1.zip "scallion-v2.1/*" -d /opt/scallion/ && \  
apt remove -y curl unzip ca-certificates && \  
apt autoclean -y && \  
rm -rf /var/lib/apt/lists/* && \  
useradd -ms /bin/bash scallion  
  
USER scallion  
  
ENTRYPOINT ["/usr/bin/mono", "/opt/scallion/scallion.exe"]  

