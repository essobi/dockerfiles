FROM terragontech/python  
  
MAINTAINER Terragon DCB Team <tech@terragonltd.com>  
  
RUN cd /  
  
RUN mkdir production  
RUN mkdir /var/log/tmoni/  
  
RUN cd production  
  
RUN mkdir logs  
  
WORKDIR /production  
  
ADD subscription-service/libraries /production/libraries  
ADD subscription-service/subscription_service.py
/production/subscription_service.py  
ADD subscription-service/consumer_partner_updates.py
/production/consumer_partner_updates.py  
ADD subscription-service/consumer_revenue.py /production/consumer_revenue.py  
ADD subscription-service/consumer_sercom_feedback.py
/production/consumer_sercom_feedback.py  
ADD subscription-service/consumer_billing.py /production/consumer_billing.py  
ADD subscription-service/background_active_renewal.py
/production/background_active_renewal.py  
ADD subscription-service/background_pending_renewal.py
/production/background_pending_renewal.py  
ADD subscription-service/background_utitlity.py
/production/background_utitlity.py  
ADD subscription-service/requirements.txt /production/requirements.txt  
  
RUN pip install -r requirements.txt  
  
RUN ls -larth  
  
EXPOSE 8086  
CMD python subscription_service.py  
  

