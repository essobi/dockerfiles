FROM python:2.7-alpine  
  
RUN apk update \  
apk add bash  
  
RUN mkdir /app  
WORKDIR /app  
  
ENV KEGBOT_VERSION=master  
RUN apk add curl \  
&& curl -k -L https://github.com/Kegbot/kegbot-
server/archive/${KEGBOT_VERSION}.tar.gz -o /tmp/kegbot.tar.gz \  
&& tar -xf /tmp/kegbot.tar.gz -C /tmp/ \  
&& ls -la /tmp/ \  
&& cp -r /tmp/kegbot-server-${KEGBOT_VERSION}/* /app/ \  
&& apk add gcc musl-dev \  
&& apk add zlib-dev libjpeg-turbo libjpeg-turbo-dev libjpeg openjpeg \  
&& apk add mysql-client \  
&& apk add mariadb-dev \  
&& ls -la ./ \  
&& python ./setup.py install \  
&& apk del musl-dev gcc \  
&& rm -rf /tmp/kegbot*  
  
RUN mkdir -p /etc/kegbot  
COPY local_settings.py /etc/kegbot/  
  
ADD run.sh /run.sh  
RUN chmod 700 /run.sh  
  
EXPOSE 8000  
ENTRYPOINT ["/bin/sh"]  
CMD ["/run.sh"]  

