FROM alpine:edge  
  
LABEL maintainer="contact@ahmedaminemejri.com"  
  
RUN apk add --update postfix \  
postfix-mysql \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 25 465 587  
CMD ["postfix","start-fg"]  
  

