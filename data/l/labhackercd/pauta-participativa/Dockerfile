FROM labhackercd/alpine-python3-nodejs  
  
ENV BUILD_PACKAGES postgresql-dev postgresql-client gettext  
  
RUN apk add --update --no-cache $BUILD_PACKAGES  
RUN mkdir -p /var/labhacker/pauta-participativa  
  
ADD . /var/labhacker/pauta-participativa  
WORKDIR /var/labhacker/pauta-participativa  
  
RUN pip3 install -r requirements.txt psycopg2 gunicorn && \  
rm -r /root/.cache  
  
RUN npm install  
  
WORKDIR /var/labhacker/pauta-participativa/src  
RUN python3 manage.py collectstatic_js_reverse && \  
python3 manage.py compress --force && \  
python3 manage.py collectstatic --no-input && \  
python3 manage.py compilemessages  
  
EXPOSE 8000  
CMD ./start.sh  

