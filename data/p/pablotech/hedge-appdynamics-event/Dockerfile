FROM pablotech/hedge-j2se:latest  
  
# AppDynamics for Web apps a  
#WORKDIR /root  
RUN wget https://s3.amazonaws.com/hedge-it/Event.zip # this provides the
account information  
RUN unzip Event.zip -d /opt; mv /opt/ver4.2.12.0 /opt/Event; mkdir -p
/opt/Event/logs/Event/; chmod 777 -R /opt/Event  
  

