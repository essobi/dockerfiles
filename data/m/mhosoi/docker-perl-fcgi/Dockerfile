FROM alpine:3.5  
RUN apk update && apk add perl fcgiwrap curl perl-dbi perl-list-moreutils
perl-readonly perl-uri perl-json perl-lwp-protocol-https perl-dbd-sqlite \  
&& apk add \--no-cache --virtual=build_dependencies gcc make perl-dev musl-dev
\  
&& curl -LO https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm
\  
&& export PERL_CPANM_OPT="--verbose --mirror https://cpan.metacpan.org
--mirror-only" \  
&& chmod +x cpanm \  
&& ./cpanm --no-wget App::cpanminus \  
&& rm -fr ./cpanm \  
&& cpanm --no-wget CGI::Minimal URI::Escape FindBin File::Basename File::Path
Smart::Comments HTTP::Request::Common JSON::XS Cache::FileCache Text::Xslate \  
&& apk del build_dependencies \  
&& rm -rf /var/cache/apk/*  
  
  
  
#ADD echo.pl /cgi-bin/echo.pl  
#ENTRYPOINT [ "fcgiwrap", "-s", "tcp:0.0.0.0:9999", "-f" ]  
#EXPOSE 9999  

