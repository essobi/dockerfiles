FROM composer  
  
LABEL maintainer "Yushin Washio <yuwash at yandex dot com>"  
  
RUN composer global require couscous/couscous  
  
# mercurial has python2 dependency but we want to use python3  
RUN set -x \  
&& apk del \  
mercurial \  
&& apk add --no-cache \  
python3 \  
&& cd $(dirname $(which python3)) \  
&& ln -s python3 python  
  
# Add global binary directory to PATH and make sure to re-export it  
ENV PATH $COMPOSER_HOME/vendor/bin:$PATH  
  
WORKDIR /project  
EXPOSE 8000  
ENTRYPOINT ["couscous"]  

