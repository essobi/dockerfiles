FROM mhoush/py3  
MAINTAINER https://github.com/m-housh  
  
RUN apk add --update --no-cache --purge \  
openssl \  
git && \  
pip install --no-cache-dir --upgrade --ignore-installed \  
pip \  
devpi-client \  
setuptools \  
sphinx  
  
COPY entrypoint.sh /  
  
VOLUME /mnt  
VOLUME /site-packages  
VOLUME /root/.pip  
  
WORKDIR /mnt  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["--help"]  

