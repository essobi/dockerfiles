FROM terragontech/python  
  
MAINTAINER Terragon DCB Team <tech@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir production  
  
WORKDIR /production  
ADD partner_microservice/libraries /production/libraries  
  
ADD logs /production/logs  
  
ADD partner_microservice/partner.py /production/partner.py  
  
ADD partner_microservice/requirements.txt /production/requirements.txt  
  
RUN pip install -r requirements.txt  
  
EXPOSE 8081  
CMD python partner.py  

