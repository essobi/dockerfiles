FROM efrecon/medium-tcl  
MAINTAINER Emmanuel Frecon <emmanuel@sics.se>  
  
# Copy current version of the bridge software to /opt/bridge/  
COPY bin/*.tcl /opt/biot/bin/  
COPY lib/biot/*.tcl /opt/biot/lib/biot/  
COPY lib/biot/src/*.tcl /opt/biot/lib/biot/src/  
COPY lib/biot/dst/*.tcl /opt/biot/lib/biot/dst/  
COPY lib/modules/*.tcl /opt/biot/lib/modules/  
COPY lib/modules/*.tm /opt/biot/lib/modules/  
COPY lib/netstats/*.tcl /opt/biot/lib/netstats/  
COPY lib/syslog/*.tcl /opt/biot/lib/syslog/  
COPY lib/toclbox /opt/biot/lib/toclbox  
COPY lib/websocket/*.tcl /opt/biot/lib/websocket/  
COPY lib/tockler /opt/biot/lib/tockler  
COPY cfg/tpl/ /opt/biot/cfg/tpl/  
COPY cfg/daemon/ /opt/biot/cfg/daemon/  
COPY cfg/*.cfg /opt/biot/cfg/  
  
# Install git and fossil so we can install dependencies  
RUN apk add --update-cache git socat && \  
apk add --update-cache --repository
http://dl-4.alpinelinux.org/alpine/edge/testing fossil && \  
git clone --depth 1 https://github.com/efrecon/tcl-stomp /tmp/tcl-stomp && \  
rm -rf /tmp/tcl-stomp/.git && \  
mv /tmp/tcl-stomp/lib/stomp /opt/biot/lib/ && \  
git clone --depth 1 https://github.com/efrecon/til /opt/biot/lib/til && \  
rm -rf /opt/biot/lib/til/.git && \  
git clone https://github.com/efrecon/etcd-tcl /tmp/etcd-tcl && \  
rm -rf /tmp/etcd-tcl/.git && \  
mv /tmp/etcd-tcl/etcd /opt/biot/lib/ && \  
fossil clone -A docker http://chiselapp.com/user/sgolovan/repository/tclxmpp
/tmp/tclxmpp.fsl && \  
mkdir /opt/biot/lib/tclxmpp && \  
cd /opt/biot/lib/tclxmpp && \  
fossil open /tmp/tclxmpp.fsl && \  
apk del git fossil && \  
rm -rf /tmp/tcl-stomp /tmp/etcd-tcl /tmp/tclxmpp.fsl && \  
rm -rf /var/cache/apk/*  
  
# Export port for draft REST API  
EXPOSE 8800  
  
# Arrange to autoexecute biot as daemon on start  
ENTRYPOINT ["tclsh8.6", "/opt/biot/bin/biot.tcl"]  

