FROM mobilelive/alpine:basic  
MAINTAINER mobilelive/dockerfiles  
  
# install #  
RUN apk add --update \  
python \  
py-setuptools \  
py-pip \  
;  
RUN pip install elasticsearch-curator==4.2.6  
RUN apk del py-pip  
RUN rm -rf /var/cache/apk/*  
  
# cmd #  
CMD [ "curator_cli" ]  
  

