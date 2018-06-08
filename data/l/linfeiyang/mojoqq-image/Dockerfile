FROM alpine:3.7  
RUN apk add --update gcc perl perl-utils make wget perl-io-socket-ssl perl-
crypt-openssl-rsa perl-crypt-openssl-random perl-crypt-openssl-bignum && rm
-rf /var/cache/apk/*  
RUN cpan -i App::cpanminus  
RUN cpanm Encode::Locale IO::Socket::SSL Mojolicious  
RUN cpanm Webqq::Encryption  
  
RUN wget -q https://github.com/sjdy521/Mojo-Webqq/archive/master.zip -OMojo-
Webqq.zip \  
&& unzip -qo Mojo-Webqq.zip \  
&& cd Mojo-Webqq-master \  
&& cpanm . \  
&& cd .. \  
&& rm -rf Mojo-Webqq-master Mojo-Webqq.zip  
ADD main.pl main.pl  
CMD ["perl","main.pl"]  

