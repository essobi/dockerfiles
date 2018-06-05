FROM highfive/base:alpine  
  
RUN apk add \--no-cache python2 py2-pip groff less \  
&& pip install awscli \  
&& apk del --no-cache --purge py2-pip  
  
COPY config /root/.aws/  
  
WORKDIR /aws  
ENTRYPOINT ["/usr/bin/aws"]  

