FROM python:3.6.3-alpine3.6  
ENV PYTHONUNBUFFERED 1  
ENV INSTALL_PATH /kubernetes-envoy-discovery  
RUN mkdir -p $INSTALL_PATH  
  
WORKDIR $INSTALL_PATH  
  
COPY requirements/prod.txt requirements.txt  
RUN apk add --no-cache --virtual .build-deps \  
build-base \  
&& pip install -r requirements.txt \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .rundeps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/*  
  
COPY ./run.py run.py  
COPY ./envoy_discovery_service envoy_discovery_service  
  
EXPOSE 5000  
CMD python3 run.py  

