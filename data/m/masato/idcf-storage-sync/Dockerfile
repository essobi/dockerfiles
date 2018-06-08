FROM ubuntu:14.04.1  
MAINTAINER Masato Shimizu <ma6ato@gmail.com>  
  
ENV LANG ja_JP.UTF-8  
RUN locale-gen ja_JP.UTF-8 && \  
update-locale LANG=ja_JP.UTF-8 && \  
ln -sf /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -qy \  
python-setuptools python-dateutil python-magic git  
  
RUN git clone https://github.com/s3tools/s3cmd.git /s3cmd && \  
cd /s3cmd && python setup.py install  
  
ADD run.sh /run.sh  
ADD s3cfg /.s3cfg  
CMD ["/run.sh"]  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

