FROM alpine:3.4  
MAINTAINER Yuriy Prokopets <yuriy.prokopets@gmail.com>  
  
ENV TIMEZONE Europe/Kiev  
ENV PHP_MEMORY_LIMIT 64M  
ENV WEB_ROOT /var/www/webgrind  
ENV WEBGRIND_STORAGE_DIR /var/webgrind  
ENV XDEBUG_OUTPUT_DIR /tmp  
ENV PORT 8080  
RUN apk add --update tzdata && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
apk add --no-cache git \  
  
# PHP 5.X and webgrind dependency libraries  
php5 php5-json \  
  
# Python and Graphviz for function call graphs  
python graphviz \  
  
# for making binary preprocessor  
g++ make musl-dev && \  
  
# Install webgrind  
git clone --depth=1 \--branch=master https://github.com/jokkedk/webgrind
$WEB_ROOT && \  
rm -rf $WEB_ROOT/.git && \  
  
# Remove git after installation  
apk del git  
  
RUN \  
# configure php  
sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i" /etc/php5/php.ini
&& \  
sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i"
/etc/php5/php.ini && \  
# configure webgrind  
sed -i "s|.*storageDir =.*|static \$storageDir = '${WEBGRIND_STORAGE_DIR}';|i"
${WEB_ROOT}/config.php && \  
sed -i "s|.*profilerDir =.*|static \$profilerDir = '${XDEBUG_OUTPUT_DIR}';|i"
${WEB_ROOT}/config.php  
  
RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*  
  
RUN mkdir -p $WEBGRIND_STORAGE_DIR  
  
WORKDIR $WEB_ROOT  
# make binary  
RUN make  
  
VOLUME ${XDEBUG_OUTPUT_DIR}  
EXPOSE ${PORT}  
  
CMD ["php", "-S", "0.0.0.0:8080", "index.php"]

