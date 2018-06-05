FROM terragontech/python  
  
MAINTAINER Terragon DCB Team <tech@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir production  
  
WORKDIR /production  
ADD airtel_service/libraries /production/libraries  
  
ADD airtel_service/templates /production/templates  
  
ADD airtel_service/static /production/static  
  
ADD airtel_service/api_entry.py /production/api_entry.py  
  
ADD airtel_service/requirements.txt /production/requirements.txt  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8080  
CMD python api_entry.py  

