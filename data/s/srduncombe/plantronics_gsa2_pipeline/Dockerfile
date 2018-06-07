FROM valtechcanada/python-postgres:latest  
  
RUN apt-get update  
  
# Install PhantomJS  
RUN apt-get install -y build-essential chrpath libssl-dev libxft-dev
libfreetype6 \  
libfreetype6-dev libfontconfig1 libfontconfig1-dev \  
&& export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64" \  
&& wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 \  
-qO /usr/local/lib/phantomjs.tar.bz2 \  
&& tar xvjf /usr/local/lib/phantomjs.tar.bz2 -C /usr/local/lib/ \  
&& ln -sf /usr/local/lib/$PHANTOM_JS/bin/phantomjs /usr/local/share/phantomjs
\  
&& ln -sf /usr/local/lib/$PHANTOM_JS/bin/phantomjs /usr/local/bin/phantomjs \  
&& ln -sf /usr/local/lib/$PHANTOM_JS/bin/phantomjs /usr/bin/phantomjs  
# Install Heroku CLI  
RUN wget https://cli-assets.heroku.com/branches/stable/heroku-linux-
amd64.tar.gz -qO heroku.tar.gz \  
&& mkdir -p /usr/local/lib \  
&& tar -xvzf heroku.tar.gz -C /usr/local/lib \  
&& /usr/local/lib/heroku/install  
  

