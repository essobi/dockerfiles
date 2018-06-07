FROM pablotech/hedge-j2se:latest  
#FROM hedge-j2se:latest  
#IBGateway download  
RUN apt-get -y install xterm  
RUN wget https://download2.interactivebrokers.com/installers/ibgateway/latest-
standalone/ibgateway-latest-standalone-linux-x64.sh  
RUN mv ibgateway-latest-standalone-linux-x64.sh /opt; chmod +x /opt/ibgateway-
latest-standalone-linux-x64.sh  
#IBGateway install  
WORKDIR /home/hedge  
USER hedge  
RUN cd /home/hedge/ && echo "n" | /opt/ibgateway-latest-standalone-
linux-x64.sh  
  
USER root  
#IBController download  
RUN git clone https://github.com/ib-controller/ib-controller.git /opt/ib-
controller  
  
#IBController install  
RUN mkdir -p /opt/IBController  
RUN cp -R /opt/ib-controller/resources/* /opt/IBController/  
RUN chmod +x /opt/IBController/IBControllerGatewayStart.sh  
RUN chmod +x /opt/IBController/Scripts/*  
RUN ln -sf /opt/IBController/ /home/hedge/  
  
RUN chown hedge: -R /opt/*  
  
RUN sed -i '10s/^/\nset | grep "^ONENOW\\\|^JAVA_TOOL_OPTION" >\/etc\/env\n/'
/etc/rc.local  
RUN sed -i '12s/^/su - hedge -c "touch \/home\/hedge\/.Xresources"\n/'
/etc/rc.local  
  
#add the IBGw into X starting procedures  
RUN echo '#!/bin/bash' > /usr/bin/start_ibjts  
RUN echo '. /etc/env' >> /usr/bin/start_ibjts  
  
#change the default user  
RUN echo "sed -ie \"s/^IbLoginId=.*/IbLoginId=\$ONENOW_IB_LOGIN/g\"
/opt/IBController/IBController.ini" >>/usr/bin/start_ibjts  
  
#change the default pass  
RUN echo "sed -ie \"s/^IbPassword=.*/IbPassword=\$ONENOW_IB_PASS/g\"
/opt/IBController/IBController.ini" >>/usr/bin/start_ibjts  
  
