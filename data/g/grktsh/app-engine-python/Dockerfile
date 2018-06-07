FROM python:2.7.12-alpine  
  
ENV PYTHONUNBUFFERED 1  
ENV APP_ENGINE_SDK_PYTHON_VERSION 1.9.70  
ENV APP_ENGINE_SDK_PYTHON_SHA1SUM 1a3a7279b6c1cc090c8bf9c7651c35698422f359  
  
RUN set -ex \  
&& apk add --no-cache --virtual .fetch-deps openssl \  
&& wget -qO google_appengine.zip https://storage.googleapis.com/appengine-
sdks/featured/google_appengine_$APP_ENGINE_SDK_PYTHON_VERSION.zip \  
&& apk del .fetch-deps \  
&& echo "$APP_ENGINE_SDK_PYTHON_SHA1SUM google_appengine.zip" | sha1sum -c \  
&& unzip -q google_appengine.zip \  
&& rm -f google_appengine.zip  
  
ENV GAE_SDK_ROOT /google_appengine  
  
ENV PATH /google_appengine:$PATH  

