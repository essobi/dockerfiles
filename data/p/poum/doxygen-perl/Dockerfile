FROM alpine:3.6  
LABEL maintainer "Philippe Poumaroux <poum@cpan.org>"  
  
RUN apk add --update graphviz doxygen perl curl wget make && \  
curl -L -o /usr/local/bin/cpanm
https://raw.githubusercontent.com/miyagawa/cpanminus/master/cpanm && \  
chmod +x /usr/local/bin/cpanm && \  
cpanm Doxygen::Filter::Perl && \  
apk del curl wget make && \  
rm -rf ./cpanm /root/.cpanm /var/cache/apk/*  
  
WORKDIR /tmp  
CMD ["/usr/bin/doxygen"]  

