FROM httpd:2.4.32-alpine  
  
RUN apk add --update --no-cache bash \  
&& apk add --virtual dependencies \  
autoconf automake \  
ca-certificates coreutils \  
dpkg-dev dpkg file \  
gcc gnupg \  
libc-dev \  
libtool make \  
wget \  
&& cd /tmp \  
&& wget https://storage.googleapis.com/google-code-archive-
downloads/v2/code.google.com/mod-auth-token/mod_auth_token-1.0.5.tar.gz \  
&& tar xf mod_auth_token-1.0.5.tar.gz \  
&& cd mod_auth_token-1.0.5 \  
&& rm -f configure \  
&& autoreconf -fi \  
&& automake -f \  
&& ./configure \  
&& make \  
&& make install \  
&& apk del dependencies \  
&& rm -rf /tmp/*  
  
COPY configs/ /  
  
EXPOSE 80  
  
CMD ["httpd-foreground"]

