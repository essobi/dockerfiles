#  
FROM muccg/python-base:debian8-2.7  
MAINTAINER ccg <devops@ccg.murdoch.edu.au>  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
npm nodejs nodejs-legacy iceweasel xvfb git && \  
apt-get autoremove -y --purge && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN npm install -g inherits \  
&& npm install -g \  
bower \  
jasmine-node \  
jasmine-reporters@1.0.0 \  
karma \  
karma-firefox-launcher \  
karma-jasmine \  
karma-junit-reporter \  
karma-ng-scenario && \  
rm -rf /root/.npm/  
  
ENV NODE_PATH /usr/lib/nodejs/:/usr/local/lib/node_modules/  
  
VOLUME ["/data"]  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD /docker-entrypoint.sh  

