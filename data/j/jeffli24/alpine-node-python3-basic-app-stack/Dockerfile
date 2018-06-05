FROM jeffli24/alpine-node-python3:latest  
  
RUN apk update && apk upgrade && \  
apk add --no-cache \  
git \  
bash \  
uwsgi-python3 \  
g++ \  
linux-headers \  
postgresql-dev && \  
rm -rf /var/cache/apk/* # Delete the cache folder  
  
RUN pip3 install --no-cache-dir \  
falcon \  
SQLAlchemy \  
alembic \  
uwsgi \  
psycopg2 \  
pytz \  
requests \  
pytest \  
pytest-cov \  
coverage  
RUN rm -r /root/.cache  
  
# cut down on download times  
RUN npm set progress=false  
RUN npm install -g \  
webpack \  
protractor \  
karma \  
karma-mocha \  
karma-chai \  
karma-sinon \  
karma-coverage \  
karma-webpack \  
mocha \  
chai \  
chai-as-promised \  
sinon \  
uglify-js \  
eslint \  
eslint-config-airbnb-base \  
eslint-loader \  
eslint-plugin-import \  
eslint_d  
RUN npm cache clean --force  

