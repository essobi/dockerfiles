FROM buildpack-deps:jessie  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install nodejs -y \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY app /data/app  
COPY scripts/run.sh /data/  
  
RUN set -ex \  
&& groupadd -g 2567 app \  
&& useradd -rm -u 2567 -g app app \  
\  
&& chmod u+x /data/run.sh \  
\  
&& chown -R app:app /data  
  

