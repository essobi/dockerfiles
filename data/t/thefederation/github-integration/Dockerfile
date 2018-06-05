FROM golang:1.9  
ENV DEBIAN_FRONTEND noninteractive  
ENV GI_DIR $GOPATH/src/github.com/thefederationinfo/github-integration  
  
RUN useradd -ms /bin/bash user  
  
RUN mkdir -p $GI_DIR  
COPY . $GI_DIR  
WORKDIR $GI_DIR  
  
RUN go get ./... && go build  
RUN mv github-integration /usr/local/bin/github-integration  
RUN mv templates /home/user && \  
chown -R user:user /home/user/templates  
RUN rm -rv $GOPATH/src/*  
  
USER user  
WORKDIR /home/user  
  
EXPOSE 8181  
CMD ["sh", "-c", "/usr/local/bin/github-integration --github-id ${GITHUB_ID}
\--github-secret ${GITHUB_SECRET} \--server-domain ${DOMAIN} \--travis-token
${TRAVIS_SECRET}"]  

