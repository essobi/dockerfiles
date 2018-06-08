FROM alpine  
  
MAINTAINER Joshua Marquez "joshua.marquezn@gmail.com"  
# api-console version to use  
ENV API_CONSOLE_VERSION 3.0.19  
# Install some tools  
RUN apk add --update nodejs nodejs-npm wget unzip && rm -rf /var/cache/apk/*  
  
# Define working directory  
WORKDIR /api-console  
  
# Download api-console  
RUN wget https://github.com/mulesoft/api-
console/archive/v$API_CONSOLE_VERSION.zip -O console.zip  
  
# Install api-console  
RUN unzip console.zip -d . \  
&& rm -rf console.zip \  
&& cd api-console-$API_CONSOLE_VERSION \  
&& mv -f dist .. \  
&& mv Gruntfile.js .. \  
&& mv package.json .. \  
&& cd .. && rm -rf api-console-$API_CONSOLE_VERSION \  
&& mkdir dist/raml \  
&& cp dist/examples/simple.raml dist/raml/api.raml \  
&& rm -rf dist/examples  
  
# Install dependencies  
RUN npm install -g grunt-cli && npm install && npm cache clean  
  
RUN sed -i 's/<raml-initializer><\/raml-initializer>/<raml-console-loader
src="raml\/api.raml"><\/raml-console-loader>/g' /api-console/dist/index.html  
  
EXPOSE 9000  
EXPOSE 35729  
CMD ["grunt","connect:livereload","watch"]  

