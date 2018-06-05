FROM python:3-slim  
MAINTAINER yuuki0xff <yuuki0xff@gmail.com>  
EXPOSE 8000  
VOLUME /srv  
ADD ./entrypoint /usr/local/bin  
ADD https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64
/usr/local/bin/gosu  
ADD https://github.com/shingetsu/saku/archive/master.tar.gz /opt/saku-
master.tar.gz  
  
RUN set -euv && \  
chmod +x /usr/local/bin/gosu && \  
\  
useradd saku && \  
mkdir -p /opt/saku /srv && \  
\  
cd /opt/saku && \  
tar xvf /opt/saku-master.tar.gz --strip-components=1 && \  
mv file file.original && \  
ln -s /srv/cache . && \  
ln -s /srv/file . && \  
ln -s /srv/log . && \  
ln -s /srv/run . && \  
\  
pip install markupsafe  
ADD ./saku.ini ./spam.txt /opt/saku/file.original/  
  
ENTRYPOINT ["/usr/local/bin/entrypoint"]  
CMD ["python3", "/opt/saku/saku.py"]  

