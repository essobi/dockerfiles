# Base  
FROM alpine:3.7 AS base  
RUN apk add --no-cache tini  
WORKDIR /root/app  
ENTRYPOINT ["/sbin/tini", "--"]  
  
# Deps  
FROM base AS dependencies  
RUN apk add --no-cache git go libc-dev  
RUN go get github.com/michalschott/go-restful-api-example  
RUN cd /root/go/src/github.com/michalschott/go-restful-api-example && go build  
RUN ls -l /root/go/src/github.com/michalschott/go-restful-api-example/go-
restful-api-example  
  
# Final image  
FROM base AS release  
COPY \--from=dependencies /root/go/src/github.com/michalschott/go-restful-api-
example/go-restful-api-example .  
EXPOSE 3000  
CMD /root/app/go-restful-api-example  

