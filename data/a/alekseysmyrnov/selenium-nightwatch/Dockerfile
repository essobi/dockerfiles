FROM alekseysmyrnov/selenium:latest  
MAINTAINER Aleksey @soar Smyrnov (http://soar.name)  
  
# Install Node.js  
RUN apt-get update \  
&& apt-get -yqq install \  
nodejs-legacy \  
npm \  
&& rm -rf /var/lib/apt/lists/*  
  
# Additional NPM packages  
RUN npm install -g nightwatch  
RUN npm install -g phantomjs-prebuilt  
  
# Additional parameters  
#ENV XVFB_PARAMS ""  
#ENV XVFB_SERVER_ARGS "-screen 0 800x600x24"  
#ENV SELENIUM_CLIARGS ""  
#ENV SELENIUM_PARAMS ""  
# Startup  
EXPOSE 4444  
CMD xvfb-run -a ${XVFB_PARAMS} \--server-args="${XVFB_SERVER_ARGS}" \  
java ${SELENIUM_CLIARGS} -jar /opt/selenium/selenium-server-standalone.jar
${SELENIUM_PARAMS}  

