FROM python:alpine  
  
ARG VERSION=3.9  
ENV PUID=1000 PGID=1000  
RUN apk add --no-cache openssl su-exec && \  
wget -O- https://github.com/wking/rss2email/archive/v$VERSION.tar.gz \  
| tar zx && \  
pip install -q --no-cache-dir html2text feedparser && \  
cd rss2email-$VERSION && \  
python setup.py install && \  
cd / && \  
rm -rf rss2email-$VERSION  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

