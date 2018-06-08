FROM mono:latest as mono  
  
ARG TAG  
RUN mono --version && \  
apt update && \  
apt install -y git && \  
git clone \--depth=50 --branch=$TAG
https://github.com/Flexberry/NewPlatform.Flexberry.ServiceBus.git
/Flexberry/NewPlatform.Flexberry.ServiceBus && \  
msbuild /version && \  
cd /Flexberry/NewPlatform.Flexberry.ServiceBus && \  
nuget restore NewPlatform.Flexberry.ServiceBus.sln && \  
msbuild /p:Configuration=Release NewPlatform.Flexberry.ServiceBus.sln  
  
FROM flexberry/alt.p8-apache2-mono:latest  
  
COPY \--from=mono
/Flexberry/NewPlatform.Flexberry.ServiceBus/NewPlatform.Flexberry.ServiceBus.WinServiceHost/bin/Release
/opt/flexberry-service-bus  
COPY host/prepareConf.sh /opt/  
COPY host/start-flexberry-service-bus.sh /opt/  
  
RUN mkdir /opt/flexberry-service-bus ; adduser flexberry ; \  
rm /opt/flexberry-service-bus/Mono.Security.dll ; \  
rm /opt/flexberry-service-
bus/NewPlatform.Flexberry.ServiceBus.WinServiceHost.exe.config ; \  
cp /opt/flexberry-service-bus/App.Docker.config /opt/flexberry-service-
bus/NewPlatform.Flexberry.ServiceBus.WinServiceHost.exe.config  
  
MAINTAINER mail@flexberry.net  
  
USER root  
  
CMD echo "DOCKER_HOSTNAME=$DOCKER_HOSTNAME"; sh -x /opt/prepareConf.sh ; su -l
-c "sh /opt/start-flexberry-service-bus.sh" flexberry  

