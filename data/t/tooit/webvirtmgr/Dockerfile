FROM ubuntu:14.04  
MAINTAINER Julian Montagna <julian.montagna@tooit.com>  
  
ENV CLIENT_IP 172.17.0.1  
ENV CLIENT_PORT 8000  
ENV CLIENT_ROOT admin  
ENV CLIENT_SECRET 1234  
ENV CLIENT_MAIL admin@example.com  
  
#v4.8.8  
ENV CLIENT_TAG 7f140f99f4  
  
RUN apt-get -y update && \  
apt-get -y install git python-pip python-libvirt python-libxml2 supervisor
novnc  
  
RUN git clone https://github.com/retspen/webvirtmgr /webvirtmgr  
  
WORKDIR /webvirtmgr  
  
RUN git checkout ${CLIENT_TAG} && pip install -r requirements.txt  
  
ADD local_settings.py /webvirtmgr/webvirtmgr/local/local_settings.py  
  
RUN sed -i 's/0.0.0.0:80/${CLIENT_IP}:${CLIENT_PORT}/g' vrtManager/create.py
&& /usr/bin/python /webvirtmgr/manage.py collectstatic --noinput  
  
ADD supervisor.webvirtmgr.conf /etc/supervisor/conf.d/webvirtmgr.conf  
ADD gunicorn.conf.py /webvirtmgr/conf/gunicorn.conf.py  
ADD bootstrap.sh /webvirtmgr/bootstrap.sh  
  
RUN useradd webvirtmgr -g libvirtd -u 1010 -d /data/vm/ -s /sbin/nologin &&
chown webvirtmgr:libvirtd -R /webvirtmgr && apt-get -ys clean  
  
WORKDIR /  
  
VOLUME /data/vm  
  
EXPOSE 8000  
EXPOSE 6080  
CMD ["supervisord", "-n"]  

