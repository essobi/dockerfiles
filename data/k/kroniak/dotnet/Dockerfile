FROM microsoft/dotnet:1.1.0-sdk-projectjson  
  
# Install node-js and npm  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install nodejs \  
&& rm -rf /var/lib/apt/lists/*  
# Install global dependicies for node  
RUN npm i --loglevel=error -g --quiet bower gulp-cli

