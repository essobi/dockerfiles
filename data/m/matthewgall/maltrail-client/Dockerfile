FROM matthewgall/python-dev:latest  
MAINTAINER Matthew Gall <docker@matthewgall.com>  
  
RUN apk add --update \  
libpcap-dev \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /app  
  
RUN git clone https://github.com/stamparm/maltrail.git /app  
RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt  
  
EXPOSE 22-9000  
CMD ["/env/bin/python", "sensor.py"]

