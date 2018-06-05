FROM python:2.7-slim  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
# this list of deps is taken from the alarmdecoder README, with a few removed  
sendmail libffi-dev build-essential libssl-dev curl libpcre3-dev libpcre++-dev
zlib1g-dev libcurl4-openssl-dev autoconf automake avahi-daemon locales
dosfstools sqlite3 git sudo \  
&& rm -rf /var/lib/apt/lists/*  
  
# Sane defaults for pip  
ENV PIP_NO_CACHE_DIR off  
ENV PIP_DISABLE_PIP_VERSION_CHECK on  
  
RUN useradd -ms /bin/bash alarmdecoder \  
&& adduser alarmdecoder sudo  
  
RUN pip install gunicorn --upgrade  
  
RUN cd /opt \  
&& git clone https://github.com/nutechsoftware/alarmdecoder-webapp.git  
  
WORKDIR /opt/alarmdecoder-webapp  
  
RUN pip install -r requirements.txt  
  
RUN mkdir instance \  
&& chown -R alarmdecoder:alarmdecoder .  
  
USER alarmdecoder  
RUN python manage.py initdb  
USER root  
  
# sqlite db is stored here  
VOLUME /opt/alarmdecoder-webapp/instance  
  
# I'm not sure what's going on here, but the app starts its own server on port  
# 5000, and that's the server that it wants exposed to the outside world. So
we  
# start gunicorn on port 8000, but that server is ignored and the code spins
up  
# the actual server that we expose.  
#  
# This port 5000 also seems to be hard-coded in a few different places in the
app.  
EXPOSE 5000  
COPY start.sh /  
  
CMD ["/start.sh"]  

