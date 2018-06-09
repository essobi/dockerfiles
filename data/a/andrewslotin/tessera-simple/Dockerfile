FROM python:2.7  
MAINTAINER Andrew Slotin <andrew.slotin@gmail.com>  
  
ENV TESSERA_REV 2258c712c8726609aaff62470317e36513db7093  
ENV TESSERA_CONFIG /var/lib/tessera/config.py  
  
RUN apt-get -qq update &&\  
apt-get -qq -y install curl git npm gunicorn &&\  
ln -s $(which nodejs) /usr/bin/node  
RUN npm install -g grunt-cli  
  
ADD ./config.py $TESSERA_CONFIG  
  
RUN mkdir -p /opt  
RUN git clone https://github.com/urbanairship/tessera.git /opt/tessera &&\  
cd /opt/tessera && git reset --hard $TESSERA_REV  
  
# Compile assets  
RUN cd /opt/tessera/tessera-frontend/ &&\  
npm install &&\  
grunt  
  
WORKDIR /opt/tessera/tessera-server  
  
# Install Python dependencies  
RUN pip install -r requirements.txt &&\  
pip install -r dev-requirements.txt  
  
# Create database  
RUN inv db.init  
  
# Cleanup  
RUN npm cache clean -f &&\  
npm ls -gp | awk -F/ '/node_modules/ && !/node_modules.*node_modules/ {print
$NF}' | xargs npm -g rm  
RUN apt-get -qq -y purge npm &&\  
apt-get -qq -y autoremove  
  
EXPOSE :80  
CMD inv run  

