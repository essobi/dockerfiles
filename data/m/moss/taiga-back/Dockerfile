FROM python:3.4  
MAINTAINER Thiago Almeida <thiagoalmeidasa@gmail.com>  
  
  
ENV TAIGA_BACK_VERSION 3.0.0  
ENV TAIGA_CONTRIB_SLACK 3.0  
ENV LANG en_US.UTF-8  
ENV LC_TYPE en_US.UTF-8  
# Install dependencies  
RUN \  
apt-get update -qq && \  
apt-get install -y gettext netcat locales && \  
apt-get autoremove -y && rm -rf /var/lib/apt/lists/* && \  
sed -i 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \  
locale-gen && pip install circus  
  
# Install taiga-back  
RUN \  
mkdir -p /usr/local/taiga && \  
useradd -d /usr/local/taiga taiga && \  
git clone https://github.com/taigaio/taiga-back.git /usr/local/taiga/taiga-
back && \  
mkdir /usr/local/taiga/media && chown -R taiga /usr/local/taiga/media && \  
mkdir /usr/local/taiga/static && chown -R taiga /usr/local/taiga/static && \  
mkdir /usr/local/taiga/logs && chown -R taiga /usr/local/taiga/logs && \  
cd /usr/local/taiga/taiga-back && \  
git checkout ${TAIGA_BACK_VERSION} && \  
pip install -r requirements.txt && \  
pip install taiga-contrib-slack==${TAIGA_CONTRIB_SLACK} taiga-contrib-ldap-
auth && \  
touch /usr/local/taiga/taiga-back/settings/dockerenv.py && \  
touch /usr/local/taiga/circus.ini  
  
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

