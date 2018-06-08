FROM mongo:3.3  
RUN useradd pl  
  
RUN set -xe \  
&& apt-get update \  
&& apt-get install -y curl \  
&& curl -qLl https://deb.nodesource.com/setup_4.x | bash - \  
&& apt-get update \  
&& apt-get install -y nodejs daemontools \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY backend /pl/backend  
COPY frontend /pl/frontend  
COPY exampleCourse /course  
COPY docker/config.json docker/start.sh /  
COPY docker/service /etc/service  
RUN chown -R pl /pl \  
&& chmod 666 /config.json \  
&& ln -sf /config.json /pl/backend/config.json \  
&& cd /pl/backend && npm install  
  
EXPOSE 3000  
ENTRYPOINT []  
CMD ["/start.sh"]  

