FROM alpine:latest  
  
RUN apk update  
  
# Setup aws cli  
RUN mkdir -p /aws  
RUN apk -Uuv add groff less python py-pip  
RUN pip install awscli  
RUN apk --purge -v del py-pip  
  
# add extra goodies  
RUN apk add jq  
RUN apk add bash  
  
RUN rm /var/cache/apk/*  
CMD ["aws"]  

