FROM ubuntu:16.04  
MAINTAINER Douglas Tan <bianster@gmail.com>  
  
# install xvfb and other X dependencies for IB  
RUN apt-get update -y \  
&& apt-get install -y xvfb libxrender1 libxtst6 x11vnc socat unzip software-
properties-common unzip supervisor inotify-tools \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN add-apt-repository -y ppa:webupd8team/java \  
&& apt-get update -y \  
&& apt-get install -y oracle-java8-installer ca-certificates  
  
# installs to /root irregardless of WORKDIR settings  
ADD https://github.com/bianster/ib-tws-binaries/raw/master/tws/963.3m/tws-
stable-standalone-linux-x64.sh tws-standalone-linux-x64.sh  
RUN chmod +x tws-standalone-linux-x64.sh  
RUN ./tws-standalone-linux-x64.sh -q  
  
RUN mkdir -p /opt/IBController && wget https://github.com/ib-controller/ib-
controller/releases/download/3.4.0/IBController-3.4.0.zip && unzip
IBController-3.4.0.zip -d /opt/IBController && chmod -R +x
/opt/IBController/*.sh && chmod -R +x /opt/IBController/Scripts/*.sh && rm
IBController-3.4.0.zip  
  
COPY bin/update-ibcontroller-config.py /usr/bin/update-ibcontroller-config.py  
COPY bin/run-ibc /usr/bin/run-ibc  
COPY bin/run-vnc /usr/bin/run-vnc  
COPY bin/run-xvfb /usr/bin/run-xvfb  
COPY bin/run-logger /usr/bin/run-logger  
  
RUN mkdir -p /var/log/ib && mkdir -p /root/conf && mkdir -p /root/IBController
&& mkdir -p /tmp/tws  
COPY conf/supervisord.conf /root/conf/supervisord.conf  
  
ENV DISPLAY=":0" VNC_PASSWORD="1234" TWS_CONF_DIR="" TWS_SYNC_CONF=""
IB_LOGIN="edemo" IB_PASSWORD="demouser" IB_MODE="paper"  
EXPOSE 5900 4001  
VOLUME /var/log/ib /root/IBController/Logs /tmp/tws  
  
CMD ["/usr/bin/supervisord", "-n", "-c", "/root/conf/supervisord.conf"]

