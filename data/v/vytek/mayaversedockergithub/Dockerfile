#Name of container: MayaVerDocker  
#Version of container: 0.1 Alfa  
FROM mono:latest  
MAINTAINER Enrico Speranza <enrico.speranza@gmail.com>  
  
# Install git  
RUN apt-get update && apt-get -y install git  
  
# Install Hazel Server  
RUN git clone https://github.com/Vytek/HazelTest usr/src/hazel  
  
WORKDIR /usr/src/hazel  
  
# Compile Hazel Server  
#RUN dotnet add package DarkRiftNetworking.Hazel --version 0.1.2-beta  
#RUN dotnet add package DevZH.FlatBuffers --version 1.4.0  
RUN msbuild /t:restore HazelTest.sln  
  
# Hazel Server  
EXPOSE 4296/udp  
  

