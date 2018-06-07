FROM ubuntu:15.04  
RUN echo "deb http://archive.ubuntu.com/ubuntu vivid multiverse\n" >>
/etc/apt/sources.list  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && apt-get install -fy --force-yes --no-install-recommends
\  
python-pip \  
libpq-dev \  
python-dev \  
postgresql-client-common \  
postgresql-client-9.4 \  
build-essential \  
cron \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
WORKDIR /frontend  
COPY kitling /frontend/kitling  
COPY videos /frontend/videos  
COPY templates /frontend/templates  
COPY manage.py /frontend/manage.py  
COPY refreeze.sh /frontend/refreeze.sh  
COPY wait-for-postgres.sh /frontend/wait-for-postgres.sh  
EXPOSE 8000  
ENV PGPASSWORD mysecretpassword  
CMD ./wait-for-postgres.sh postgres && python manage.py migrate && python
manage.py crontab add && /etc/init.d/cron start && python manage.py runserver
0.0.0.0:8000  

