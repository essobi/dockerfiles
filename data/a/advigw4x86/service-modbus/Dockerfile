FROM advigw4x86/rmm3.3-agent_service-base  
  
#MAINTAINER Advantech  
# Modbus_Handler  
  
RUN apt-get update &&\  
git clone \--branch edge-sense-connector https://github.com/ADVANTECH-
Corp/docker-igw-app-x86.git &&\  
mv /home/adv/docker-igw-app-x86/AgentService /usr/local/EService-Modbus && cd
/usr/local/EService-Modbus &&\  
mv ./service/Modbus_Handler.so* ./module/. && mv ./service/module_config-
Modbus_Handler.xml ./module/module_config.xml &&\  
mv ./agent_config-Modbus_Handler.xml agent_config.xml &&\  
rm -rf /home/adv/docker-igw-app-x86/ &&\  
apt-get autoremove --purge -y git-core  
  
ENTRYPOINT ["/usr/local/EService-Modbus/run_service-modbus.sh"]  

