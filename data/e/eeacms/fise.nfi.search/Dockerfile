FROM python:3.6-slim as npm_builder  
ENV APP_HOME=/var/local/fise.nfi.search  
RUN apt-get update -y \  
&& apt-get install -y --no-install-recommends curl \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN runDeps="nodejs yarn" \  
&& apt-get update -y \  
&& apt-get install -y --no-install-recommends $runDeps  
RUN mkdir -p $APP_HOME/frontend  
COPY frontend $APP_HOME/frontend/  
COPY package.json postcss.config.js yarn.lock $APP_HOME/  
WORKDIR $APP_HOME  
RUN npm_config_tmp=$APP_HOME yarn  
RUN npm run build  
  
FROM python:3.6-slim  
ARG REQUIREMENTS_FILE=requirements.dep.txt  
ENV APP_HOME=/var/local/fise.nfi.search  
RUN runDeps="netcat libpq-dev" \  
&& apt-get update -y \  
&& apt-get install -y --no-install-recommends $runDeps \  
&& apt-get clean \  
&& rm -vrf /var/lib/apt/lists/*  
RUN mkdir -p $APP_HOME  
COPY requirements.txt $REQUIREMENTS_FILE $APP_HOME/  
WORKDIR $APP_HOME  
RUN pip install --no-cache-dir -r $REQUIREMENTS_FILE  
COPY \--from=npm_builder $APP_HOME/frontend/dist/build/ $APP_HOME/static/  
COPY \--from=npm_builder $APP_HOME/webpack-stats.json $APP_HOME  
COPY . $APP_HOME  
RUN rm -rf $APP_HOME/frontend package.json postcss.config.js yarn.lock  
  
ENTRYPOINT ["./docker-entrypoint.sh"]  
CMD ["run"]  
  

