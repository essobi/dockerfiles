FROM kkarczmarczyk/node-yarn:7.2-slim  
  
RUN apt-get update && \  
apt-get install --yes bzip2 python && \  
# PhantomJS requirements.  
apt-get install --yes build-essential chrpath libssl-dev libxft-dev
libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev && \  
apt-get clean  
  
COPY phantomjs_install.sh /phantomjs_install.sh  
  
# This variable is required by the install script.  
ENV PHANTOM_JS_VERSION 2.1.1  
RUN bash /phantomjs_install.sh && rm /phantomjs_install.sh  
  

