FROM python:2.7-alpine  
  
ENV ELASTALERT_VERSION 0.1.21  
RUN apk update && apk upgrade && apk add --no-cache curl openssl  
  
RUN apk --no-cache add g++ libffi-dev openssl-dev \  
&& pip install elastalert==$ELASTALERT_VERSION \  
&& apk del g++ libffi-dev openssl-dev \  
&& rm -rf /var/cache/apk/*  
  
RUN mkdir -p /conf && mkdir -p /rules  
  
COPY docker-entrypoint.sh /  
COPY run.sh /  
  
WORKDIR /opt/elastalert/  
ENTRYPOINT [ "/docker-entrypoint.sh" ]  
CMD [ "/run.sh" ]  

