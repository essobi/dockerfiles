FROM python:2-alpine  
MAINTAINER Freeletics GmbH <operations@freeletics.com>  
  
RUN pip install --upgrade pip  
RUN pip install boto  
COPY elb-presence.py /bin/elb-presence  
  
CMD /bin/elb-presence  

