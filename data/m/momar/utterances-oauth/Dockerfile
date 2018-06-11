FROM alpine  
LABEL maintainer="contact-docker@mo-mar.de"  
  
RUN apk add --no-cache nodejs git &&\  
git clone https://github.com/utterance/utterances-oauth.git /data && cd /data
&&\  
npm install  
  
ENV PORT=80  
ENV SCOPES=public_repo  
ENV USER_AGENT=Utterance  
  
CMD ["/usr/bin/node", "/data"]  

