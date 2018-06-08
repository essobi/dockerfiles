FROM alpine:3.5  
LABEL description='Devpi server.'  
LABEL maintainer='s.apostolico@gmail.com'  
  
RUN apk add --update --no-cache bash ca-certificates python3 \  
&& python3 -m ensurepip \  
&& rm -r /usr/lib/python*/ensurepip \  
&& pip3 install --upgrade pip setuptools \  
&& update-ca-certificates \  
&& rm -r /root/.cache  
ADD src/requirements.pip /  
  
RUN apk add --no-cache --virtual .build-deps \  
gcc python3-dev libffi-dev musl-dev bash \  
&& pip install -r /requirements.pip \  
&& apk del .build-deps \  
&& rm -r /root/.cache  
  
VOLUME /export  
VOLUME /mnt  
  
EXPOSE 3141  
ADD VERSION /  
ADD src/entrypoint.sh /  
ADD src/export.sh /export.sh  
ADD src/import.sh /import.sh  
  
CMD ["/entrypoint.sh"]  

