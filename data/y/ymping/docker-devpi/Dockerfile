FROM python:3-alpine  
MAINTAINER https://github.com/ymping/  
  
ENV DEVPI_SERVER_VERSION=4.4.0 \  
DEVPI_WEB_VERSION=3.2.2 \  
DEVPI_CLIENT_VERSION=4.0.0 \  
DEVPI_PASSWORD=devpipass \  
DEVPI_SERVERDIR=/data/server \  
DEVPI_CLIENTDIR=/data/client \  
MIRROR_URL=https://pypi.doubanio.com/simple/  
  
RUN apk add --no-cache build-base libffi-dev bash  
  
RUN pip install --no-cache \  
"devpi-client==${DEVPI_CLIENT_VERSION}" \  
"devpi-web==${DEVPI_WEB_VERSION}" \  
"devpi-server==${DEVPI_SERVER_VERSION}"  
  
EXPOSE 3141  
VOLUME /data  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["devpi"]

