FROM alpine:3.4  
MAINTAINER Zoltan Burgermeiszter <zoltan@burgermeiszter.com>  
  
RUN apk add --update --no-cache asterisk asterisk-dev asterisk-sample-config  
  
EXPOSE 5060  
EXPOSE 8088  
ENTRYPOINT ["asterisk"]  
CMD ["-vvvvf"]

