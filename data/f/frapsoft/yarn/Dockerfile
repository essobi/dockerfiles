FROM frapsoft/node:yarn  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
USER root  
  
RUN yarn self-update && \  
chown -R app:app /app  
  
USER app  
  
ENTRYPOINT ["yarn"]  
  
CMD ["--version"]  

