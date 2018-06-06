FROM node  
  
ENV HOME /home/root  
RUN mkdir -p /home/root/.browserstack/  
WORKDIR /home/root  
  
RUN yes | apt-get update  
  
#Install Java and Download BrowserStack  
RUN yes | apt-get install default-jre  
RUN curl -o $HOME/.browserstack/BrowserStackTunnel.jar
http://www.browserstack.com/BrowserStackTunnel.jar  
  
ADD . /install  
  
#Install phantomjs  
RUN chmod +x /install/install-phantomjs  
RUN chmod +x /install/init-browserstack  
RUN /install/install-phantomjs  
  
RUN mkdir -p /var/cache/drone/src/github.com/  
  
CMD /install/init-browserstack && npm -d i && npm test

