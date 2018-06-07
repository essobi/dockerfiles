FROM python:2.7-alpine  
  
ENV AIRFLOW_HOME /airflow  
VOLUME /airflow  
EXPOSE 8080  
  
RUN set -ex \  
&& apk add --no-cache --virtual .build-deps \  
alpine-sdk \  
&& apk add --no-cache --virtual .airflow-deps \  
bash \  
libxslt \  
libxslt-dev \  
libxml2 \  
libxml2-dev \  
linux-headers \  
tzdata \  
&& ln -s /usr/include/locale.h /usr/include/xlocale.h \  
&& CFLAGS="-I/usr/include/libxml2" pip install --no-cache-dir airflow \  
&& apk del .build-deps  
  
COPY ./docker-entrypoint.sh /docker-entrypoint.sh  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["airflow", "webserver"]  

