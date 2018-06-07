FROM python:3.6.4-alpine3.7  
LABEL maintainer="technology@unleashed.be"  
  
ARG UID=1000  
ARG GID=1000  
ARG USERNAME=python  
  
RUN set -xe \  
&& apk --no-cache add su-exec \  
&& addgroup -g ${GID} ${USERNAME} \  
&& adduser -D -h /home/python -u ${UID} -G ${USERNAME} ${USERNAME} \  
&& pip install --upgrade pip \  
&& pip install jinja2-cli pyyaml \  
&& find /usr/local \  
\\( -type d -a -name test -o -name tests \\) \  
-o \\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
-exec rm -rf '{}' \+ \  
&& mkdir -p /data  
  
COPY docker-entrypoint.sh /entrypoint  
  
WORKDIR /data  
ENTRYPOINT [ "/entrypoint", "jinja2" ]  
CMD [ "--help" ]  

