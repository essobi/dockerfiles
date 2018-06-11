FROM python:3.6.1-alpine3.6  
WORKDIR /usr/src/app/  
RUN apk --no-cache add --virtual .build-deps \  
build-base \  
openssl-dev \  
libffi-dev \  
zlib-dev  
  
ONBUILD ARG PIP_DISABLE_PIP_VERSION_CHECK=on  
ONBUILD ARG PIP_FIND_LINKS=  
ONBUILD ARG BUILD_DEPS=  
ONBUILD ARG BYPASS_PIP_INSTALL_ERRORS=  
  
ONBUILD RUN echo $BUILD_DEPS | xargs -r apk --no-cache add --virtual .build-
deps  
ONBUILD COPY requirements.txt .  
ONBUILD RUN PIP_FIND_LINKS=$PIP_FIND_LINKS pip install \  
-r requirements.txt  
ONBUILD RUN find /usr/local/lib -type f -name "*.pyc" -delete && \  
find /usr/local/lib -type f -name "*.pyo" -delete && \  
find /usr/local/lib -type d -name "__pycache__" -delete && \  
find /usr/local/lib -type d -name "tests" -exec rm -rf '{}' +  
ONBUILD RUN apk del .build-deps  

