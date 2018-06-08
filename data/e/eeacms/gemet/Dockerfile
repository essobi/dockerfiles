FROM python:2.7-slim  
  
LABEL maintainer="European Environment Agency (EEA): IDM2 S-Team"  
  
ENV PROJ_DIR=/var/local/gemet  
  
RUN runDeps="gcc libmysqlclient-dev libldap2-dev libsasl2-dev libxml2-dev
libxslt1-dev netcat-traditional" \  
&& apt-get update -y \  
&& apt-get install -y --no-install-recommends $runDeps \  
&& rm -vrf /var/lib/apt/lists/*  
  
RUN mkdir -p $PROJ_DIR  
COPY . $PROJ_DIR  
WORKDIR $PROJ_DIR  
RUN mv gemet/local_settings.py.docker gemet/local_settings.py  
  
RUN pip install -r requirements-docker.txt  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  

