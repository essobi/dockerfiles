FROM node:alpine  
LABEL maintainer Nicolas Zagulajew (freeeflyer) <docker.com@xoop.org>  
  
ADD . /app  
WORKDIR /app  
  
ENV WETTY_USER="term" \  
WETTY_HASH='$6$GaPRprhf$gSoLLlfIL6E4DziJkiAnkX4QEUi5Z./IdTtXral4Yolo39APievK7COwbJrLJPuNyCywrxdFZ.r/x5WzPo.Cw1'
\  
WETTY_PORT=3000  
RUN apk add --update vim bash openssh-client python make g++ procps \  
&& npm install \  
&& apk del python make g++  
  
EXPOSE ${WETTY_PORT}  
  
CMD ["bin/entrypoint.sh"]  

