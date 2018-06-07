FROM node:6.13 as ember_app  
  
ARG TAG  
RUN echo TAG=$TAG ; \  
node --version ; npm --version ; \  
npm install g yarn ; yarn --version ; \  
yarn global add ember-cli@2.4.3 ; \  
yarn global add bower ; \  
git clone --depth=50 --branch=docker-release
https://github.com/Flexberry/flexberry-service-bus-editor.git
/Flexberry/flexberry-service-bus-editor ; \  
cd /Flexberry/flexberry-service-bus-editor ; \  
yarn install ; \  
bower install --allow-root ; \  
ember build --environment=docker  
  
  
FROM mono:latest as backend  
  
ARG TAG  
RUN echo TAG=$TAG ; \  
mono --version ; \  
apt update ; \  
apt install -y git ; \  
git clone --depth=50 --branch=$TAG
https://github.com/Flexberry/NewPlatform.Flexberry.ServiceBus.Editor.git
/Flexberry/NewPlatform.Flexberry.ServiceBus.Editor ; \  
msbuild /version ; \  
cd /Flexberry/NewPlatform.Flexberry.ServiceBus.Editor ; \  
nuget restore NewPlatform.Flexberry.ServiceBus.Editor.sln ; \  
msbuild /p:Configuration=Release NewPlatform.Flexberry.ServiceBus.Editor.sln  
  
FROM flexberry/alt.p8-apache2-mono:latest  
  
MAINTAINER mail@flexberry.net  
COPY \--from=backend
/Flexberry/NewPlatform.Flexberry.ServiceBus.Editor/ODataBackend
/var/www/vhosts/ServiceBusEditor  
COPY \--from=ember_app /Flexberry/flexberry-service-bus-editor/dist
/var/www/vhosts/ServiceBusEditor  
COPY vhosts.conf /conf  
RUN rm -f /var/www/vhosts/ServiceBusEditor/bin/Mono.Security.dll ; \  
rm -f /var/www/vhosts/ServiceBusEditor/Global.asax.cs ; \  
rm -f
/var/www/vhosts/ServiceBusEditor/NewPlatform.Flexberry.ServiceBus.Editor.ODataBackend.csproj
; \  
rm -f /var/www/vhosts/ServiceBusEditor/Web.Debug.config ; \  
rm -f /var/www/vhosts/ServiceBusEditor/Web.Release.config ; \  
rm -f /var/www/vhosts/ServiceBusEditor/packages.config ; \  
rm -fr /var/www/vhosts/ServiceBusEditor/App_Start ; \  
rm -fr /var/www/vhosts/ServiceBusEditor/Properties ; \  
rm -fr /var/www/vhosts/ServiceBusEditor/obj ; \  
rm /var/www/vhosts/ServiceBusEditor/Web.config ; \  
mv /var/www/vhosts/ServiceBusEditor/Web.Docker.config
/var/www/vhosts/ServiceBusEditor/Web.config  

