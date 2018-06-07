FROM centos:7  
RUN \  
yum install -y curl https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm https://centos7.iuscommunity.org/ius-release.rpm  
  
RUN \  
mkdir -p /opt/jumpserver /opt/coco /opt/luna;\  
curl -fsSL "https://github.com/jumpserver/jumpserver/archive/1.3.0.tar.gz" |
tar -zxvf - --strip-components=1 -C /opt/jumpserver;\  
curl -fsSL "https://github.com/jumpserver/coco/archive/1.3.0.tar.gz" | tar
-zxvf - --strip-components=1 -C /opt/coco;\  
curl -fsSL
"https://github.com/jumpserver/luna/releases/download/v1.0.0/luna.tar.gz" |
tar -zxvf - --strip-components=1 -C /opt/luna  
  
RUN \  
yum install -y gcc nginx redis supervisor python36u python36u-devel
python36u-pip &&\  
yum install -y $(cat /opt/jumpserver/requirements/rpm_requirements.txt) && yum
install -y $(cat /opt/coco/requirements/rpm_requirements.txt) &&\  
ln -s /usr/bin/python3.6 /usr/bin/python3  
  
RUN \  
pip3.6 install -r /opt/jumpserver/requirements/requirements.txt && pip3.6
install -r /opt/coco/requirements/requirements.txt  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY supervisord.conf /etc/supervisord.conf  
COPY jumpserver_conf.py /opt/jumpserver/config.py  
COPY coco_conf.py /opt/coco/conf.py  
  
## Scripts  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod a+x /docker-entrypoint.sh  
  
EXPOSE 2222 80  
VOLUME ["/opt/jumpserver/data"]  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["supervisord"]  

