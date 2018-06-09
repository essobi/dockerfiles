FROM alpine  
MAINTAINER Christoph Dwertmann <christoph.dwertmann@vaultsystems.com.au>  
RUN apk --update add python py-pip  
RUN apk --update add --virtual build-dependencies gcc python-dev musl-dev \  
&& pip install python-keystoneclient python-swiftclient Flask waitress \  
&& apk del build-dependencies  
RUN setup-timezone -z /usr/share/zoneinfo/Australia/Sydney  
ADD swiftmail.py /  
CMD python -u /swiftmail.py  

