FROM node:8  
LABEL maintainer "karolis@pretendentas.lt"  
  
ENV BUILD_TASK ""  
ENV GULP_TASK ""  
ENV NPM_TASK ""  
COPY command.sh /root/command.sh  
  
RUN npm install bower gulp-cli -g \  
&& chmod +x /root/command.sh  
  
ENTRYPOINT ["/root/command.sh"]

