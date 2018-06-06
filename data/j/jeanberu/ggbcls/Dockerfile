FROM jeanberu/nodejs  
  
RUN apk add --update ruby-dev git python \  
&& rm -rf /var/cache/apk/* \  
&& gem install sass \  
&& npm install -g grunt-cli gulp bower coffee-script less sass \  
&& npm cache clean  

