FROM node:0.10.35  
ENV APP_HOME /usr/src/sunset  
  
ADD . $APP_HOME  
WORKDIR $APP_HOME  
  
ADD ./entrypoint.sh /  
RUN chmod 0755 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 50555:50555  
CMD ["npm", "start"]

