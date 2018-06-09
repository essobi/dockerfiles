FROM python:3.4  
MAINTAINER Damien Gustave <delovan@gmail.com>  
  
# Install dependencies  
RUN \  
apt-get update -qq && \  
apt-get install -y netcat gettext && \  
rm -rf /var/lib/apt/lists/* && \  
pip install gunicorn  
  
RUN \  
cd /root && \  
git clone https://github.com/circus-tent/circus.git && \  
cd circus && \  
pip install pyzmq && \  
python setup.py install && \  
cd / && \  
rm -rf /root/circus  
  
# Install taiga-back  
RUN \  
mkdir -p /usr/local/taiga && \  
useradd -d /usr/local/taiga taiga && \  
git clone https://github.com/taigaio/taiga-back.git /usr/local/taiga/taiga-
back && \  
mkdir /usr/local/taiga/media /usr/local/taiga/static /usr/local/taiga/logs &&
\  
cd /usr/local/taiga/taiga-back && \  
git checkout 3.1.0 && \  
pip install -r requirements.txt && \  
pip install -Iv taiga-contrib-slack==3.1 && \  
touch /usr/local/taiga/taiga-back/settings/dockerenv.py && \  
touch /usr/local/taiga/circus.ini && \  
chown -R taiga:taiga /usr/local/taiga  
  
# Add Taiga Configuration  
ADD ./local.py /usr/local/taiga/taiga-back/settings/local.py  
  
# Configure and Start scripts  
ADD ./configure /usr/local/taiga/configure  
ADD ./start /usr/local/taiga/start  
RUN chmod +x /usr/local/taiga/configure /usr/local/taiga/start  
  
VOLUME /usr/local/taiga/media  
VOLUME /usr/local/taiga/static  
VOLUME /usr/local/taiga/logs  
  
EXPOSE 8000  
CMD ["/usr/local/taiga/start"]  

