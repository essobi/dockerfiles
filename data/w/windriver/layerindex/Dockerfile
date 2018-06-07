FROM debian:stretch  
MAINTAINER Michael Halstead <mhalstead@linuxfoundation.org>  
  
EXPOSE 80  
ENV PYTHONUNBUFFERED=1 \  
LANG=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8 \  
LC_CTYPE=en_US.UTF-8  
## Uncomment to set proxy ENVVARS within container  
#ENV http_proxy http://your.proxy.server:port  
#ENV https_proxy https://your.proxy.server:port  
ADD requirements.txt /  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
autoconf \  
g++ \  
gcc \  
make \  
python3-pip \  
python3-dev \  
python3-pil \  
python3-mysqldb \  
python3-setuptools \  
netcat-openbsd \  
libjpeg-dev \  
vim git curl locales \  
&& echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.UTF-8 \  
&& update-locale \  
&& mkdir /opt/workdir \  
&& pip3 install --upgrade pip && pip3 install wheel gunicorn \  
&& pip3 install -r /requirements.txt \  
&& apt-get purge -y g++ make python3-dev autoconf \  
&& apt-get autoremove -y \  
&& rm -rf /var/lib/apt/lists/* \  
&& apt-get clean \  
&& groupadd user \  
&& useradd --create-home --home-dir /home/user -g user user  
  
ADD . /opt/layerindex  
  
ADD settings.py /opt/layerindex/settings.py  
ADD docker/updatelayers.sh /opt/updatelayers.sh  
ADD docker/migrate.sh /opt/migrate.sh  
  
## Uncomment to add a .gitconfig file within container  
#ADD docker/.gitconfig /root/.gitconfig  
## Uncomment to add a proxy script within container, if you choose to  
## do so, you will also have to edit .gitconfig appropriately  
#ADD docker/git-proxy /opt/bin/git-proxy  
# Add entrypoint to start celery worker and gnuicorn  
ADD docker/entrypoint.sh /entrypoint.sh  
  
RUN mkdir -p /opt/layers && chown -R user:user /opt  
  
VOLUME ['/opt/layers']  
  
# Run gunicorn and celery as unprivileged user  
USER user  
ENTRYPOINT ["/entrypoint.sh"]  

