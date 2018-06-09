FROM ubuntu:14.04.2  
MAINTAINER Travis James <travis@tribemedia.io>  
  
RUN apt-get -y update  
RUN apt-get -y upgrade  
RUN apt-get -y dist-upgrade  
RUN apt-get autoremove  
RUN apt-get install -y build-essential  
RUN apt-get install -y git  
RUN apt-get install -y cmake  
RUN apt-get install -y wget  
RUN apt-get install -y python2.7 python2.7-dev  
RUN apt-get install -y nano  
RUN apt-get install -y openssl libssl-dev libevent-dev  
RUN apt-get install -y curl  
  
RUN locale-gen en_US en_US.UTF-8  
RUN dpkg-reconfigure locales  
ENV LANG en_US.utf8  
  
RUN apt-get update && apt-get install -y openssh-server supervisor  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
COPY start.sh start.sh  
RUN ["chmod", "+x", "start.sh"]  
RUN mkdir /var/run/sshd  
RUN echo 'root:tribemedia' | chpasswd  
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN export PATH=$PATH:/usr/bin && git clone https://github.com/joyent/node.git
/node && cd /node && git checkout tags/v0.12.7 && ./configure && CXX="g++
-Wno-unused-local-typedefs" make && CXX="g++ -Wno-unused-local-typedefs" make
install && \  
npm install -g npm && \  
printf '\n# Node.js\nexport PATH="node_modules/.bin:/usr/local/bin:$PATH"' >>
/root/.bashrc  
RUN apt-get install -y software-properties-common  
  
# CoTurn  
RUN cd / && git clone https://github.com/svn2github/coturn.git && cd coturn &&
./configure && make && make install  
  
# Node stuff  
RUN npm install -g bower  
  
RUN echo "{\"allow_root\":true}" >> /root/.bowerrc  
  
RUN "deb http://ubuntu.kurento.org trusty kms6" | tee
/etc/apt/sources.list.d/kurento.list && \  
wget -O - http://ubuntu.kurento.org/kurento.gpg.key | sudo apt-key add - && \  
apt-get -y update && apt-get install kurento-server  
RUN rm /etc/kurento/modules/kurento/MediaElement.conf.ini && rm
/etc/kurento/modules/kurento/HttpEndpoint.conf.ini && \  
rm /etc/kurento/modules/kurento/WebRtcEnpoint.ini  
COPY MediaElement.conf.ini /etc/kurento/modules/kurento/MediaElement.conf.ini  
COPY HttpEndpoint.conf.ini /etc/kurento/modules/kurento/HttpEndpoint.conf.ini  
  
COPY transform/go.js /transform/go.js  
COPY transform/goturn.js /transform/goturn.js  
COPY transform/WebRtcEndpoint.tmpl /transform/WebRtcEndpoint.tmpl  
COPY transform/turnserver.tmpl /transform/turnserver.tmpl  
COPY transform/package.json /transform/package.json  
  
RUN mkdir /docker-entrypoint-init-kurento.d  
  
RUN rm -rf /node  
RUN rm -rf /coturn  
  
ENV KURENTO_DATA /var/lib/kurento/data  
VOLUME /var/lib/kurento/data  
  
EXPOSE 22 3000 8888 8080 49152-65535/udp 3478/udp 3478  
ENTRYPOINT ["/start.sh"]  
CMD ["/usr/bin/supervisord"]

