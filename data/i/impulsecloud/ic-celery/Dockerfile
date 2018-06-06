FROM impulsecloud/ic-ubuntu:16.04  
  
MAINTAINER Johann du Toit <johann@winkreports.com>  
  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \  
apt-get install -y \  
supervisor \  
nodejs && \  
pip3 install lxml && \  
pip3 install cryptography && \  
pip3 install Pillow && \  
pip3 install SQLAlchemy && \  
pip3 install psycopg2 && \  
pip3 install pycrypto && \  
npm install --global \  
babel-cli \  
babel-plugin-transform-react-jsx \  
babel-preset-env babel-preset-react \  
babel-plugin-transform-object-rest-spread && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD . /opt/django/  
  
RUN pip3 install --exists-action=s -r /opt/django/requirements.txt  
  
RUN ln -s /opt/django/supervisord.conf /etc/supervisor/conf.d/; \  
ln -s /usr/lib/node_modules/ /node_modules  
  
VOLUME ["/opt/django/app"]  
EXPOSE 80  
CMD ["/opt/django/run.sh"]  

