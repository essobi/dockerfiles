FROM ruby:2.3.3  
ENV APP_HOME /myapp/  
WORKDIR $APP_HOME  
  
ENV BUNDLE_JOBS=3  
ENV BUNDLE_RETRY=3  
ENV POSTGRES_ENV_POSTGRES_DB=innovate  
ENV POSTGRES_ENV_POSTGRES_USER=postgres  
ENV POSTGRES_ENV_POSTGRES_PASSWORD=postgres  
ENV POSTGRES_DB=innovate  
ENV POSTGRES_USER=postgres  
ENV POSTGRES_PASSWORD=postgres  
ENV LOG_LEVEL=warn  
ENV PHANTOMJS_CDNURL=http://luma-app-production.s3.amazonaws.com  
ENV CAPYBARA_DEFAULT_WAIT_TIME=5  
COPY ubuntu-common.sh $APP_HOME/  
COPY ubuntu-bootstrap-deps.sh $APP_HOME/  
  
COPY ubuntu-bootstrap-app-deps.sh $APP_HOME/  
COPY Gemfile $APP_HOME/  
COPY Gemfile.lock $APP_HOME/  
COPY .ruby-version $APP_HOME/  
COPY package.json $APP_HOME/  
COPY yarn.lock $APP_HOME/  
COPY postinstall.sh $APP_HOME/  
COPY frontend/package.json $APP_HOME/frontend/  
COPY frontend/yarn.lock $APP_HOME/frontend/  
COPY frontend/bower.json $APP_HOME/frontend/  
COPY frontend/postinstall.sh $APP_HOME/frontend/  
  
RUN ./ubuntu-bootstrap-deps.sh  
  
RUN mkdir -p $APP_HOME/frontend/  
RUN ./ubuntu-bootstrap-app-deps.sh  

