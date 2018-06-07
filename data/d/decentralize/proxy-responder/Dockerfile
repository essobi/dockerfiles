FROM golang  
  
ENV GOPATH /go  
ENV GLIDE_VERSION 0.12.3  
ENV APP_DIR /go/src/github.com/djmaze/proxy-responder  
RUN curl -sL
https://github.com/Masterminds/glide/releases/download/v${GLIDE_VERSION}/glide-v${GLIDE_VERSION}-linux-
amd64.tar.gz \  
| tar xzf - --strip-components=1 -C /usr/local/bin linux-amd64/glide  
WORKDIR ${APP_DIR}  
COPY glide.yaml glide.lock ${APP_DIR}/  
RUN glide install  
COPY . ${APP_DIR}/  
RUN CGO_ENABLED=0 GOOS=linux go build  
  
FROM scratch  
COPY \--from=0 /go/src/github.com/djmaze/proxy-responder /  
ENTRYPOINT ["/proxy-responder"]  

