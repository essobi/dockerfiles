FROM httpd:2.4-alpine  
  
RUN set -x \  
&& runDeps=' \  
perl \  
opensp \  
ca-certificates \  
' \  
&& apk add --no-cache --virtual .build-deps \  
perl-dev \  
libc-dev \  
opensp-dev \  
gcc \  
g++ \  
make \  
libxml2-dev \  
zlib-dev \  
git \  
tar \  
wget \  
\  
&& perl -MCPAN -e 'install HTML::Tidy' \  
&& perl -MCPAN -e 'install SGML::Parser::OpenSP' \  
&& perl -MCPAN -e 'install Bundle::W3C::Validator' \  
&& wget \--quiet http://www.eu.apache.org/dist/perl/mod_perl-2.0.10.tar.gz \  
&& tar -zxvf mod_perl-2.0.10.tar.gz \  
&& rm mod_perl-2.0.10.tar.gz \  
&& cd mod_perl-2.0.10 \  
&& perl Makefile.PL MP_AP_PREFIX=/usr/local/apache2 \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -Rf mod_perl-2.0.10 \  
&& mkdir -p /usr/local \  
&& git clone https://github.com/w3c/markup-validator.git /usr/local/validator
\  
&& mkdir -p /etc/w3c \  
&& cp -r /usr/local/validator/htdocs/config/* /etc/w3c \  
&& sed 's/Allow Private IPs = no/Allow Private IPs = yes/' -i
/etc/w3c/validator.conf \  
&& sed 's/#HTML5/HTML5/' -i /etc/w3c/validator.conf \  
&& sed 's!/html5/!/!' -i /etc/w3c/validator.conf \  
&& echo 'LoadModule perl_module modules/mod_perl.so' >>
/usr/local/apache2/conf/httpd.conf \  
&& echo 'Include /usr/local/validator/httpd/conf/w3c.conf' >>
/usr/local/apache2/conf/httpd.conf \  
&& sed 's/#LoadModule rewrite_module/LoadModule rewrite_module/' -i
/usr/local/apache2/conf/httpd.conf \  
&& sed 's/#LoadModule expires_module/LoadModule expires_module/' -i
/usr/local/apache2/conf/httpd.conf \  
&& sed 's/#LoadModule cgid_module/LoadModule cgid_module/' -i
/usr/local/apache2/conf/httpd.conf \  
&& sed 's/#LoadModule cgi_module/LoadModule cgi_module/' -i
/usr/local/apache2/conf/httpd.conf \  
&& sed 's/#LoadModule include_module/LoadModule include_module/' -i
/usr/local/apache2/conf/httpd.conf \  
&& sed 's/#LoadModule deflate_module/LoadModule deflate_module/' -i
/usr/local/apache2/conf/httpd.conf \  
&& sed 's/#LoadModule negotiation_module/LoadModule negotiation_module/' -i
/usr/local/apache2/conf/httpd.conf \  
&& apk add --virtual .validator-rundeps $runDeps \  
&& apk del .build-deps  
  
  
  
COPY w3c.conf /usr/local/validator/httpd/conf/w3c.conf  

