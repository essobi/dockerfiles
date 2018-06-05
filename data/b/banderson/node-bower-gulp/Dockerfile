FROM digitallyseamless/nodejs-bower-grunt  
  
RUN apt-get update \  
&& apt-get install -y libnotify-bin libnotify-dev apt-transport-https ca-
certificates \  
&& npm install -g gulp \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt-get update && apt-get install yarn \  
&& rm -rf /var/lib/apt/lists/*  

