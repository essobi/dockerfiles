# Rendr app base container  
#  
# Run container by executing following command:  
# $ docker run -t -i -v $(pwd):/www -p 3030:3030 -p 8080:8080
alexindigo/trulia-rendr-base <command>  
#  
# alexindigo/rendr-base  
FROM alexindigo/node-dev:0.10.29  
MAINTAINER Alex Indigo <iam@alexindigo.com>  
  
# Preparations  
ENV PHANTOMJS_URL
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.7-linux-x86_64.tar.bz2  
  
# Make DEBIAN_FRONTEND less chatty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install external services  
# - Sass needs rubygems  
# - Phantomjs needs fontconfig  
RUN apt-get update && apt-get install -y rubygems fontconfig  
  
# Install PhantomJS  
RUN curl -s -L ${PHANTOMJS_URL} -o "phantomjs.tar.bz2"  
RUN mkdir -p /usr/local/share/phantomjs && \  
tar -C /usr/local/share/phantomjs --strip-components 1 -xjf phantomjs.tar.bz2
&& \  
rm phantomjs.tar.bz2  
RUN ln -s /usr/local/share/phantomjs/bin/phantomjs /usr/local/bin/phantomjs  
  
# Install ruby deps  
RUN gem install sass  
  
# Install global npm packages  
RUN npm -q install -g grunt-cli node-inspector  
  
# Create workspace  
# And bind it to the site folder at runtime  
VOLUME ["/www"]  
WORKDIR /www  
  
# Open ports  
EXPOSE 3030  
EXPOSE 5858  
EXPOSE 8080  
# Reset DEBIAN_FRONTEND  
ENV DEBIAN_FRONTEND newt  

