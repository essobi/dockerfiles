FROM alpine:3.5  
# Install basic stuff =)  
RUN apk add --no-cache \  
bash \  
ca-certificates \  
nginx \  
openssl \  
py2-pip \  
supervisor \  
tini \  
&& pip install \  
supervisor-stdout \  
gunicorn  
  
# Install graphite  
ENV GRAPHITE_ROOT /opt/graphite  
  
RUN apk add --no-cache \  
alpine-sdk \  
fontconfig \  
libffi \  
libffi-dev \  
python-dev \  
py-cairo \  
&& export PYTHONPATH="/opt/graphite/lib/:/opt/graphite/webapp/" \  
&& pip install https://github.com/graphite-project/whisper/tarball/1.1.x \  
&& pip install https://github.com/graphite-project/carbon/tarball/1.1.x \  
&& pip install https://github.com/graphite-project/graphite-web/tarball/1.1.x
\  
&& apk del \  
alpine-sdk \  
python-dev \  
libffi-dev  
  
EXPOSE 8080  
EXPOSE 2003  
EXPOSE 2004  
EXPOSE 7002  
VOLUME ["/opt/graphite/conf", "/opt/graphite/storage"]  
  
COPY run.sh /run.sh  
COPY etc/ /etc/  
COPY conf/ /opt/graphite/conf.example/  
  
# Enable tiny init  
ENTRYPOINT ["/sbin/tini", "--"]  
CMD ["/bin/bash", "/run.sh"]  

