FROM ubuntu:trusty  
  
COPY InstallSpinnaker.sh /  
  
RUN apt-get update && apt-get install -y netcat apt-transport-https software-
properties-common curl  
  
RUN bash /InstallSpinnaker.sh --cloud_provider none  

