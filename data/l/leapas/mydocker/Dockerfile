FROM ciyinhuang/ubuntu-python  
MAINTAINER zhoucen <zhocuencl@gmail.com>  
# Install python-lib  
RUN \  
apt-get update && \  
apt-get install supervisor -y && \  
apt-get install python-pip -y && \  
apt-get install python-dev -y && \  
apt-get install libxml2-dev libxslt1-dev lib32z1-dev libffi-dev libssl-dev -y
&& \  
pip install gevent==1.0.2 Flask==0.10.1 requests==2.4.3 gunicorn==19.1.0
scrapy==0.24 elasticsearch leap-sdk  
  
# Add supervisord conf, bootstrap.sh files  
ADD files /  
  
EXPOSE 5000  
  
WORKDIR /opt/src  
  
RUN echo "*/1 * * * * root cd /opt/src/ && /usr/bin/python crontab_task.py" >>
/etc/crontab  
RUN chmod +x /etc/crontab  
  
CMD ["/config/bootstrap.sh"]  

