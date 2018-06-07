FROM ubuntu:16.04  
RUN sed -i.bak -e
"s%http://archive.ubuntu.com/ubuntu/%http://ftp.riken.jp/Linux/ubuntu/%g"
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y build-essential libssl-dev libffi-dev python-dev python-pip
libsasl2-dev libldap2-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install --no-cache-dir superset==0.22.1 psycopg2==2.7.3.2  
  
ENV SUPERSET_HOME /superset  
  
COPY docker-entrypoint.sh .  
ENTRYPOINT ["./docker-entrypoint.sh"]  
  
EXPOSE 8088  
CMD ["superset", "runserver"]  

