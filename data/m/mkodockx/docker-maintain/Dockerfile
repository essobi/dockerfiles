FROM mhart/alpine-node-base:0.10  
MAINTAINER Markus Kosmal https://m-ko-x.de <code@m-ko-x.de>  
  
ENV MAINTAIN_PORT 80  
ENV MAINTAIN_CODE 503  
ENV MAINTAIN_MESSAGE "The requested service is not available at the moment.
Please try again later or contact an administrator"  
RUN mkdir /app  
  
ADD content/index.js /app/index.js  
WORKDIR /app  
  
EXPOSE $MAINTAIN_PORT  
  
CMD ["node", "index.js"]

