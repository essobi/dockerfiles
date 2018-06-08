FROM quantrocket/anaconda3-uwsgi  
MAINTAINER QuantRocket <support@quantrocket.com>  
  
RUN apt-get update && apt-get install -y \  
unzip \  
expect \  
socat \  
xvfb \  
lsof \  
x11vnc \  
xmlstarlet \  
&& /bin/bash -c "source activate /opt/conda" \  
&& pip install websockify==0.8.0 \  
&& /bin/bash -c "source deactivate"  
# Install IBG  
COPY tmp/install_ibg.exp /tmp/install_ibg.exp  
RUN curl \--fail \--output /tmp/ibgateway-latest-standalone-linux-x64.sh
https://download2.interactivebrokers.com/installers/ibgateway/latest-
standalone/ibgateway-latest-standalone-linux-x64.sh \  
&& chmod u+x /tmp/ibgateway-latest-standalone-linux-x64.sh \  
&& chmod u+x /tmp/install_ibg.exp \  
&& sync && /tmp/install_ibg.exp \  
&& apt-get remove -y expect  
  
# Install IBController  
ENV IBCONTROLLER_VERSION 3.2.0  
RUN curl \--fail \--silent \--location \--output /tmp/IBController.zip
https://github.com/ib-controller/ib-
controller/releases/download/${IBCONTROLLER_VERSION}/IBController-${IBCONTROLLER_VERSION}.zip
\  
&& unzip /tmp/IBController.zip -d /opt/IBController \  
&& chmod -R u+x /opt/IBController/*.sh \  
&& chmod -R u+x /opt/IBController/Scripts/*.sh \  
&& apt-get remove -y unzip  
  
# Add xvfb/vnc/bin scripts  
COPY init /etc/init.d  
COPY bin /usr/bin  
COPY qrocket /tmp/uwsgi/qrocket  
COPY root /root  
COPY uwsgi /etc/uwsgi  
RUN chmod u+x /etc/init.d/* \  
&& mkdir -p /etc/opt/quantrocket \  
&& chmod -R u+x /usr/bin/* \  
&& /tmp/build.sh  
# Set env vars for IBController  
ENV IBC_INI=/root/IBController/IBController.ini \  
IBC_PATH=/opt/IBController \  
TWS_PATH=/root/Jts \  
TWS_CONFIG_PATH=/root/Jts \  
LOG_PATH=/opt/IBController/Logs \  
APP=GATEWAY \  
IBG_CLIENT_RANGE=1000  
  
# expose ibg and vnc port  
EXPOSE 4001 5900  

