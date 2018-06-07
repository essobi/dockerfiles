FROM alpine:3.5  
  
MAINTAINER TiTom73 <titom73@users.noreply.github.com>  
  
##########################################################  
  
RUN apk update && apk upgrade  
RUN apk add build-base gcc g++ make python-dev py-pip py-lxml \  
libxslt-dev libxml2-dev libffi-dev openssl-dev curl \  
ca-certificates openssl wget git openssh-client bash  
RUN pip install --upgrade pip\  
&& pip install --upgrade junos-eznc\  
&& pip install --upgrade ansible==2.4.2\  
&& ansible-galaxy install Juniper.junos  
  
CMD ["/bin/ash"]  
  
WORKDIR /builds  

