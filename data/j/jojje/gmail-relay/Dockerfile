FROM alpine:3.6  
MAINTAINER Jonas Tingeborn <github.com/jojje>  
  
# Add static utility for changing user description (name)  
RUN apk add --no-cache -t deps gcc make libc-dev curl \  
&& DIR=$(mktemp -d) && cd ${DIR} \  
&& curl -sL https://pkg-shadow.alioth.debian.org/releases/shadow-4.2.1.tar.xz
| xzcat | tar --strip-components=1 -xf - \  
&& ./configure --without-nscd \  
&& make -j$(grep -c processor /proc/cpuinfo) LDFLAGS=-all-static \  
&& strip src/chfn \  
&& cp src/chfn /usr/local/bin/ \  
&& cd && rm -rf ${DIR} \  
&& apk del deps  
  
# Add the *real* content of the container  
RUN apk add --no-cache ssmtp  
COPY conf/ssmtp.conf /etc/ssmtp/ssmtp.conf  
COPY init-mailer.sh /usr/local/bin/init-mailer  
ENTRYPOINT ["/usr/local/bin/init-mailer"]  

