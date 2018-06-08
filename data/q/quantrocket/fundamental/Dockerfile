FROM quantrocket/anaconda3-uwsgi  
MAINTAINER QuantRocket <support@quantrocket.com>  
  
RUN pip install xmltodict==0.11.0  
  
ENV IBG_CLIENT_RANGE=4000 UWSGI_WORKERS=2  
COPY qrocket /tmp/uwsgi/qrocket  
COPY quantrocket.fundamental.*.schema.sql /var/opt/  
COPY reuters_estimates_indicators_data_dictionary.csv /tmp/  
COPY uwsgi /etc/uwsgi  
  
RUN mkdir -p /var/lib/quantrocket \  
&& mkdir -p /tmp/ibfundamental \  
&& mkdir -p /var/tmp/uwsgi/mule/ibfundamental \  
&& /tmp/build.sh  

