FROM node AS admin-ui  
  
COPY admin/package.json /src/package.json  
RUN cd /src && npm install  
  
COPY admin/public /src/public  
COPY admin/src /src/src  
RUN cd /src && npm run build  
  
FROM node AS login-ui  
  
COPY login-ui/package.json /src/package.json  
RUN cd /src && npm install  
  
COPY login-ui/public /src/public  
COPY login-ui/src /src/src  
RUN cd /src && npm run build  
  
FROM python:3.6  
ENV PYTHONUNBUFFERED 1  
RUN groupadd -r flask && useradd -r -g flask flask  
RUN mkdir -p /app/var/audit && chown flask: /app/var/audit  
  
COPY ./requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt  
  
COPY . /app/src  
RUN pip install -r /app/src/requirements.txt -e /app/src  
  
COPY \--from=admin-ui /src/build/asset-manifest.json /app/admin-ui/asset-
manifest.json  
COPY \--from=admin-ui /src/build/static /app/admin-ui/static  
  
COPY \--from=login-ui /src/build/asset-manifest.json /app/login-ui/asset-
manifest.json  
COPY \--from=login-ui /src/build/static /app/login-ui/static  
  
COPY ./docker/flask/gunicorn.conf /app/etc/gunicorn.conf  
COPY ./docker/flask/logging.conf /app/etc/logging.conf  
  
COPY ./docker/flask/gunicorn.sh /gunicorn.sh  
COPY ./docker/flask/entrypoint.sh /entrypoint.sh  
  
RUN sed -i 's/\r//' /entrypoint.sh \  
&& sed -i 's/\r//' /gunicorn.sh \  
&& chown flask /entrypoint.sh \  
&& chown flask /gunicorn.sh  
  
WORKDIR /app/src  
  
USER flask  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/gunicorn.sh"]  

