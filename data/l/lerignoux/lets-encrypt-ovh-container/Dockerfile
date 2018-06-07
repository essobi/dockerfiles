FROM alpine  
  
RUN apk update && apk add openssh git python-dev py-pip bash openssl curl  
  
RUN git clone https://github.com/lukas2511/dehydrated  
RUN mkdir ./dehydrated/hooks  
RUN git clone https://github.com/rbeuque74/letsencrypt-ovh-hook
./dehydrated/hooks/ovh  
RUN pip install -r /dehydrated/hooks/ovh/requirements.txt  
  
WORKDIR /dehydrated  
ADD docker-entrypoint.sh /dehydrated/  
  
ENTRYPOINT ["bash", "./docker-entrypoint.sh"]  

