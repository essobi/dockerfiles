FROM alpine:3.3  
RUN apk add --update perl libxml2 openssl expat bash \  
  
#install this to compile cpan XML library  
&& apk add \--virtual build \  
g++ make perl-dev libxml2-dev openssl-dev expat-dev \  
  
#install cpan then cleanup  
&& cpan install XML::LibXML LWP::Protocol::http10 LWP::Protocol::https \  
&& rm -rf $HOME/.cpan/build/* \  
$HOME/.cpan/sources/authors/id \  
$HOME/.cpan/cpan_sqlite_log.* \  
/tmp/cpan_install_*.txt \  
  
#cleanup unneed packages  
&& apk del build \  
&& rm -rf /var/cache/apk/*  
  
COPY aliases.sh /etc/profile.d/aliases.sh  
COPY . /test/  
  
WORKDIR /test/  
ENTRYPOINT ["./entrypoint.sh"]  
CMD ["test"]  
  
LABEL org.label-schema.docker.dockerfile="/Dockerfile" \  
org.label-schema.license="MIT" \  
org.label-schema.name="HTTP Test" \  
org.label-schema.vcs-type="Git" \  
org.label-schema.vcs-url="https://github.com/allamand/http-tests"  

