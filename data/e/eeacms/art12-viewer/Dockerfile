FROM python:2.7-slim  
MAINTAINER "EEA: IDM2 C-TEAM" <eea-edw-c-team-alerts@googlegroups.com>  
  
ENV WORK_DIR=/var/local/art12  
ENV DATA_DIR=/var/local/art12-data  
  
RUN runDeps="curl vim build-essential netcat mysql-client libmysqlclient-dev
python-dev libldap2-dev libsasl2-dev libssl-dev libxrender1 libfontconfig1
libxext6" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $runDeps \  
&& rm -vrf /var/lib/apt/lists/*  
  
RUN curl -OL
https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-
amd64.tar.xz \  
&& tar -xvf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \  
&& cp -r wkhtmltox/* /usr/local/ \  
&& rm -R wkhtmltox \  
&& rm wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
  
COPY . $WORK_DIR/  
WORKDIR $WORK_DIR  
  
RUN mkdir $WORK_DIR/logs \  
&& mkdir -p $DATA_DIR/maps \  
&& mkdir -p $DATA_DIR/factsheets \  
&& ln -s $DATA_DIR/maps $WORK_DIR/art12/static/maps \  
&& ln -s $DATA_DIR/factsheets $WORK_DIR/art12/static/factsheets  
  
RUN pip install -U setuptools \  
&& pip install -r requirements-dep.txt --trusted-host eggshop.eaudeweb.ro \  
&& mv docker-entrypoint.sh /bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

