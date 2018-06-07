FROM alpine:3.5  
MAINTAINER Gervasio Marchand <gmc@gmc.uy>  
ENV build_date 2017-01-20 21:36  
RUN apk add --update \  
python \  
python-dev \  
py2-pip \  
build-base \  
git \  
supervisor \  
redis \  
curl \  
bash \  
&& pip install virtualenv \  
&& rm -rf /var/cache/apk/* \  
&& git clone https://github.com/g3rv4/simple-redirect.git /var/simple-redirect
\  
&& virtualenv /var/simple-redirect/env \  
&& /var/simple-redirect/env/bin/pip install --no-cache-dir -r /var/simple-
redirect/requirements.txt  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
VOLUME ["/var/config"]  
  
WORKDIR /var/simple-redirect  
EXPOSE 8000  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

