FROM tozd/base:ubuntu-xenial  
  
RUN apt-get update -q -q && \  
apt-get install --yes --force-yes runit  
  
COPY ./runsvdir-start /usr/local/sbin/runsvdir-start  
  
ENTRYPOINT ["/usr/local/sbin/runsvdir-start"]  

