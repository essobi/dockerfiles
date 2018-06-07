#  
# Version: 1.0.1  
#  
FROM ubuntu:16.04  
MAINTAINER Oscar Martin "oscar@omartin.es"  
  
ENV REFRESHED_AT 2018-05-08  
  
RUN apt-get update; \  
apt-get install -y net-tools vim curl wget xz-utils python make; \  
apt-get install -y x11vnc xvfb firefox  
  
WORKDIR /home  
USER root  
RUN wget https://nodejs.org/dist/v8.11.1/node-v8.11.1-linux-x64.tar.xz -O
/home/node-v8.11.1-linux-x64.tar.xz; \  
tar xJvf /home/node-v8.11.1-linux-x64.tar.xz -C /home/; \  
mv /home/node-v8.11.1-linux-x64 /opt/; \  
ln -s /opt/node-v8.11.1-linux-x64/ /opt/node; \  
ln -s /opt/node/bin/node /usr/local/bin/; \  
ln -s /opt/node/bin/npm /usr/local/bin/; \  
ln -s /opt/node/bin/np /usr/local/bin/; \  
rm /home/node-v8.11.1-linux-x64.tar.xz  
  
RUN wget
https://github.com/mozilla/geckodriver/releases/download/v0.20.1/geckodriver-v0.20.1-linux64.tar.gz
-O /home/geckodriver.tar.gz; \  
tar xzvf /home/geckodriver.tar.gz -C /home/; \  
mv /home/geckodriver /usr/local/bin/; \  
rm /home/geckodriver.tar.gz  
  
RUN npm install --global web-ext --unsafe-perm; \  
npm install --global selenium-webdriver; \  
mkdir -p /home/firefox/extensions; \  
mkdir ~/.vnc  
  
RUN x11vnc -storepasswd 1234 ~/.vnc/passwd  
  
ENV PATH=$PATH:/opt/node/lib/node_modules/web-ext/bin  
ENV DISPLAY=:1.0  
RUN bash -c "echo 'export PATH=$PATH:/opt/node/lib/node_modules/web-ext/bin'
>> ~/.bashrc"  
RUN bash -c "echo 'export DISPLAY=:1.0' >> ~/.bashrc"  
  
EXPOSE 5900  
  
COPY run.sh run.sh  
CMD ./run.sh  