#change the TradingMode  
RUN echo "sed -ie \"s/^TRADING_MODE=.*/TRADING_MODE=\$ONENOW_IB_MODE/g\"
/opt/IBController/IBControllerGatewayStart.sh" >>/usr/bin/start_ibjts  
RUN echo "sed -ie \"s/^TradingMode=.*/TradingMode=\$ONENOW_IB_MODE/g\"
/opt/IBController/IBController.ini" >>/usr/bin/start_ibjts  
RUN echo "sed -ie \"s/^tradingMode=.*/tradingMode=\${ONENOW_IB_MODE:0:1}/g\"
/home/hedge/Jts/jts.ini" >>/usr/bin/start_ibjts  
RUN echo "/opt/IBController/IBControllerGatewayStart.sh" >>
/usr/bin/start_ibjts  
RUN echo "sleep 20s && kill \\`ps -ef | grep jts4launch- | grep -v grep | awk
'{ print \$2}'\\`" >>/usr/bin/start_ibjts  
  
RUN echo "find /home/hedge/Jts/ -mindepth 1 -maxdepth 1 -type d -not -name
\"jars\" -not -name \"ibgateway\" -not -name \"dhublqxuuj\" -exec cp
/home/hedge/Jts/dhublqxuuj/ibg.xml \"{}\" \;" >>/usr/bin/start_ibjts  
RUN echo "sed -ie
\"s/readOnlyApi=\\\\\"false\\\\\"/readOnlyApi=\\\\\"\${ONENOW_IB_READONLY}\\\\\"/g\"
/home/hedge/Jts/*/ibg.xml" >>/usr/bin/start_ibjts  
  
#java  
RUN echo "sed -ie \"s/^-Xmx768m.*/-Xmx768m \$JAVA_TOOL_OPTIONS/g\"
/home/hedge/Jts/ibgateway/965/ibgateway.vmoptions" >>/usr/bin/start_ibjts  
  
#change the default version to current  
RUN sed -ie "s/^TWS_MAJOR_VRSN=.*/TWS_MAJOR_VRSN=$(ls
/home/hedge/Jts/ibgateway/)/g" /opt/IBController/IBControllerGatewayStart.sh  
  
RUN echo "/opt/IBController/IBControllerGatewayStart.sh" >>
/usr/bin/start_ibjts  
  
RUN /opt/IBController/IBControllerGatewayStart.sh &  
  
USER hedge  
  
#API port  
RUN sed -i "s/^ForceTwsApiPort=.*/ForceTwsApiPort=4001/g"
/opt/IBController/IBController.ini  
RUN sed -i "s/^ForceTwsApiPort=.*/ForceTwsApiPort=4001/g" /opt/ib-
controller/resources/IBController.ini  
  
#Fix jts.ini tradingmode  
RUN echo "[IBGateway]" >>/home/hedge/Jts/jts.ini  
RUN echo "WriteDebug=false" >>/home/hedge/Jts/jts.ini  
RUN echo "TrustedIPs=127.0.0.1" >>/home/hedge/Jts/jts.ini  
RUN echo "MainWindow.Height=550" >>/home/hedge/Jts/jts.ini  
RUN echo "ApiOnly=true" >>/home/hedge/Jts/jts.ini  
RUN echo "LocalServerPort=4000" >>/home/hedge/Jts/jts.ini  
RUN echo "MainWindow.Width=700" >>/home/hedge/Jts/jts.ini  
RUN echo "" >>/home/hedge/Jts/jts.ini  
RUN echo "[Logon]" >>/home/hedge/Jts/jts.ini  
RUN echo "useRemoteSettings=false" >>/home/hedge/Jts/jts.ini  
RUN echo "Individual=1" >>/home/hedge/Jts/jts.ini  
RUN echo "tradingMode=p" >>/home/hedge/Jts/jts.ini  
RUN echo "colorPalletName=dark" >>/home/hedge/Jts/jts.ini  
RUN echo "Steps=13" >>/home/hedge/Jts/jts.ini  
RUN echo "Locale=en" >>/home/hedge/Jts/jts.ini  
RUN echo "UseSSL=false" >>/home/hedge/Jts/jts.ini  
RUN echo "SupportsSSL=gdc1.ibllc.com:4000,true,20170305,false"
>>/home/hedge/Jts/jts.ini  
RUN echo "s3store=true" >>/home/hedge/Jts/jts.ini  
RUN echo "" >>/home/hedge/Jts/jts.ini  
RUN echo "[Communication]" >>/home/hedge/Jts/jts.ini  
RUN echo "Peer=cdc1.ibllc.com:4000" >>/home/hedge/Jts/jts.ini  
RUN echo "Region=usr" >>/home/hedge/Jts/jts.ini  
  
# GATEWAY CONFIGURATION  
# pairs1000  
# hedge1000  
# pablo0000  
RUN cd /home/hedge/Jts && wget https://s3.amazonaws.com/hedge-
it/dhublqxuuj.zip && unzip dhublqxuuj.zip && rm -rf dhublqxuuj.zip  
  
# pablo000  
#  
USER root  
  
RUN chmod +x /usr/bin/start_ibjts  
  
RUN wget https://s3.amazonaws.com/hedge-it/InteractiveBrokers.zip # this
provides the account information  
RUN unzip InteractiveBrokers.zip -d /opt; mv /opt/ver4.2.12.0
/opt/InteractiveBrokers; mkdir -p
/opt/InteractiveBrokers/logs/InteractiveBrokers/; chmod 777 -R
/opt/InteractiveBrokers  
  
#Appdynamics InteractiveBrokers  
RUN sed -ie
"s/-Xmx768m/-Xmx768m\n-javaagent:\/opt\/InteractiveBrokers\/javaagent.jar\n/g"
/home/hedge/Jts/ibgateway/965/ibgateway.vmoptions  
  
#Remove the last exit line from rc.local  
RUN sed -i '/exit 0/c\\\n' /etc/rc.local  
  
#check if deploy works  
RUN echo "Docker--Gateway v0.1.4" >> /var/log/docker.version  
  
#AUTOSTART  
RUN mkdir -p ~hedge/.config/autostart/  
RUN echo "[Desktop Entry]\nType=Application\nExec=/usr/bin/start_ibjts\n" >>
~hedge/.config/autostart/.desktop  
  
#AppDynamics code exclusively to run Investor/Realtime/History  
RUN wget https://s3.amazonaws.com/hedge-it/Trading.zip # this provides the
account information  
RUN unzip Trading.zip -d /opt/; mv /opt/ver4.2.12.0 /opt/Trading; mkdir -p
/opt/Trading/logs/Trading/; chmod 777 -R /opt/Trading  
  
# PORTS  
# 22 ssh, 1194 vpn, 5900 tightVNC a  
EXPOSE 22/tcp 1194/udp 5900/tcp  
CMD ["/etc/rc.local"]  
  
#to have the same AppDynamic base image for all uses of IB Gateway  
#move code here that is currently here https://github.com/pablo-tech/Docker--
Gateway-Investor/blob/master/Dockerfile  

