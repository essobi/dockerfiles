FROM alpine:3.6  
RUN apk add --no-cache python py-pip jq  
RUN pip install awscli  
RUN mkdir -p /aws  
COPY invalidate.sh /aws/invalidate.sh  
WORKDIR /aws  
ENTRYPOINT "/aws/invalidate.sh"  

