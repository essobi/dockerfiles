FROM nginx  
  
COPY / /src  
WORKDIR /src  
  
RUN apt-get update \  
&& apt-get install -y curl git build-essential \  
&& curl -sL https://deb.nodesource.com/setup_0.12 | bash - \  
&& apt-get install -y nodejs \  
&& npm install -g gulp bower \  
&& npm install \  
&& bower install --allow-root \  
&& gulp build --env=${NODE_ENV:-prod} \  
&& cp -rp dist/* /usr/share/nginx/html \  
&& apt-get remove -y curl git build-essential nodejs apt-transport-https \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/* /tmp/npm-* /usr/lib/node_modules /usr/bin/bower
/usr/bin/gulp /src /root/.cache /root/.node-* /root/.npm  
  
EXPOSE 80 443  

