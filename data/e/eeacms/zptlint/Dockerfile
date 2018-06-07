FROM python:2-alpine  
MAINTAINER "EEA: IDM2 A-Team" <eea-edw-a-team-alerts@googlegroups.com>  
  
ENV ZPTLINT_VERSION=0.2.5rc2  
  
RUN apk add --no-cache --virtual .build-deps gcc musl-dev \  
&& apk add --no-cache --virtual .run-deps git \  
&& git clone https://github.com/eea/zptlint.git /tmp/zptlint \  
&& cd /tmp/zptlint \  
&& git checkout $ZPTLINT_VERSION \  
&& cd / \  
&& pip install /tmp/zptlint \  
&& apk del .build-deps \  
&& rm -rf /tmp/zptlint \  
&& mkdir -p /code  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["zptlint"]  

