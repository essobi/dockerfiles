FROM python:3-alpine  
MAINTAINER Dang Mai <contact@dangmai.net>  
  
ENV LIMNORIA_VERSION master-2017-04-16  
RUN apk --no-cache add git bash openssl ca-certificates vim less \  
&& pip install -r
https://raw.githubusercontent.com/ProgVal/Limnoria/${LIMNORIA_VERSION}/requirements.txt
\  
&& pip install git+https://github.com/ProgVal/Limnoria.git@${LIMNORIA_VERSION}
\--upgrade \  
&& apk del git  
  
VOLUME ["/var/supybot/data"]  
WORKDIR /var/supybot/data  
  
ADD ["start.sh", "/"]  
RUN chmod u+x /start.sh  
ENTRYPOINT ["/start.sh"]  

