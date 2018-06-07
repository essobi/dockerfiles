FROM ubuntu:16.04  
MAINTAINER Jamie Curnow <jc@jc21.com>  
LABEL maintainer="Jamie Curnow <jc@jc21.com>"  
  
ENV S6_FIX_ATTRS_HIDDEN=1  
ENV TMP_DIR /tmp/intensecoin  
RUN echo "fs.file-max = 65535" > /etc/sysctl.conf  
  
RUN apt-get -y update \  
&& apt-get -y --no-install-recommends install wget ca-certificates xz-utils
p7zip-full gawk bzip2  
  
RUN mkdir -p $TMP_DIR \  
&& cd $TMP_DIR \  
&& wget
"https://github.com/valiant1x/intensecoin/releases/download/v2.0.2.1/intensecoin-
cli-linux-64bit-v2.0.2.1.tar.bz2" \  
&& tar xvjf intensecoin-cli-linux-64bit-v2.0.2.1.tar.bz2 \  
&& rm -f intensecoin-cli-linux-64bit-v2.0.2.1.tar.bz2 \  
&& cd intensecoin-cli-linux-64bit-v2.0.2.1 \  
&& chmod +x * \  
&& mv * /usr/local/bin/ \  
&& rm -rf $TMP_DIR  
  
# Contains the blockchain  
VOLUME /root/.intensecoin  
  
# Generate your wallet via accessing the container and run:  
# cd /wallet  
# intense-wallet-cli  
VOLUME /wallet  
  
EXPOSE 48782  
EXPOSE 48772  
WORKDIR /root  
  
# S6 Overlay  
COPY rootfs /  
ADD env/.bashrc /root/  
RUN apt-get -y install curl && curl -L -s https://github.com/just-
containers/s6-overlay/releases/download/v1.21.2.1/s6-overlay-amd64.tar.gz \  
| tar xzf - -C /  
  
CMD [ "/init" ]  

