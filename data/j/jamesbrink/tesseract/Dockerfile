# Tesseract  
#  
# VERSION 3.05.01  
  
FROM alpine:3.7  
  
ARG VCS_REF  
ARG BUILD_DATE  
  
LABEL maintainer="James Brink, brink.james@gmail.com" \  
decription="Tesseract OCR" \  
version="3.05.01" \  
org.label-schema.name="Tesseract OCR" \  
org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/jamesbrink/docker-tesseract" \  
org.label-schema.schema-version="1.0.0-rc1"  
# Create our tesseract user  
RUN addgroup -g 1000 -S tesseract \  
&& adduser -u 1000 -S -h /tesseract -s /bin/sh -G tesseract tesseract  
  
# Install all needed runtime dependencies.  
RUN set -xe; \  
apk add --update --no-cache --virtual .runtime-deps \  
bash \  
cairo \  
giflib \  
icu \  
libjpeg-turbo \  
libpng \  
libwebp-dev \  
openjpeg \  
pango \  
tiff \  
zlib; \  
apk add --no-cache --virtual .build-deps \  
alpine-sdk \  
autoconf \  
automake \  
cairo-dev \  
giflib-dev \  
git \  
icu-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
libtool \  
libwebp-dev \  
openjpeg-dev \  
pango-dev \  
tiff-dev \  
zlib-dev; \  
cd /var/tmp; \  
wget http://www.leptonica.org/source/leptonica-1.75.3.tar.gz; \  
tar xfv leptonica-1.75.3.tar.gz; \  
rm leptonica-1.75.3.tar.gz; \  
cd leptonica-1.75.3; \  
./configure --prefix=/usr/local/; \  
make; \  
make install; \  
cd /var/tmp; \  
rm -rf leptonica-1.75.3; \  
git clone https://github.com/tesseract-ocr/tesseract.git; \  
cd tesseract; \  
git checkout 3.05.01; \  
./autogen.sh; \  
./configure --prefix=/usr/local/; \  
make; \  
make install; \  
cd /var/tmp; \  
rm -rf tesseract; \  
mkdir -p /tesseract/tessdata; \  
cd /tesseract/tessdata/; \  
wget https://github.com/tesseract-ocr/tessdata/raw/3.04.00/eng.traineddata; \  
cd /; \  
chown -R tesseract:tesseract /tesseract; \  
apk del .build-deps;  
  
# Copy our docker assets.  
COPY ./docker-entrypoint.sh /usr/local/bin/entrypoint.sh  
  
# Drop down to our unprivileged user account.  
USER tesseract  
  
# Set our working directory.  
WORKDIR /tesseract  
  
# Set our environment variables.  
ENV TESSDATA_PREFIX=/tesseract/tessdata  
  
# Setup the data volume.  
VOLUME ["/tesseract/data"]  
  
# Set our entrypoint.  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]

