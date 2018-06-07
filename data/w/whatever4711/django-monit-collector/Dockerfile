FROM python:3.6-alpine  
  
ENV ARCH amd64  
COPY ./requirements.txt .  
COPY ./gunicornup.sh /usr/local/bin/  
COPY ./pythonstart.sh /usr/local/bin/  
  
# Problem with dockerize on AARCH64, need to use armhf-version  
RUN BUILD_DEPS="ca-certificates wget" && \  
DOCKERIZE_ARCH=$(echo "${ARCH}" | sed -e "s/aarch64/armhf/g") && \  
apk add --update --no-cache postgresql-client postgresql-dev sqlite g++ gcc
libxslt-dev tini ${BUILD_DEPS} && \  
pip install --no-cache-dir -r requirements.txt && \  
wget -O dockerize.tar.gz
https://github.com/jwilder/dockerize/releases/download/v0.3.0/dockerize-
linux-${DOCKERIZE_ARCH}-v0.3.0.tar.gz && \  
tar -xzvf dockerize.tar.gz && \  
rm dockerize.tar.gz && \  
mv dockerize /usr/local/bin/ && \  
apk del ${BUILD_DEPS} && \  
chmod +x /usr/local/bin/gunicornup.sh && \  
chmod +x /usr/local/bin/pythonstart.sh && \  
mkdir -p /usr/src/logs/  
  
WORKDIR /usr/src/app  
  
VOLUME ["/usr/src/logs/","/usr/src/app/static"]  
ENTRYPOINT ["tini", "--", "pythonstart.sh"]  

