FROM debian:jessie  
  
COPY requirements.txt /app/requirements.txt  
  
RUN apt-get update && apt-get -y --no-install-recommends install \  
git \  
g++ \  
python \  
python-dev \  
python-pip \  
python-dbus \  
&& pip install -r /app/requirements.txt \  
&& apt-get remove --purge --auto-remove -y \  
gcc \  
git \  
g++ \  
perl-modules \  
python-dev \  
&& rm -rf /tmp/* /var/tmp/  
  
COPY src/ /app  
WORKDIR /app  
  
ENTRYPOINT ["/usr/bin/python", "-m", "spacel.main"]  
  

