FROM alpine  
MAINTAINER Paul Pham <docker@aquaron.com>  
  
COPY data/runme.sh /usr/bin/runme.sh  
COPY data/cli.ini /etc/cli.ini  
  
RUN apk add --no-cache bash git python3 python3-dev musl-dev libffi-dev
openssl-dev gcc \  
&& git clone https://github.com/certbot/certbot \  
&& cd /certbot \  
&& python3 setup.py install \  
&& cd certbot-dns-google; python3 setup.py install; cd .. \  
&& cd certbot-dns-digitalocean; python3 setup.py install; cd .. \  
&& cd .. \  
&& apk del --purge git python3-dev musl-dev libffi-dev gcc \  
&& rm -rf /core /var/cache/apk/* /certbot  
  
ENTRYPOINT [ "runme.sh" ]  
CMD [ "help" ]  

