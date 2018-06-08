FROM advigw4x86/rmm3.3-agent_service-base  
  
#MAINTAINER Advantech  
# SUSIControl_Handler  
  
RUN apt-get update &&\  
apt-get install -y libpci-dev &&\  
git clone \--branch susi4.0 https://github.com/ADVANTECH-Corp/docker-igw-
app-x86.git &&\  
cd /home/adv/docker-igw-app-x86/susiinstaller/SUSI4.0/Driver && ./install.sh
&&\  
cd /home/adv/docker-igw-app-x86/susiinstaller/SUSIIoT/library && ./install.sh
&&\  
rm -rf /home/adv/docker-igw-app-x86 && cd /home/adv &&\  
git clone \--branch edge-sense-connector https://github.com/ADVANTECH-
Corp/docker-igw-app-x86.git &&\  
mv /home/adv/docker-igw-app-x86/AgentService /usr/local/EService-SUSIControl
&& cd /usr/local/EService-SUSIControl &&\  
mv ./service/SUSIControlHandler.so* ./module/. && mv ./service/module_config-
SUSIControlHandler.xml ./module/module_config.xml &&\  
mv ./agent_config-SUSIControlHandler.xml agent_config.xml &&\  
rm -rf /home/adv/docker-igw-app-x86/ &&\  
apt-get autoremove \--purge -y git-core  
  
ENTRYPOINT ["/usr/local/EService-SUSIControl/run_service-susicontrol.sh"]  

