  
FROM frapsoft/node  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
USER root  
  
RUN npm update && \  
npm i -g typescript ts-node && \  
npm cache clean  
  
USER app  
  
ENV HOME=/app  
  
WORKDIR $HOME  
  
ENTRYPOINT ["ts-node"]  
  
CMD ["--version"]  

