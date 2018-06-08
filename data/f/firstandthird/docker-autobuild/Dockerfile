FROM node:6-alpine  
  
RUN apk add --update docker git bash curl  
ADD https://github.com/Yelp/dumb-init/releases/download/v1.1.1/dumb-
init_1.1.1_amd64 /usr/local/bin/dumb-init  
RUN chmod +x /usr/local/bin/dumb-init  
  
RUN mkdir /app && \  
cd /app && \  
npm i --silent --progress=false hubhooks@0.2.1  
  
WORKDIR /app/node_modules/hubhooks  
  
ENV PORT=8080  
ENV SECRET=""  
ENV GITHUB_TOKEN=""  
ENV VERBOSE=0  
VOLUME /repos  
  
EXPOSE 8080  
COPY scripts /scripts  
ENV SCRIPTS="/scripts"  
CMD ["dumb-init", "node", "bin.js"]  

