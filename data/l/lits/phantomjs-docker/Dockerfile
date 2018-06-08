FROM neo9polska/nodejs-bower-gulp  
  
# Env  
ENV PHANTOMJS_VERSION 1.9.8  
# Install or update to the latest system software  
RUN apt-get update -qq  
RUN apt-get install -qq build-essential chrpath libssl-dev libxft-dev  
  
# Install these packages needed by PhantomJS to work correctly.  
RUN apt-get install -qq libfreetype6 libfreetype6-dev  
RUN apt-get install -qq libfontconfig1 libfontconfig1-dev  
  
# Install wget  
RUN apt-get install -qq wget  
  
# Get it from the PhantomJS website.  
RUN wget -P /usr/local/share/
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2  
RUN tar xjf /usr/local/share/phantomjs-1.9.8-linux-x86_64.tar.bz2 -C
/usr/local/share  
  
# create a symlink  
RUN ln -sf /usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs
/usr/local/bin/phantomjs  
RUN ln -sf /usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs
/usr/local/share/phantomjs  
RUN ln -sf /usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs
/usr/bin/phantomjs  
  
# Clean installiation hash  
RUN apt-get autoremove -y  
RUN apt-get clean all  
  
# Make phantomjs as Node module.  
RUN npm install phantom  

