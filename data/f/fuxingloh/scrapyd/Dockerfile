FROM python:3.5  
MAINTAINER Fuxing  
  
RUN pip install 'scrapyd>=1.1.0,<1.2.0'  
RUN pip install dateparser  
RUN mkdir /etc/scrapyd/ \  
&& echo "[scrapyd] \n bind_address = 0.0.0.0" > /etc/scrapyd/scrapyd.conf  
  
EXPOSE 6800  
CMD ["scrapyd"]  

