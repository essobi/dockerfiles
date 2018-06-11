FROM ubuntu:16.04  
  
COPY ["start.sh", "/start.sh"]  
  
RUN apt update \  
&& apt upgrade -y \  
&& apt install build-essential git python-dev libxml2-dev \  
libxslt-dev zlib1g-dev python-virtualenv nginx curl \  
apt-transport-https python-pip -y \  
&& curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- \  
&& echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list \  
&& apt update \  
&& apt install yarn -y \  
&& cd /opt \  
&& git clone https://github.com/yeti-platform/yeti.git \  
&& cd /opt/yeti \  
&& pip install -r requirements.txt \  
&& pip install uwsgi \  
&& yarn install \  
&& adduser yeti \  
&& cp extras/systemd/*.service /etc/systemd/system/ \  
&& chown -R yeti:yeti /opt/yeti \  
&& chmod +x /opt/yeti/yeti.py \  
&& service nginx restart \  
&& pip install --upgrade pip \  
&& chmod +x /start.sh \  
&& cp /opt/yeti/yeti.conf.sample /home/yeti/yeti.conf \  
&& ln -s /home/yeti/yeti.conf /opt/yeti/yeti.conf \  
&& apt remove curl git -y  
  
COPY ["nginx.conf", "/etc/nginx/sites-available/yeti"]  
  
RUN rm /etc/nginx/sites-enabled/default && \  
ln -s /etc/nginx/sites-available/yeti /etc/nginx/sites-enabled/yeti  
  
VOLUME ["/home/yeti"]  
CMD ["/start.sh"]  
  
EXPOSE 5000  

