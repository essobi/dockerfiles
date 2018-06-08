FROM kylemanna/openvpn  
  
MAINTAINER Maxim Kurbatov <maksimkurb@gmail.com>  
  
RUN apk add --update make gcc g++ libgcrypt libgcrypt-dev \  
&& wget http://www.nongnu.org/radiusplugin/radiusplugin_v2.1a_beta1.tar.gz \  
&& tar xvfz radiusplugin_v2.1a_beta1.tar.gz \  
&& cd radiusplugin_v2.1a_beta1/ \  
&& make \  
&& cp radiusplugin.so /usr/local/share/ \  
&& cd .. \  
&& apk del make gcc g++ libgcrypt-dev \  
&& rm -rf /tmp/* /var/tmp/* /var/cache/apk/* /var/cache/distfiles/*
/radiusplugin_v2.1a_beta1 /radiusplugin_v2.1a_beta1.tar.gz  
  
ADD ./bin /usr/local/bin  
RUN chmod a+x /usr/local/bin/*

