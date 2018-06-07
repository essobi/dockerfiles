FROM python:2.7-slim  
  
ARG REQUIREMENTS_FILE=requirements-dep.txt  
  
ENV APP_HOME=/var/local/meetings/  
  
RUN runDeps="curl vim build-essential netcat libpq-dev libxml2-dev
libxslt1-dev libjpeg-dev libxrender1 libfontconfig libxtst6" \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends $runDeps \  
&& curl -o /tmp/wkhtmltopdf.tgz -SL
https://svn.eionet.europa.eu/repositories/Zope/trunk/wk/wkhtmltopdf-0.12.2.4.tgz
\  
&& tar -zxvf /tmp/wkhtmltopdf.tgz -C /tmp/ \  
&& mv -v /tmp/wkhtmltopdf /usr/bin/ \  
&& apt-get clean \  
&& rm -vrf /var/lib/apt/lists/* \  
&& rm -vrf /tmp/*  
  
COPY requirements.txt $REQUIREMENTS_FILE $APP_HOME  
WORKDIR $APP_HOME  
  
RUN pip install -r $REQUIREMENTS_FILE \  
&& mkdir -p $APP_HOME/instance/files  
  
COPY . $APP_HOME  
  
RUN pybabel compile -d mrt/translations \  
&& mv settings.example instance/settings.py \  
&& mv ./docker/docker-entrypoint.sh /bin/  
  
ENTRYPOINT ["docker-entrypoint.sh"]  

