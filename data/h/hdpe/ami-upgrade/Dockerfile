FROM alpine  
  
RUN apk update \  
&& apk --no-cache add openssh jq py-pip \  
&& pip install awscli  
  
COPY ami-upgrade.sh /  
  
CMD ["/ami-upgrade.sh"]  

