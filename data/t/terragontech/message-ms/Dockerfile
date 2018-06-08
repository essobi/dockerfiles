  
FROM terragontech/python  
  
MAINTAINER Terragon DCB Team <tech@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir production  
  
WORKDIR /production  
  
ADD message-service/libraries /production/libraries  
  
ADD message-service/message_service.py /production/message_service.py  
  
ADD message-service/requirements.txt /production/requirements.txt  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8089  
CMD python message_service.py  
  

