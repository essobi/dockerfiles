FROM gone/base:latest  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - && \  
apt-get -yq install --no-install-recommends \  
nodejs && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /etc/service/nodejs  
COPY run.nodejs.sh /etc/service/nodejs/run  
  
RUN chmod +x /etc/service/*/run  
  
EXPOSE 80  
# On build, add anything in with Dockerfile into /app  
ONBUILD ADD ./ /app  

