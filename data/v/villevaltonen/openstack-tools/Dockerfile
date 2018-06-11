FROM python:2.7  
ADD oscommand.sh /oscommand.sh  
  
RUN apt-get update \  
&& pip install python-openstackclient \  
&& pip install python-heatclient \  
&& chmod +x /oscommand.sh  
  
ENTRYPOINT ["/oscommand.sh"]  

