FROM alpine  
  
# expose web server port  
# only http, for ssl use reverse proxy  
EXPOSE 80  
#build tools for Flask-SQLAlchemy-->cffi  
RUN apk add --no-cache bash git nginx uwsgi uwsgi-python3 python3-dev libffi-
dev alpine-sdk postgresql-dev \  
&& pip3 install --upgrade pip  
  
# application folder  
ENV APP_DIR /app  
VOLUME [ "/app/migrations", "/app/config" ]  
  
# app dir  
COPY webapp ${APP_DIR}/webapp  
COPY .git/refs/heads/master ${APP_DIR}/version.txt  
COPY app.ini app.py config.py.example entrypoint.sh manage.py requirements.txt
${APP_DIR}/  
COPY nginx.conf /etc/nginx/nginx.conf  
RUN chmod 777 -R /run/  
WORKDIR ${APP_DIR}  
  
RUN pip3 install -r requirements.txt  
  
# exectute start up script  
ENTRYPOINT ["/app/entrypoint.sh"]  

