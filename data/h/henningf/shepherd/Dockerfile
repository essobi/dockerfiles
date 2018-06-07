FROM centos:7  
RUN \  
yum install -y epel-release && \  
yum install -y git python-pip python-devel libpng-devel libjpeg-devel gcc
gcc-c++ make libffi-devel openssl-devel supervisor libxml2 libxml2-devel
libxslt libxslt-devel  
  
RUN \  
pip install requests[security] pika gunicorn supervisor-stdout warctools
python-dateutil lxml pywebhdfs hapy-heritrix bagit  
  
RUN \  
cd / && git clone https://github.com/ukwa/python-shepherd.git  
  
RUN \  
cd /python-shepherd/python-warcwriterpool && \  
python setup.py install  
  
RUN \  
mkdir -p /etc/supervisor/conf.d && cd /etc/supervisor/conf.d/ && curl -OL
https://raw.githubusercontent.com/ukwa/wren/master/shepherd/supervisord.conf  
  
RUN \  
cd / && curl -OL
https://raw.githubusercontent.com/ukwa/wren/master/shepherd/setup-testrun.sh  
  
EXPOSE 8000 8001  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

