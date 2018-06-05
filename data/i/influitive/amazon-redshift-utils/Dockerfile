FROM python:2-onbuild  
RUN apt-get update && apt-get install -y --no-install-recommends \  
postgresql-client && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/src/app/log  
  
RUN chmod +x redshift-*.sh  
  
CMD ["/bin/bash"]  

