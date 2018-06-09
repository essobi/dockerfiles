  
FROM terragontech/python  
  
MAINTAINER Terragon DCB Team <tech@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir production  
  
WORKDIR /production  
ADD user-service/libraries /production/libraries  
  
ADD logs /production/logs  
  
ADD user-service/user_service.py /production/user_service.py  
  
ADD user-service/requirements.txt /production/requirements.txt  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8080  
CMD python user_service.py  
  

