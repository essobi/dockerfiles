FROM alpine:3.4  
RUN apk add --no-cache py-pip python \  
&& pip install -U pip \  
&& rm -rf /var/cache/apk/* \  
&& ln -s /usr/etc/tvrenamer /etc/tvrenamer  
  
COPY . /tvrenamer/  
  
WORKDIR /tvrenamer  
  
RUN apk add --no-cache --virtual .build-deps \  
git \  
g++ \  
python-dev \  
&& pip install --no-cache-dir -r requirements.txt \  
&& python setup.py install \  
&& apk del .build-deps \  
&& rm -rf /var/cache/apk/* .git/ build/ *.egg-info/  
  
VOLUME ["/usr/etc/tvrenamer"]  
  
CMD ["tvrename"]  

