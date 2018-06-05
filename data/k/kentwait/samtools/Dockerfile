# kentwait/samtools  
FROM kentwait/alpine-base  
MAINTAINER Kent Kawashima <kentkawashima@gmail.com>  
  
ENV SAMTOOLS_VERSION 1.3.1  
ENV BCFTOOLS_VERSION 1.3.1  
ENV HTSLIB_VERSION 1.3.2  
ADD
"https://github.com/samtools/samtools/releases/download/${SAMTOOLS_VERSION}/samtools-${SAMTOOLS_VERSION}.tar.bz2"
/tmp/  
ADD
"https://github.com/samtools/bcftools/releases/download/${BCFTOOLS_VERSION}/bcftools-${BCFTOOLS_VERSION}.tar.bz2"
/tmp/  
ADD
"https://github.com/samtools/htslib/releases/download/${HTSLIB_VERSION}/htslib-${HTSLIB_VERSION}.tar.bz2"
/tmp/  
  
WORKDIR /tmp  
RUN apk add --no-cache --virtual temp-pkgs \  
musl-dev \  
zlib-dev \  
ncurses-dev \  
make \  
gcc \  
# Install Samtools  
&& tar xfj samtools-${SAMTOOLS_VERSION}.tar.bz2 \  
&& rm samtools-${SAMTOOLS_VERSION}.tar.bz2 \  
&& cd /tmp/samtools-${SAMTOOLS_VERSION} \  
&& make && make prefix=/usr install \  
&& cd /tmp \  
# Install BCFtools  
&& tar xfj bcftools-${BCFTOOLS_VERSION}.tar.bz2 \  
&& rm bcftools-${BCFTOOLS_VERSION}.tar.bz2 \  
&& cd /tmp/bcftools-${BCFTOOLS_VERSION} \  
&& make && make prefix=/usr install \  
&& cd /tmp \  
# Install HTSlib  
&& tar xfj htslib-${HTSLIB_VERSION}.tar.bz2 \  
&& rm htslib-${HTSLIB_VERSION}.tar.bz2 \  
&& cd /tmp/htslib-${HTSLIB_VERSION} \  
&& make && make prefix=/usr install \  
&& cd /tmp \  
# Create data directory  
&& mkdir -p /data \  
# Remove temp  
&& apk del temp-pkgs \  
&& rm -rf /tmp/* /var/cache/apk/* /root/.wget-hsts /root/.[acpw]*  
  
WORKDIR /data  
VOLUME /data  
ENTRYPOINT ["/init"]  

