FROM alpine:3.2  
EXPOSE 2525  
ENTRYPOINT ["mb"]  
CMD ["start"]  
ENV MOUNTEBANK_VERSION=1.3.0  
RUN apk add --update nodejs  
RUN npm install -g mountebank@${MOUNTEBANK_VERSION} \--production  

