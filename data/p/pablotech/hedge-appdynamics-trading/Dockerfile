FROM pablotech/hedge-appdynamics-interactivebrokers:latest  
  
#Insert here AppDynamics code exclusively to run Investor/Realtime/History  
RUN wget https://s3.amazonaws.com/hedge-it/Trading.zip # this provides the
account information  
RUN unzip Trading.zip -d /opt/; mv /opt/ver4.2.12.0 /opt/Trading; mkdir -p
/opt/Trading/logs/Trading/; chmod 777 -R /opt/Trading  
  

