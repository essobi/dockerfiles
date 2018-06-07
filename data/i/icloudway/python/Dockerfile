FROM python:3.4-slim  
  
RUN apt-get update && apt-get install -y \  
gcc \  
gettext \  
python-dev \  
python-pip \  
mysql-client libmysqlclient-dev \  
postgresql-client libpq-dev \  
sqlite3 \  
nginx \  
supervisor \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
RUN pip2 install mysqlclient psycopg2 \  
&& pip3 install mysqlclient psycopg2 \  
&& pip2 install uwsgi && mv /usr/local/bin/uwsgi /usr/local/bin/uwsgi2 \  
&& pip3 install uwsgi && mv /usr/local/bin/uwsgi /usr/local/bin/uwsgi3 \  
&& ln -sf /usr/local/bin/uwsgi3 /usr/local/bin/uwsgi \  
&& pip install virtualenv  
  
ENV PIP_INDEX_URL https://pypi.douban.com/simple  

