FROM terragontech/python  
  
MAINTAINER Terragon DCB Team <tech@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir production  
  
WORKDIR /production  
  
ADD safaricom_service/libraries /production/libraries  
  
ADD safaricom_service/templates /production/templates  
  
ADD safaricom_service/static /production/static  
  
ADD safaricom_service/api_entry.py /production/api_entry.py  
  
ADD safaricom_service/requirements.txt /production/requirements.txt  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8080  
CMD python api_entry.py  

