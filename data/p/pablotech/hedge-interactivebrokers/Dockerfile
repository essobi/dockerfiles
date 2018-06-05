FROM pablotech/hedge-j2se:latest  
  
#IBGateway download  
RUN wget https://download2.interactivebrokers.com/installers/ibgateway/latest-
standalone/ibgateway-latest-standalone-linux-x64.sh  
RUN mv ibgateway-latest-standalone-linux-x64.sh /opt; chmod +x /opt/ibgateway-
latest-standalone-linux-x64.sh  
#IBGateway install  
RUN echo "n" | su - hedge -c "/opt/ibgateway-latest-standalone-linux-x64.sh"  
#RUN mv /root/Jts /home/hedge/  
#RUN chown -R hedge: /home/hedge/Jts  
#IBController download  
RUN git clone https://github.com/ib-controller/ib-controller.git /opt/ib-
controller  
  
#IBController install  
RUN mkdir -p /opt/IBController  
RUN cp -R /opt/ib-controller/resources/* /opt/IBController/  
RUN chmod +x /opt/IBController/IBControllerGatewayStart.sh  
RUN chmod +x /opt/IBController/Scripts/*  
RUN ln -s /opt/IBController/ /home/hedge/  
  
#add the IBGw into X starting procedures  
RUN echo '#!/bin/bash' > /usr/bin/start_ibjts  
RUN echo '. /etc/auth' >> /usr/bin/start_ibjts  
RUN echo /opt/IBController/IBControllerGatewayStart.sh >> /usr/bin/start_ibjts  
RUN /opt/IBController/IBControllerGatewayStart.sh &  
RUN chmod +x /usr/bin/start_ibjts  
  
RUN sed -i '10s/^/\necho "export IBLOGIN=$IBLOGIN" >>\/etc\/auth\n/'
/etc/rc.local  
RUN sed -i '10s/^/\necho "export IBPASS=$IBPASS" >\/etc\/auth\n/'
/etc/rc.local  
  
RUN sed -i '10s/^/\nsu - hedge -c "touch \/home\/hedge\/.Xresources"\n/'
/etc/rc.local  
  
RUN export IBLOGIN=$IBLOGIN  
RUN export IBPASS=$IBPASS  
RUN echo $IBLOGIN >> /tmp/bla  
RUN echo $IBPASS >> /tmp/bla  
  
#change the default version to current  
RUN sed -ie "s/TWS_MAJOR_VRSN=$(cat
/opt/IBController/IBControllerGatewayStart.sh | grep -i TWS_MAJOR_VRSN= | cut
-d '=' -f2)/TWS_MAJOR_VRSN=$(ls /home/hedge/Jts/ibgateway/) /g"
/opt/IBController/IBControllerGatewayStart.sh  
  
#change the default user  
RUN sed -ie "s/IbLoginId=$(cat /opt/IBController/IBController.ini| grep -i
IbLoginId= | cut -d '=' -f2)/IbLoginId=$IBLOGIN /g"
/opt/IBController/IBController.ini  
  
#change the default pass  
RUN sed -ie "s/IbPassword=$(cat /opt/IBController/IBController.ini| grep -i
IbPassword= | cut -d '=' -f2)/IbPassword=$IBPASS /g"
/opt/IBController/IBController.ini  
  
#changes requested by pablo  
RUN sed -ie
"s/-Xmx768m/-Xmx768m\n-XX:+CMSClassUnloadingEnabled\n-XX:+UseConcMarkSweepGC\n-Dsun.net.http.allowRestrictedHeaders=true\n/g"
/home/hedge/Jts/ibgateway/*/ibgateway.vmoptions  
  
# PORTS  
# 22 ssh, 1194 vpn, 5900 tightVNC a  
EXPOSE 22/tcp 1194/udp 5900/tcp  
  
CMD ["/etc/rc.local"]  
  

