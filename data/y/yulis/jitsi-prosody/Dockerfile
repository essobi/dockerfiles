FROM ubuntu:trusty  
  
MAINTAINER Yulian Slobodyan <y.slobodian@gmail.com>  
  
ENV PROSODY_VERSION="0.10"  
ENV OTALK_SERVER_GIT_REVISION="50d5d385f8d81fd133c4f880ee8873b1273ee867"  
# These variables should be overriden to configure Prosody  
ENV XMPP_DOMAIN="example.com"  
ENV VIDEOBRIDGE_SECRET="fUb8iJ5aRk5Urg1Y"  
ENV FOCUS_SECRET="oB2cHipt6Ur0eD6E"  
RUN apt-get -y install wget  
  
RUN echo deb http://packages.prosody.im/debian trusty main | sudo tee -a
/etc/apt/sources.list  
RUN wget --no-check-certificate \  
https://prosody.im/files/prosody-debian-packages.key -O- | apt-key add -  
  
RUN apt-get update && apt-get -y install \  
git-core \  
prosody-${PROSODY_VERSION} \  
lua-zlib \  
lua-dbi-sqlite3 \  
liblua5.1-bitop-dev \  
liblua5.1-bitop0  
  
RUN wget http://security.ubuntu.com/ubuntu/pool/universe/l/lua-expat/lua-
expat_1.3.0-2_amd64.deb  
RUN dpkg -i lua-expat_1.3.0-2_amd64.deb  
  
RUN git clone https://github.com/andyet/otalk-server.git && \  
cd otalk-server && \  
git checkout ${OTALK_SERVER_GIT_REVISION} && \  
cp -r mod* /usr/lib/prosody/modules  
  
ADD conf/prosody.cfg.lua /etc/prosody/prosody.cfg.lua  
ADD conf/host.cfg.lua /etc/prosody/conf.d/host.cfg.lua.tmpl  
ADD scripts/run.sh run.sh  
  
# XMPP client-to-server  
EXPOSE 5222  
# XMPP server-to-server  
EXPOSE 5269  
# HTTP and WebSocket  
EXPOSE 5280  
# HTTP and WebSocket with SSL  
EXPOSE 5281  
# STUN/TURN (UDP)  
EXPOSE 3478  
# External Components (XEP_0114)  
EXPOSE 5347  
CMD [ "./run.sh" ]  

