FROM squareone/uwsgi  
RUN apt-get update && \  
apt-get install -y libpq-dev && \  
rm -rf /var/lib/apt/lists/*  
  
  
ADD requirements.txt /srv/app/requirements.txt  
RUN pip3 install -r /srv/app/requirements.txt

