FROM hongshunyang/docker-freeradius-mysql  
MAINTAINER Hongshun Yang <yanghongshun@outlook.com>  
  
  
RUN echo "@community http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories  
  
RUN apk add -U freeradius-perl \  
perl-lwp-useragent-determined \  
perl-lwp-protocol-https \  
perl-lwp-mediatypes \  
perl-config-inifiles \  
perl-try-tiny \  
perl-json \  
perl-data-dump@community \  
&& rm -rf /var/cache/apk/*  

