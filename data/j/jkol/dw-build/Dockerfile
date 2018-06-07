FROM node:8.3.0  
ENV ARCH x86_64  
ENV PHANTOM_VERSION phantomjs-1.9.8  
ENV PHANTOM_JS $PHANTOM_VERSION-linux-$ARCH  
  
RUN apt-get update \  
&& apt-get upgrade -y --force-yes \  
&& apt-get install -y --force-yes rsync zip \  
&& apt-get install -y --force-yes build-essential chrpath libssl-dev libxft-
dev \  
&& apt-get install -y --force-yes libfreetype6 libfreetype6-dev \  
&& apt-get install -y --force-yes libfontconfig1 libfontconfig1-dev \  
&& rm -rf /var/lib/apt/lists/*;  
  
RUN npm install -g gulp  
  
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 \  
&& tar -xvjf $PHANTOM_JS.tar.bz2 \  
&& mv $PHANTOM_JS /usr/local/share \  
&& ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin \  
&& rm $PHANTOM_JS.tar.bz2  
  
CMD [ "node" ]  

