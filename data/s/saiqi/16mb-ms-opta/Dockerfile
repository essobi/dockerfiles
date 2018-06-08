FROM saiqi/16mb-platform:latest  
  
RUN pip install python-dateutil pytz lxml  
  
RUN mkdir /service  
ADD application /service/application  
ADD ./cluster.yml /service  
  
WORKDIR /service  

