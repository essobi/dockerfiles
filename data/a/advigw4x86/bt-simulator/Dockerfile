FROM advigw4x86/service-template:v2.0.3  
#bt-simulator  
#MAINTAINER Advantech  
WORKDIR /home/adv  
  
RUN apt-get update &&\  
apt-get install -y git-core &&\  
git clone \--branch bt-simulator-v2.0.3 https://github.com/ADVANTECH-
Corp/docker-igw-app-x86.git ./wsn-simulator && \  
cp -r ./wsn-simulator/code ./wsn-simulator/wisesim . && \  
rm -rf ./wsn-simulator && \  
apt-get autoremove --purge -y git-core  
  
# Run Bt Simulator Service  
ENTRYPOINT ["./wisesim"]  

