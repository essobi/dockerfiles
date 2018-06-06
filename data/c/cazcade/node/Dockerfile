FROM node  
  
RUN apt-get -qq update  
RUN apt-get -y install wget  
  
# install new relic server monitoring  
RUN echo deb http://apt.newrelic.com/debian/ newrelic non-free >>
/etc/apt/sources.list.d/newrelic.list  
RUN wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add -  
RUN apt-get -qq update  
RUN apt-get install newrelic-sysmond  
  
RUN npm install -g npm-install-missing  
RUN npm install -g strongloop  
  
# replace this with your application's default port  
EXPOSE 3000  
# replace this with your main "server" script file  
CMD [ "/run.sh"]  

