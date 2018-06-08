# Singularity v2.5  
#  
# docker run --rm pottava/singularity:2.5  
# docker run --rm --entrypoint cat pottava/singularity:2.5
/usr/local/etc/singularity/singularity.conf  
  
FROM alpine:3.7  
  
ENV SINGULARITY_VERESION=2.5.1  
  
RUN apk --no-cache add bash tar python squashfs-tools  
RUN apk --no-cache add --virtual build-dependencies curl make gcc g++ \  
linux-headers libarchive-dev file \  
&& repo=https://github.com/singularityware/singularity/releases/download \  
&& curl --location --silent --show-error \--out singularity.tar.gz \  
${repo}/${SINGULARITY_VERESION}/singularity-${SINGULARITY_VERESION}.tar.gz \  
&& tar xvf singularity.tar.gz \  
&& cd singularity-${SINGULARITY_VERESION} \  
&& ./configure --prefix=/usr/local \  
&& make -j$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& make install \  
&& cd / \  
&& rm -rf singularity* \  
&& apk del --purge -r build-dependencies  
  
RUN apk --no-cache add \--virtual build-dependencies curl gnupg openssl \  
&& cd /usr/local/bin \  
&& curl \--location --silent --show-error --out gosu \  
https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64 \  
&& curl \--location --silent --show-error --out gosu.asc \  
https://github.com/tianon/gosu/releases/download/1.10/gosu-amd64.asc \  
&& gpg \--keyserver ha.pool.sks-keyservers.net \  
\--recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--batch --verify gosu.asc gosu \  
&& chmod +x gosu \  
&& rm -r gosu.asc \  
&& apk del --purge -r build-dependencies  
  
WORKDIR /work  
  
ADD entrypoint.sh /sbin/  
RUN chmod 755 /sbin/entrypoint.sh  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  

