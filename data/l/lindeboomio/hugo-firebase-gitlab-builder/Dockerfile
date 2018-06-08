FROM lindeboomio/hugo-alpine:0.40.1  
  
RUN apk add \--no-cache nodejs bash && \  
npm install -g \  
firebase-tools \  
broken-link-checker \  
remark-lint remark-cli remark-preset-lint-recommended \  
htmlhint && \  
addgroup -g 1000 gitlab && \  
adduser -D -u 1000 -G gitlab gitlab  
  
USER gitlab  
  
ENTRYPOINT [ ]  

