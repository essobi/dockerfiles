  
FROM alpine as builder  
  
RUN apk upgrade --update  
RUN apk add bash tzdata wget  
  
WORKDIR /brook  
  
ENV VERSION=v20180227  
ENV BROOK_DOWNLOAD_URL
https://github.com/txthinking/brook/releases/download/$VERSION/brook  
  
RUN wget --no-check-certificate ${BROOK_DOWNLOAD_URL} -O brook && chmod +x
brook  
  
FROM alpine  
COPY \--from=builder /brook/brook /usr/local/bin/brook  
  
EXPOSE 80  
CMD brook server -l :80 -p ${PASSWD:=brook}  

