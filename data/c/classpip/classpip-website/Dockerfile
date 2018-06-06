FROM ghost:0.11.4  
MAINTAINER Ferran Vila ferran.vila.conesa@gmail.com  
  
# Install new relic agent  
RUN set -x \  
&& npm install newrelic \  
&& echo "exports.config = { app_name: ['classpip-website'], license_key:
process.env.NEW_RELIC_TOKEN, logging: {level: 'info'}}" > newrelic.js \  
&& echo "require('newrelic');" | cat - index.js > temp && mv temp index.js  

