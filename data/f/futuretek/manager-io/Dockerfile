FROM ubuntu:xenial  
  
MAINTAINER Lukas Cerny <lukas.cerny@futuretek.cz>  
  
RUN mkdir /manager /data  
  
WORKDIR /manager  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF \  
&& echo "deb http://download.mono-project.com/repo/ubuntu stable-xenial main"
| tee /etc/apt/sources.list.d/mono-official-stable.list \  
&& apt-get update \  
&& apt-get install -y mono-complete wget \  
&& wget https://d2ap5zrlkavzl7.cloudfront.net/18.1.96/ManagerServer.tar.gz -P
/manager \  
&& tar -xzf /manager/ManagerServer.tar.gz -C /manager \  
&& rm /manager/ManagerServer.tar.gz \  
&& apt-get -y autoremove \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8080  
VOLUME ["/data"]  
  
CMD mono ManagerServer.exe -port 8080 -path "/data"  

