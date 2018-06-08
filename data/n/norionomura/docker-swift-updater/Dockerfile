ARG DOCKER_IMAGE=norionomura/swift:swift-4.2-branch  
FROM ${DOCKER_IMAGE}  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
libunwind8 \  
software-properties-common && \  
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \  
add-apt-repository \  
"deb [arch=amd64] https://download.docker.com/linux/ubuntu \  
$(lsb_release -cs) \  
stable" && \  
apt-get update && apt-get install -y docker-ce && \  
rm -r /var/lib/apt/lists/*  
ADD . /docker-swift  
RUN cd /docker-swift && \  
swift build --configuration release --static-swift-stdlib && \  
mv `swift build --configuration release --static-swift-stdlib --show-bin-
path`/docker-swift-updater /usr/bin && \  
cd / && \  
rm -rf docker-swift  
  
CMD ["docker-swift-updater"]  

