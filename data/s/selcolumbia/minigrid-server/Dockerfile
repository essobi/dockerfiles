FROM python:3.6  
COPY . /minigrid-server  
WORKDIR /minigrid-server  
RUN set -x \  
&& curl -sL https://deb.nodesource.com/setup_7.x | bash \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/* \  
&& npm install \  
&& node node_modules/webpack/bin/webpack.js  
RUN set -x \  
&& pip install --no-cache-dir -r requirements.txt \  
&& useradd -r -d /minigrid-server -s /sbin/nologin minigrid-server \  
&& chown -R minigrid-server:minigrid-server .  
USER minigrid-server  
CMD ["./prod/run.sh"]  
EXPOSE 8889  

