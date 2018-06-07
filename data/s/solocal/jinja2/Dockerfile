FROM python:3-alpine3.6  
RUN pip install --upgrade pip && \  
pip install \  
PyYAML \  
Jinja2 \  
httplib2 \  
urllib3 \  
simplejson  
  
## Expose some volumes  
VOLUME ["/data", "/out"]  
  
ENV APP_DIR /app  
ENV TEMPLATES_DIR /data  
ENV OUT_DIR /out  
ENV TEMPLATE my.tmpl  
  
RUN mkdir ${APP_DIR}  
  
COPY render.py ${APP_DIR}/render.py  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
WORKDIR /data  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

