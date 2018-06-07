FROM python:2.7  
MAINTAINER Sylvain Roy "sylvain.roy@m4x.org"  
ENV REFRESHED_AT 09aug15  
  
RUN mkdir /var/peoplestore  
ADD . /var/peoplestore  
  
RUN pip install -r /var/peoplestore/requirements.txt  
  
WORKDIR /var/peoplestore  
CMD python /var/peoplestore/app.py  
  
EXPOSE 8000  

