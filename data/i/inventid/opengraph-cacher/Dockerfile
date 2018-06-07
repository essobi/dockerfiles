FROM node:8.9  
MAINTAINER Rogier Slag  
  
EXPOSE 7070  
  
RUN groupadd -r luser && useradd -r -g luser luser  
RUN mkdir -p /home/luser/.pm2/  
RUN chown -R luser.luser /home/luser  
RUN npm install -g pm2  
  
RUN mkdir /service  
ADD .babelrc /service/  
ADD yarn.lock /service/  
ADD package.json /service/  
RUN cd /service && yarn install --pure-lockfile  
ADD src /service/src/  
RUN cd /service && yarn dist  
  
USER luser  
WORKDIR /service/dist  
CMD ["/usr/local/bin/pm2", "start", "index.js", "--no-daemon", "--
instances=max"]  
  

