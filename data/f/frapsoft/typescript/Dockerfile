FROM frapsoft/node:yarn  
  
MAINTAINER Maik Ellerbrock (https://github.com/ellerbrock)  
  
USER root  
  
RUN yarn global add typescript && \  
yarn cache clean  
  
USER app  
  
ENV HOME=/app  
  
WORKDIR $HOME  
  
ENTRYPOINT ["tsc"]  
  
CMD ["--version"]  

