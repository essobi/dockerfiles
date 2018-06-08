FROM snowhigh/teumaster-base  
  
RUN apt-get install -y postgresql postgresql-contrib postgresql-server-dev-all
supervisor gcc && \  
apt-get clean  
  
# Install paddles  
RUN cd /root/ && git clone https://github.com/ceph/paddles  
  
ADD config.py.in /root/paddles/config.py  
ADD alembic.ini.in /root/paddles/alembic.ini  
  
RUN /etc/init.d/postgresql start && \  
sudo -u postgres psql --command "CREATE USER paddles WITH SUPERUSER PASSWORD
'password';" && \  
sudo -u postgres createdb -O paddles paddles && \  
cd /root/paddles && \  
virtualenv ./virtualenv && \  
/bin/bash -c "source ./virtualenv/bin/activate; pip install -r
requirements.txt; python setup.py develop; pecan populate config.py; alembic
stamp head"  
  
ADD supervisord_paddles.conf /etc/supervisor/conf.d/supervisord_paddles.conf  
  
# Install pulpito  
RUN cd /root && git clone https://github.com/ceph/pulpito.git  
  
ADD prod.py /root/pulpito/prod.py  
ADD get-pip.py /root/pulpito/get-pip.py  
  
RUN export HOME=/root && \  
cd /root/pulpito && \  
virtualenv ./virtualenv && \  
/bin/bash -c "source ./virtualenv/bin/activate; python get-pip.py; pip install
-r requirements.txt;"  
  
ADD supervisord_pulpito.conf /etc/supervisor/conf.d/supervisord_pulpito.conf  
  
ADD run.sh /run.sh  
  
EXPOSE 8088 8089  
CMD ["/run.sh"]  

