FROM debian:jessie  
MAINTAINER Oliver Lineham <olineham@users.noreply.github.com>  
  
COPY requirements.txt /opt/pulse/requirements.txt  
WORKDIR /opt/pulse  
  
RUN \  
DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get install \  
#-qq \  
\--yes \  
\--no-install-recommends \  
\--no-install-suggests \  
build-essential \  
libffi-dev \  
libssl-dev \  
python3-virtualenv \  
python2.7-dev \  
python3 \  
python3-dev \  
python-pip \  
  
&& python3 -m virtualenv --python=python3 venv \  
&& pip install --upgrade pip \  
&& . venv/bin/activate \  
&& pip install -r requirements.txt \  
  
&& DEBIAN_FRONTEND=noninteractive apt-get purge \  
#-qq \  
\--yes \  
build-essential \  
libffi-dev \  
libssl-dev \  
python2.7-dev \  
python3-dev \  
&& DEBIAN_FRONTEND=noninteractive apt-get autoremove --yes \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY . /opt/pulse  
ENV environment production  
EXPOSE 8000  
  
CMD . venv/bin/activate && PORT=8000 gunicorn pulse:app --log-
file=data/gunicorn.log --pid /tmp/gunicorn.pid  

