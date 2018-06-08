# Example built from a couple of sources  
FROM node  
MAINTAINER Tim Hartmann <tfhartmann@gmail.com>  
  
RUN apt-get update  
RUN apt-get -y install wget python-dev g++ make libicu-dev redis-server
python-pip  
  
RUN apt-get -y install build-essential chrpath libssl-dev libxft-dev  
RUN apt-get -y install libfreetype6 libfreetype6-dev  
RUN apt-get -y install libfontconfig1 libfontconfig1-dev  
WORKDIR ~  
ENV PHANTOM_JS "phantomjs-2.1.1-linux-x86_64"  
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2  
RUN tar xvjf $PHANTOM_JS.tar.bz2  
RUN mv $PHANTOM_JS /usr/local/share  
RUN ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin  
  
RUN npm install --global coffee-script hubot@v2.7.5  
RUN hubot --create /opt/hubot  
WORKDIR /opt/hubot  
RUN npm install  
ADD add-hubot-scripts.sh /tmp/  
ADD add-external-scripts.py /tmp/  
RUN npm install hubot-skype-web --save  
  
CMD redis-server /etc/redis/redis.conf && /tmp/add-hubot-scripts.sh &&
/tmp/add-external-scripts.py && bin/hubot --adapter skype-web  

