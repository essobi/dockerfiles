FROM alpine:edge  
RUN adduser -D nc_semantics && \  
apk update && apk upgrade && \  
apk add --no-cache python3 py3-lxml uwsgi-python3 libjpeg-turbo && \  
apk add --no-cache --virtual=.build.dep musl-dev gcc python3-dev libjpeg-
turbo-dev zlib-dev && \  
pip3 install --no-cache-dir nltk && \  
pip3 install --no-cache-dir newspaper3k flask && \  
apk del .build.dep && \  
rm /var/cache/apk/*  
  
# newspaper (text extractor from URL needs access to user home directory.  
# This behavior doesn't work well with uwsgi.)  
USER nc_semantics  
WORKDIR /etc/uwsgi  
COPY *.py *.ini site_specific_parsing.csv /etc/uwsgi/  
COPY site_plugins /etc/uwsgi/site_plugins/  
  
ENTRYPOINT ["uwsgi", "--ini", "/etc/uwsgi/text.ini"]  
  

