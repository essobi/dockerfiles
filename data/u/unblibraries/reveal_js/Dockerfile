FROM mhart/alpine-node  
MAINTAINER Jacob Sanford <jsanford@unb.ca>  
MAINTAINER Brian Cassidy <brian.cassidy@unb.ca>  
  
ENV REVEAL_PORT 8000  
ENV REVEAL_BASE .  
ENV REVEAL_PATH /reveal.js  
  
RUN apk add --update git python make g++ && \  
rm -rf /var/cache/apk/* && \  
git clone https://github.com/hakimel/reveal.js.git ${REVEAL_PATH} && \  
npm install -g grunt-cli && \  
cd ${REVEAL_PATH}; npm install && \  
rm -rf ~/.npm && \  
npm cache clear  
  
COPY scripts/run.sh /run.sh  
EXPOSE ${REVEAL_PORT}  
  
CMD /run.sh  

