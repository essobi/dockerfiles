FROM alpine:3.5  
MAINTAINER Vince Tse <thelazyenginerd@gmail.com>  
  
RUN apk update  
RUN apk upgrade  
RUN apk add py-boto py-requests  
  
ADD bin/route53-presence /bin/route53-presence  
  
ENTRYPOINT ["/bin/route53-presence"]  
CMD ["-h"]  

