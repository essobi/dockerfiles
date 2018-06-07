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
WORKDIR /etc/uwsgi  
COPY text.ini /etc/uwsgi/  
COPY setup.py /home/nc_semantics/  
COPY text /home/nc_semantics/text  
RUN pip3 install --no-cache-dir httmock && cd /home/nc_semantics && \  
python3 setup.py test && python3 setup.py install && rm -rf * && \  
yes | pip3 uninstall httmock  
  
USER nc_semantics  
  
ENTRYPOINT ["uwsgi", "--ini", "/etc/uwsgi/text.ini"]  
  

