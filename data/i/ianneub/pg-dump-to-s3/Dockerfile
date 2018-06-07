FROM ubuntu:14.04  
RUN apt-get update && apt-get install --no-install-recommends -y postgresql-
client-9.3 python-pip && \  
pip install awscli && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PGDUMP_OPTIONS -Fc --no-acl --no-owner  
ENV PGDUMP_DATABASE **None**  
  
ENV AWS_ACCESS_KEY_ID **None**  
ENV AWS_SECRET_ACCESS_KEY **None**  
ENV AWS_BUCKET **None**  
  
ENV PREFIX **None**  
  
ADD run.sh /run.sh  
RUN chmod +x /run.sh  
  
CMD ["/run.sh"]  

