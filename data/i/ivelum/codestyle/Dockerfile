FROM python:3.6-slim  
  
COPY requirements.txt /tmp/  
COPY package.json /tmp/  
  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends curl \  
&& curl -sL https://deb.nodesource.com/setup_8.x | bash - \  
&& apt-get update && apt-get install -y --no-install-recommends \  
git \  
nodejs \  
&& rm -rf /var/lib/apt/lists/* \  
&& npm install npm -g \  
&& pip install --no-cache-dir -r /tmp/requirements.txt \  
&& npm install -g /tmp/ \  
&& ln -s /usr/lib/node_modules/ivelum-codestyle/node_modules/.bin/eslint
/usr/bin/eslint \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' +  
  
ENV PATH /usr/local/lib/node_modules/ivelum-codestyle/node_modules/.bin:$PATH  
COPY codestyle /bin/  
RUN chmod +x /bin/codestyle  

