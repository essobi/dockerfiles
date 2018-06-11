FROM alpine:3.7  
LABEL maintainer="mattias.rundqvist@icloud.com"  
  
WORKDIR /app  
  
RUN apk update && \  
apk upgrade && \  
apk add wget gcc musl-dev  
  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  
  
RUN apk add apache2 php5-apache2  
RUN mkdir /run/apache2  
  
RUN pip install -U streamlink  
  
RUN wget https://github.com/tombowditch/telly/releases/download/v0.4.5/telly-
linux-amd64 && \  
mv telly-* telly  
  
#RUN sed -i 's/#LoadModule rewrite_module modules\/mod_rewrite.so/LoadModule
rewrite_module modules\/mod_rewrite.so/g' /etc/apache2/httpd.conf  
#RUN sed -i 's/AllowOverride none/AllowOverride All/g' /etc/apache2/httpd.conf  
COPY init.sh init.sh  
COPY stream.php /var/www/localhost/htdocs/stream.php  
#COPY .htaccess /var/www/localhost/htdocs/.htaccess  
COPY iptv iptv  
  
RUN chmod 775 init.sh && \  
chmod 775 telly  
  
RUN apk add nano  
  
ENV HOST_IP=''  
ENV STREAM_PORT='8200'  
ENV TUNERS_START_PORT='8201'  
ENV PROVIDERS='SVTPLAY;NRKTV;TVPLAYER'  
ENV NRK_PROXY=''  
ENV TVPLAYER_EMAIL=''  
ENV TVPLAYER_PASSWORD=''  
ENV TVPLAYER_PROXY=''  
EXPOSE 8200-8203  
ENTRYPOINT [ "/bin/sh", "init.sh" ]

