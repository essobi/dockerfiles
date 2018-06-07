FROM microsoft/dotnet:1.0.0-preview2-sdk  
  
RUN apt-get -y clean \  
&& apt-get -y purge \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs \  
&& rm -rf /var/lib/apt/lists/*  
# Fix https://github.com/npm/npm/issues/9863  
RUN cd $(npm root -g)/npm \  
&& npm install fs-extra \  
&& sed -i -e s/graceful-fs/fs-extra/ -e s/fs\\.rename/fs.move/
./lib/utils/rename.js \  
&& npm cache clean  

