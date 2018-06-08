FROM terragontech/python  
  
MAINTAINER Terragon DCB Team <tech@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir production  
  
WORKDIR /production  
  
ADD safaricom_ad/libraries /production/libraries  
  
ADD safaricom_ad/templates /production/templates  
  
ADD safaricom_ad/static /production/static  
  
ADD safaricom_ad/api /production/api  
  
ADD safaricom_ad/app.py /production/app.py  
  
ADD safaricom_ad/requirements.txt /production/requirements.txt  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8081  
CMD python app.py  

