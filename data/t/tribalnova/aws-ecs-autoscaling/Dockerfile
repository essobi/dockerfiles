FROM alpine  
LABEL author="Nicolas Degardin<nicolas.degardin@hmhco.com>"  
  
RUN apk add --update --no-cache jq py-pip bash curl groff  
RUN pip install awscli  
COPY asg.sh /usr/bin/asg  
  
ENTRYPOINT ["asg"]  

