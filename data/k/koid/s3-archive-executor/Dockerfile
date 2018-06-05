FROM alpine  
  
RUN set -x && \  
apk add --update libintl && \  
apk add --virtual build_deps gettext && \  
cp /usr/bin/envsubst /usr/local/bin/envsubst && \  
apk del build_deps  
  
RUN set -x && \  
apk add --update python groff mailcap && \  
apk add --virtual build_deps py-pip && \  
pip install --upgrade awscli && \  
apk del build_deps  
  
RUN set -x && \  
apk add --update ruby  
  
RUN rm /var/cache/apk/*  
  
RUN mkdir -p /bin  
ADD entrypoint.sh /bin/.  
ADD extract /bin/.  
ENV PATH=${PATH}:/bin  
  
ENV APP_ROOT_DIR=/app  
RUN mkdir -p ${APP_ROOT_DIR}  
  
ENV APP_SOCK_DIR=/var/run/sock  
RUN mkdir -p ${APP_SOCK_DIR}  
VOLUME ${APP_SOCK_DIR}  
  
ENTRYPOINT ["/bin/entrypoint.sh"]  

