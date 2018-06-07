FROM pablotech/hedge-interactivebrokers:latest  
  
RUN wget https://s3.amazonaws.com/hedge-it/InteractiveBrokers.zip # this
provides the account information  
RUN unzip InteractiveBrokers.zip -d /opt; mv /opt/ver4.2.12.0
/opt/InteractiveBrokers; mkdir -p
/opt/InteractiveBrokers/logs/InteractiveBrokers/; chmod 777 -R
/opt/InteractiveBrokers  
  
#Appdynamics insert  
RUN sed -ie
"s/-Xmx768m/-Xmx768m\n-javaagent:\/opt\/InteractiveBrokers\/javaagent.jar\n/g"
/home/hedge/Jts/ibgateway/963/ibgateway.vmoptions  
#changes requested by pablo  
RUN sed -ie
"s/-Xmx768m/-Xmx768m\n-XX:+CMSClassUnloadingEnabled\n-XX:+UseConcMarkSweepGC\n-Dsun.net.http.allowRestrictedHeaders=true\n/g"
/home/hedge/Jts/ibgateway/963/ibgateway.vmoptions  
  
# TODO: on first run the API is in read-only mode (can't invest, even on paper
account )  
# https://www.evernote.com/l/AHvSyuclASlIhLyPhWeip1zrbOCSC0Kui0U  
# what is this?  
RUN sed -i '/exit 0/c\\\n' /etc/rc.local  
  
# AUTOSTART  
RUN mkdir -p ~hedge/.config/autostart/  
RUN echo "[Desktop Entry]\nType=Application\nExec=/usr/bin/start_ibjts\n" >>
~hedge/.config/autostart/.desktop  
  

