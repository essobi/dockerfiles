FROM node:4-slim  
MAINTAINER Pierre Klink <dev@klink.xyz>  
  
RUN wget https://github.com/Bluefinch/microglark/archive/master.tar.gz \  
&& tar xzf master.tar.gz --strip-components=1 \  
&& npm install \  
&& rm master.tar.gz  
  
EXPOSE 3000  
ENTRYPOINT ["npm"]  
CMD ["start"]  

