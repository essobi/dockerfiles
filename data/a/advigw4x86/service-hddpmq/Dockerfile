FROM advigw4x86/rmm3.3-agent_service-base  
  
#MAINTAINER Advantech  
# SUSIControl_Handler  
  
RUN apt-get update &&\  
git clone \--branch edge-sense-connector https://github.com/ADVANTECH-
Corp/docker-igw-app-x86.git &&\  
mv /home/adv/docker-igw-app-x86/AgentService /usr/local/EService-HDDPMQ && cd
/usr/local/EService-HDDPMQ &&\  
mv ./service/HDDPMQ.so* ./module/. && mv ./service/module_config-HDD_PMQ.xml
./module/module_config.xml &&\  
mv ./agent_config-HDD_PMQ.xml agent_config.xml &&\  
rm -rf /home/adv/docker-igw-app-x86/ &&\  
apt-get autoremove --purge -y git-core  
  
ENTRYPOINT ["/usr/local/EService-HDDPMQ/run_service-hddpmq.sh"]  

