FROM redwyvern/base  
  
RUN apt-get update -q -q && \  
apt-get install --yes --force-yes runit  
  
COPY ./runsvdir-start /usr/sbin/runsvdir-start  
  
ENTRYPOINT ["/usr/sbin/runsvdir-start"]  

