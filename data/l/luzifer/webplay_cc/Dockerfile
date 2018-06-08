FROM luzifer/php5-nginx  
  
RUN mkdir -p /application  
ADD . /application  
  
RUN apt-get update && apt-get install -y git-core && \  
cd /application && git submodule update --init --recursive && \  
apt-get purge -y git-core && apt-get autoremove -y  
  
EXPOSE 80  
CMD ["/usr/local/bin/container-run.sh"]  

