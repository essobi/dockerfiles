FROM alpine:3.5  
RUN apk add --no-cache \  
py-pip \  
py-raven \  
py-requests \  
py-redis \  
py2-pyldap \  
python \  
curl \  
bash \  
py-gunicorn  
  
ENV VISUAL=vi WORKER_COUNT=8 TIMEOUT=300  
RUN pip --disable-pip-version-check --no-cache-dir install \  
elasticsearch \  
filelock \  
flask \  
flask-cors \  
flask_restful \  
huey  
  
# ENV HUEY_VERSION=1fbffc7d8ea099bb195d8cb0b4c8841e9fb13ce6  
# RUN apk add --no-cache git && git clone https://github.com/coleifer/huey.git
/tmp/huey && cd /tmp/huey && git checkout $HUEY_VERSION && python setup.py
install && rm -rf /tmp/huey  
RUN mkdir /data && mkdir /input && mkdir /app && mkdir /app/tasks && mkdir
/app/scripts  
VOLUME ["/data", "/input"]  
  
COPY *.py /app/  
COPY scripts/* /app/scripts/  
COPY tasks/* /app/tasks/  
  
WORKDIR /app  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["server"]  

