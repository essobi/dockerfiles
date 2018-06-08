FROM python:3.6-slim  
  
# Can be overriden by compose  
ARG REQUIREMENTS_FILE=requirements.txt  
  
ENV PYTHONUNBUFFERED=1  
ENV APP_HOME=/var/local/reportek/  
ENV MEDIA_ROOT=/var/local/uploads/  
ENV PROTECTED_ROOT = /var/local/protected_uploads  
ENV DOWNLOAD_STAGING_ROOT = /var/local/download_staging  
  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends apt-utils curl bzip2 netcat-
traditional lsb-release ca-certificates \  
&& sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release
-cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' \  
&& curl -sS https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
\  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN runDeps="gcc postgresql-client-10 libxml2-dev libxslt-dev libsasl2-dev
python-dev libldap2-dev libssl-dev git nodejs yarn" \  
&& apt-get update -y \  
&& apt-get install -y --no-install-recommends $runDeps \  
&& apt-get clean \  
&& rm -vrf /var/lib/apt/lists/*  
  
RUN mkdir -p $APP_HOME $MEDIA_ROOT $PROTECTED_ROOT $DOWNLOAD_STAGING_ROOT  
  
COPY yarn.lock package*.json $REQUIREMENTS_FILE $APP_HOME  
WORKDIR $APP_HOME  
  
RUN pip install --no-cache-dir -r $REQUIREMENTS_FILE  
  
RUN npm_config_tmp=$APP_HOME yarn  
  
COPY . $APP_HOME  
  
RUN npm run build  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  
CMD ["run"]  

