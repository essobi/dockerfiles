FROM andriyg/python2.7:xenial-nonginx  
  
ADD src /teatr/src  
ADD media /teatr/media  
ADD templates /teatr/templates  
  
ADD requirements.txt /tmp/  
  
RUN \  
groupadd teatr -g 1007 && useradd -g teatr --uid 1007 -m teatr && \  
pip install -U -r /tmp/requirements.txt && \  
echo yes | python2.7 /teatr/src/manage.py collectstatic && \  
chown -R :teatr /teatr/ && \  
mkdir -p /var/log/teatr/ && \  
rm -Rf /root/.cache && \  
true  
  
ADD docker/uwsgi.ini /teatr  
  
ADD docker/start.sh /teatr/  
  
USER teatr  
  
EXPOSE 8000  
CMD ["/bin/bash", "/teatr/start.sh"]  
  
VOLUME /teatr/media/kol  

