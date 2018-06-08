FROM unifiedstreaming/origin:1.8.4  
LABEL maintainer "Unified Streaming <support@unified-streaming.com>"  
  
# install  
RUN apk --update add \  
apache2-proxy \  
&& rm -f /var/cache/apk/*  
  
# configure  
RUN sed -i "s/#LoadModule rewrite_module/LoadModule rewrite_module/"
/etc/apache2/httpd.conf \  
&& sed -i "s/LoadModule/#LoadModule/" /etc/apache2/conf.d/proxy.conf \  
&& sed -i "s/#LoadModule proxy_module/LoadModule proxy_module/"
/etc/apache2/conf.d/proxy.conf \  
&& sed -i "s/#LoadModule proxy_http_module/LoadModule proxy_http_module/"
/etc/apache2/conf.d/proxy.conf  
  
RUN wget -q -O /etc/apk/keys/alpine@unified-streaming.com.rsa.pub \  
http://apk.unified-streaming.com/alpine@unified-streaming.com.rsa.pub  
  
RUN apk --update add \  
\--repository http://apk.unified-streaming.com/repo \  
mod_unified_remix=1.8.4-r0 \  
&& rm -f /var/cache/apk/*  
  
COPY unified-origin.conf.in /etc/apache2/conf.d/unified-origin.conf.in  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
RUN chmod +x /usr/local/bin/entrypoint.sh  

