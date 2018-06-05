FROM phusion/baseimage:0.9.16  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get update && \  
apt-get install -y build-essential python python-dev python-pip sqlite3
libsqlite3-dev  
  
ADD requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
RUN mkdir /etc/luigi  
ADD luigi.cfg /etc/luigi/luigi.cfg  
  
RUN mkdir /var/log/luigid  
ADD logrotate.cfg /etc/logrotate.d/luigid  
VOLUME /var/log/luigid  
  
RUN mkdir /etc/service/luigid  
ADD luigid.sh /etc/service/luigid/run  
  
EXPOSE 8082  
CMD ["/sbin/my_init"]  

