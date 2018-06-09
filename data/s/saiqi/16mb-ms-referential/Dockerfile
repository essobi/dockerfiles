FROM saiqi/16mb-platform:latest  
  
RUN pip install python-dateutil  
  
RUN mkdir /service  
ADD application /service/application  
ADD ./cluster.yml /service  
  
WORKDIR /service  

