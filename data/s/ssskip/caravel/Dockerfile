FROM python:2.7  
MAINTAINER ssskip  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
libssl-dev \  
libffi-dev \  
python-dev \  
libsasl2-dev \  
libldap2-dev \  
&& apt-get clean -y  
  
RUN pip --no-cache-dir install caravel==0.12.0 \  
mysqlclient \  
psycopg2==2.6.1 \  
pymssql \  
sqlalchemy-redshift  
  
ENV LANG=C.UTF-8 \  
LC_ALL=C.UTF-8 \  
PATH=$PATH:/home/caravel/bin \  
PYTHONPATH=/home/caravel/caravel_config.py:$PYTHONPATH  
  
  
WORKDIR /home/caravel  
COPY caravel .  
RUN groupadd -r caravel && \  
useradd -r -m -g caravel caravel && \  
mkdir /home/caravel/db && \  
chown -R caravel:caravel /home/caravel && \  
chmod +x ./bin/*  
  
USER caravel  
  
  
  
EXPOSE 8088  
ENTRYPOINT ["caravel"]  
CMD ["runserver"]  
  

