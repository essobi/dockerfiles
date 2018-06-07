FROM ubuntu:16.04  
RUN sh -c 'echo "deb [arch=amd64] http://apt-
mo.trafficmanager.net/repos/dotnet-release/ xenial main" >
/etc/apt/sources.list.d/dotnetdev.list'  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 417A0893  
  
RUN apt-get update  
  
RUN apt-get -y install dotnet-dev-1.0.0-preview2.1-003177  
  
RUN apt-get install -y gendarme\  
&& apt-get install -y git\  
&& apt-get install -y redis-tools\  
&& apt-get install curl\  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash -\  
&& apt-get install nodejs  
  
RUN node -v  
  
COPY . /utility  
  
WORKDIR /app  
  
EXPOSE 5000  
CMD ["/bin/sh"]

