FROM ubuntu:14.04  
MAINTAINER Eugene Dounar <eugene.dounar@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y nodejs npm git  
  
RUN update-alternatives --install /usr/bin/node node /usr/bin/nodejs 10  
RUN npm install -g strider  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y apt-transport-https && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
36A1D7869245C8950F966E92D8576A8BA88D21E9 && \  
sh -c "echo deb https://get.docker.com/ubuntu docker main >
/etc/apt/sources.list.d/docker.list" && \  
apt-get update && \  
apt-get install -y lxc-docker  
  
CMD ["strider"]  
EXPOSE 3000  

