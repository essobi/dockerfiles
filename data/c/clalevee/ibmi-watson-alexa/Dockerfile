FROM openwhisk/action-nodejs-v8  
  
WORKDIR /nodejsAction  
  
# See https://crbug.com/795759  
# Install latest chrome dev package.  
# Note: this installs the necessary libs to make the bundled version of
Chromium that Pupppeteer  
# installs, work.  
RUN apt-get update && apt-get install -yq libgconf-2-4 \  
&& apt-get install -y wget --no-install-recommends \  
&& wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add \- \  
&& sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable
main" >> /etc/apt/sources.list.d/google.list' \  
&& apt-get update \  
&& apt-get install -y google-chrome-unstable \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get purge --auto-remove -y curl \  
&& rm -rf /src/*.deb  
  
RUN npm install \  
alexa-verifier@0.3.6 \  
@cloudant/cloudant@2.1.0 \  
request@2.83.0 \  
watson-developer-cloud@2.32.1 \  
ovh@2.0.1 \  
@sendgrid/mail@6.2.1 \  
&& npm cache clean --force  

