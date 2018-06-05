FROM ubuntu:xenial  
  
  
  
RUN apt-get update -q && \  
apt-get upgrade -qy && \  
apt-get install -qy build-essential && \  
apt-get install -qy libxslt1-dev libffi-dev libffi6 libpython-dev libssl-dev
python2.7 python-cherrypy python-lxml python-pip python2.7-dev && \  
apt-get install -qy git-core wget && \  
apt-get clean  
  
# apt-get install -qy git wget && \  
# apt-get install -qy libxslt1-dev libxslt1.1 libxml2-dev libxml2 libssl-dev
libffi-dev && \  
# apt-get install -qy python-pip python-dev libssl-dev && \  
RUN cd /tmp && \  
wget http://rarlab.com/rar/unrarsrc-5.2.7.tar.gz && \  
tar -xvf unrarsrc-5.2.7.tar.gz && \  
cd unrar && \  
make -f makefile && \  
install -v -m755 unrar /usr/bin  
  
RUN pip install pyopenssl  
  
RUN git clone https://github.com/SickRage/SickRage.git /opt/sickrage  
  
ADD launch.sh /launch.sh  
RUN chmod +x "/launch.sh"  
  
VOLUME ["/data/downloads"]  
VOLUME ["/data/torrentfiles"]  
VOLUME ["/data/tv"]  
VOLUME ["/data/sickrage"]  
  
#RUN touch /etc/default/sickrage && \  
# echo "SR_USER=root" >> /etc/default/sickrage && \  
# echo "SR_HOME=/opt/sickrage" >> /etc/default/sickrage && \  
# echo "SR_DATA=/opt/sickrage" >> /etc/default/sickrage && \  
# echo "SR_PIDFILE=/data/sickrage/.sickrage.pid" >> /etc/default/sickrage  
# RUN cp /opt/sickrage/runscripts/init.ubuntu /etc/init.d/sickrage && \  
# chmod +x /etc/init.d/sickrage && \  
# update-rc.d sickrage defaults  
# Change ownership to your username  
# sudo chown username:username -R /opt/sickrage  
# Test to see if you can run SickRage  
# python /opt/sickrage/SickBeard.py -d  
EXPOSE 8081  
CMD ["/launch.sh"]  
  
# CMD ["exec /opt/sickrage/SickBeard.py"]  

