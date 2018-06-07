FROM alpine  
  
ENV version 1.6  
  
RUN apk add \--update \--no-cache ncurses libbz2 xz zlib\  
&& apk add \--virtual=deps \--update \--no-cache ncurses-dev musl-dev g++ make
zlib-dev bzip2-dev xz-dev autoconf automake curl\  
&& cd /tmp \  
&& curl -fsSL https://github.com/samtools/htslib/archive/${version}.tar.gz -o
htslib-${version}.tar.gz\  
&& curl -fsSL https://github.com/samtools/samtools/archive/${version}.tar.gz
-o samtools-${version}.tar.gz \  
&& tar xzvf htslib-${version}.tar.gz\  
&& cd htslib-${version} && autoheader && autoconf \  
&& ./configure \--prefix=/tmp/htslib-${version} && make && make install && cd
..\  
&& tar xzvf samtools-${version}.tar.gz \  
&& cd /tmp/samtools-${version} \  
&& autoconf -Wno-syntax \  
&& ./configure \--with-htslib=/tmp/htslib-${version}
\--prefix=/tmp/samtools-${version} && make && make install
prefix=/tmp/samtools-${version} \  
&& mv /tmp/samtools-${version}/samtools /usr/bin \  
&& rm -rf /var/cache/apk/* /tmp/* \  
&& apk del deps  
  
CMD ["--help"]  
ENTRYPOINT ["/usr/bin/samtools"]  

