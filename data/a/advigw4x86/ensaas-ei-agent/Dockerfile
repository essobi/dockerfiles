FROM advigw4x86/rmm3.3-agent_service-base  
  
#MAINTAINER Advantech  
# SUSIControl_Handler  
  
RUN apt-get update &&\  
apt-get install -y ethtool libcurl4-openssl-dev lsb-release libpci-dev &&\  
git clone \--branch ei-agent https://github.com/ADVANTECH-Corp/docker-igw-
app-x86.git &&\  
mv /home/adv/docker-igw-app-x86/AgentService /usr/local/. && cd /usr/local/.
&&\  
rm -rf /home/adv/docker-igw-app-x86/ && cd /home/adv &&\  
git clone \--branch wapi https://github.com/ADVANTECH-Corp/docker-igw-
app-x86.git &&\  
cd /home/adv/docker-igw-app-x86/ && ./install.sh && cd /home/adv &&\  
rm -rf /home/adv/docker-igw-app-x86 &&\  
git clone \--branch susi4.0 https://github.com/ADVANTECH-Corp/docker-igw-
app-x86.git &&\  
cd /home/adv/docker-igw-app-x86/susiinstaller/SUSI4.0/Driver && ./install.sh
&&\  
cd /home/adv/docker-igw-app-x86/susiinstaller/SUSIIoT/library && ./install.sh
&&\  
rm -rf /home/adv/docker-igw-app-x86 && cd /home/adv &&\  
apt-get autoremove \--purge -y git-core  
  
ENTRYPOINT ["/usr/local/AgentService/run_service-agent.sh"]  

