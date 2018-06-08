FROM frapsoft/node  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
USER root  
  
RUN npm update && \  
npm i -g pm2 && \  
find /app -type d -name ".?*" -maxdepth 1 -exec rm -rf {} \; && \  
rm -rf /tmp/*  
  
ENTRYPOINT ["pm2"]  
CMD ["--help"]  

