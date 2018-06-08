FROM postgres:9.6.3-alpine  
MAINTAINER mouflon-jp  
  
ENV FIAPSTORAGE_DIST_URL http://fiap-dev.gutp.ic.i.u-tokyo.ac.jp/dist  
ENV FIAPSTORAGE_VERSION 20170406  
ENV FIAPSTORAGE_SHA512
f4b262f469f082d54a4de5b96d545a74f780f4bec54fffcf42f3c650ec5cd2e2c8a25e7565da4d9b0deb00e5f349f46d188664f9a7f957fc23c66670428066fc  
  
RUN cd /tmp \  
&& wget -O FIAPStorage2.zip
"${FIAPSTORAGE_DIST_URL}/FIAPStorage2-${FIAPSTORAGE_VERSION}.zip" \  
&& echo "${FIAPSTORAGE_SHA512} *FIAPStorage2.zip" | sha512sum -c - \  
&& unzip -q FIAPStorage2.zip \  
&& rm FIAPStorage2.zip \  
&& cp /tmp/FIAPStorage2/fiapstorage2.sql /docker-entrypoint-initdb.d/ \  
&& sed -i -e '8i CREATE DATABASE fiapstorage2;\r' /docker-entrypoint-
initdb.d/fiapstorage2.sql \  
&& sed -i -e '9i \\\\\\\c fiapstorage2\r' /docker-entrypoint-
initdb.d/fiapstorage2.sql \  
&& rm -rf /tmp/FIAPStorage2/  
  
WORKDIR /  
ENTRYPOINT ["docker-entrypoint.sh"]  
EXPOSE 5432  
CMD ["postgres"]

