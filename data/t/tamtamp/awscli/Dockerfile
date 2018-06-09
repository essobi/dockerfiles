FROM alpine  
MAINTAINER tamtamp  
  
  
RUN apk update && apk upgrade && \  
apk add git wget bash less groff py-pip jq && \  
pip install --upgrade pip  
RUN pip install awscli==1.15.1  
  
ENTRYPOINT []  
CMD ["tail","-f","/dev/null"]  

