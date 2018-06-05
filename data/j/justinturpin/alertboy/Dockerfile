FROM python:3.6-alpine  
  
RUN apk add --no-cache nagios-plugins  
  
ENV PATH="$PATH:/usr/lib/nagios/plugins"  
WORKDIR /opt  
  
COPY requirements.txt requirements.txt  
  
RUN pip install -r requirements.txt  
  
COPY alertboy.py alertboy.py  
  
CMD ["python3", "-u", "alertboy.py"]  

