FROM alpine:3.6 as build  
RUN apk update && apk add nasm gcc musl-dev make  
WORKDIR /exp  
COPY . .  
RUN make tiny  
  
FROM scratch  
COPY \--from=build /exp/tiny /t  
ENTRYPOINT ["/t"]  

