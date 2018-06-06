FROM nvidia/cuda:7.5-runtime  
  
RUN apt-get update  
RUN apt-get install apt-transport-https -y  
RUN sh -c 'echo "deb [arch=amd64] https://apt-
mo.trafficmanager.net/repos/dotnet-release/ trusty main" >
/etc/apt/sources.list.d/dotnetdev.list'  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893  
RUN apt-get update  
RUN apt-get install dotnet-sdk-2.0.0 -y  

