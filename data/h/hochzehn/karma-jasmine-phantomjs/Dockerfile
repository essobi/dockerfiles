FROM node:7.2.0  
RUN npm install -g \  
phantomjs-prebuilt \  
jasmine-core \  
karma karma-coverage karma-junit-reporter karma-jasmine karma-phantomjs-
launcher  
  
VOLUME /opt/karma  
WORKDIR /opt/karma  
  
CMD ["start"]  
ENTRYPOINT ["karma"]  

