FROM node:5  
EXPOSE 2525  
ENTRYPOINT ["mb"]  
CMD ["start"]  
ENV MOUNTEBANK_VERSION=1.5.0  
RUN npm install -g mountebank@${MOUNTEBANK_VERSION} \--production  
  

