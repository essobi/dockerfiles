FROM jruby:1.7  
RUN \  
apt-get update && \  
apt-get -y install cups-pdf cups-bsd && \  
rm -rf /var/lib/apt/lists/*  
COPY . /quickets  
WORKDIR quickets  
ENTRYPOINT ["containers/self/entrypoint"]  

