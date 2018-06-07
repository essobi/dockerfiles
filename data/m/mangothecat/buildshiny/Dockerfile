FROM mangothecat/buildr:3.4.1  
ENV PHANTOM_JS 2.1.1  
RUN apt-get update -qq && apt-get -y --no-install-recommends install \  
libicu-dev \  
libfontconfig1-dev \  
libjpeg-dev \  
libfreetype6 \  
libfreetype6-dev \  
libssl-dev \  
libpng-dev \  
bzip2  
  
RUN cd ~ \  
&& wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-${PHANTOM_JS}-linux-x86_64.tar.bz2
\  
&& tar xvjf phantomjs-${PHANTOM_JS}-linux-x86_64.tar.bz2 \  
&& mv phantomjs-${PHANTOM_JS}-linux-x86_64 /usr/local/share \  
&& ln -sf /usr/local/share/phantomjs-${PHANTOM_JS}-linux-x86_64/bin/phantomjs
/usr/local/bin  

