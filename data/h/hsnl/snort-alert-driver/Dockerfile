FROM linton/snort-base  
  
MAINTAINER John Lin <linton.tw@gmail.com>  
  
RUN apt-get update && \  
apt-get install -y \  
python-setuptools \  
python-pip \  
supervisor \  
vim && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
ENV HOME /root  
  
ADD . snort_alert_driver  
  
RUN pip install -r snort_alert_driver/requirements.txt  
  
# Define working directory.  
WORKDIR /opt/snort_alert_driver  
  
CMD ["/usr/bin/supervisord"]  

