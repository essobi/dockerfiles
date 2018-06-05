FROM avastsoftware/alpine-perl  
RUN apk add --update g++ make perl-dev libxml2-dev openssl openssl-dev expat-
dev \  
&& rm -rf /var/cache/apk/*  
RUN /usr/bin/cpan App::cpanminus && rm -rf /root/.cpan  
COPY cpanfile /cpanfile  
RUN cd / && cpanm --verbose --no-wget --no-curl --no-lwp --installdeps . \  
&& rm -rf ~/.cpanm /cpanfile  
RUN cpanm RURBAN/Coro-6.4801.tar.gz  
  
#Minilla needs git  
RUN apk add --update git && rm -rf /var/cache/apk/*  

