FROM cryptomental/steem-piston:latest  
MAINTAINER Cryptomental "cryptomental.com@gmail.com"  
# Install build dependencies  
USER root  
RUN apt-get update -y && apt-get -y install git make gcc libssl-dev libgmp-dev
python-dev libxml2-dev libxslt1-dev zlib1g-dev nodejs-legacy npm  
# Install common tools  
RUN apt-get install -y vim mc  
RUN npm install -g bower  
USER $PISTON_USER  
  
# Install latest steem-piston-web package from sources  
# Alpha release uses develop branch of piston and python-steemlib  
RUN git clone https://github.com/xeroc/piston \  
&& cd piston \  
&& git checkout develop \  
&& cd piston/static/libs/sliptree-bootstrap-tokenfield \  
&& bower install bootstrap-tokenfield \  
&& mv bower_components/bootstrap-tokenfield/dist dist \  
&& cd $PISTON_HOME/piston \  
&& make install-user \  
&& cd $PISTON_HOME  
RUN pip3 install --user -r piston/requirements-web.txt  
  
RUN git clone https://github.com/xeroc/python-steem \  
&& cd python-steem \  
&& git checkout develop \  
&& make install-user \  
&& cd $PISTON_HOME  
RUN pip3 install --user eventlet  
  
ENV PYTHONIOENCODING UTF-8  

