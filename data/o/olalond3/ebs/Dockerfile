FROM anigeo/awscli  
  
RUN apk add --update-cache \  
bash \  
curl \  
&& rm /var/cache/apk/*  
  
ADD ebs.sh /aws/  
RUN chmod +x /aws/ebs.sh  
  
ENTRYPOINT [ "/aws/ebs.sh" ]  

