FROM advigw4x86/service-template:v2.0.3  
#MAINTAINER Advantech  
WORKDIR /home/adv  
  
RUN apt-get update &&\  
apt-get install -y git-core &&\  
git clone \--branch dust-link-v2.0.3 https://github.com/ADVANTECH-Corp/docker-
igw-app-x86.git . &&\  
./install_dust-link.sh && rm ./install_dust-link.sh &&\  
apt-get autoremove --purge -y git-core  
  
# Run Dust Link Service  
ENTRYPOINT ["./testDustWsnDrv"]  

