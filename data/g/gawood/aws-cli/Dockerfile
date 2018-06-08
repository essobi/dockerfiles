FROM alpine:3.4  
MAINTAINER gawood  
  
RUN apk --update add \  
python \  
py-pip \  
jq \  
groff \  
&& pip install awscli \  
&& apk del py-pip \  
&& rm -rf /var/cache/apk/*  
  
ENV PAGER=less  
  
ENTRYPOINT [ "aws" ]  
CMD [ "help" ]  

