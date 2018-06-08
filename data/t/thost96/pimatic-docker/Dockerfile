FROM debian  
  
LABEL maintainer="info@thorstenreichelt.de"  
  
RUN apt-get update && apt-get install -y curl gnupg2  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -  
RUN apt-get update && apt-get install -y \  
git \  
wget \  
tar \  
build-essential \  
python \  
nodejs  
  
RUN node --version && npm -v  
RUN npm install -g node-gyp  
  
#Pimatic Install  
WORKDIR /  
RUN mkdir /pimatic-app && \  
npm install pimatic --prefix pimatic-app --production  
  
RUN cp /pimatic-app/node_modules/pimatic/config_default.json /pimatic-
app/config.json && \  
sed -i "s/\"password\": \"\"/\"password\": \"pimatic\"/g" /pimatic-
app/config.json  
  
RUN cd /pimatic-app/node_modules/pimatic && \  
npm link  
  
RUN cd /pimatic-app && \  
npm install sqlite3@3.1.8 --unsafe-perm && \  
npm install pimatic-mobile-frontend --unsafe-perm  
  
#Autostart  
RUN wget
https://raw.githubusercontent.com/pimatic/pimatic/v0.9.x/install/pimatic-
init-d && \  
cp pimatic-init-d /etc/init.d/pimatic && \  
chmod +x /etc/init.d/pimatic && \  
chown root:root /etc/init.d/pimatic && \  
update-rc.d pimatic defaults  
  
#WiringPi Setup  
RUN cd /pimatic-app && \  
git clone git://git.drogon.net/wiringPi && \  
cd wiringPi && \  
git pull origin && \  
cd wiringPi %% \  
./build  
  
#START Service  
RUN service pimatic start  
  
VOLUME ["/pimatic-app"]  
EXPOSE 80  

