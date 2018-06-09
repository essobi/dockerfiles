FROM alpine:3.7  
LABEL MAINTAINER="Youqing Han"  
  
ENV APP="bitcoin" \  
CLUSTER="CLUSTER_NAME" \  
PROVIDER="alicloud" \  
REGION="cn-beijing" \  
WORKDIR="/opt"  
  
ENV BITCOIN_VER="0.16.0" \  
GLIBC_VER="2.27-r0"  
ENV BITCOIN_TGZ="bitcoin-${BITCOIN_VER}-x86_64-linux-gnu.tar.gz"  
ENV BITCOIN_URL="https://bitcoin.org/bin/bitcoin-
core-${BITCOIN_VER}/${BITCOIN_TGZ}" \  
BITCOIN_DIR="${WORKDIR}/bitcoin" \  
BITCOIN_DATADIR="${WORKDIR}/bitcoindata" \  
GLIBC_PKG="glibc-${GLIBC_VER}.apk" \  
GLIBC_BIN="glibc-bin-${GLIBC_VER}.apk" \  
GLIBC_DOWNLOAD_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VER}"  
ENV PATH=".:${BITCOIN_DIR}/bin:${PATH}"  
RUN set -xe; \  
sed -i 's#^#\\##g' /etc/apk/repositories; \  
sed -i '1ihttp://mirrors.ustc.edu.cn/alpine/v3.6/main/' /etc/apk/repositories;
\  
sed -i '1ihttp://mirrors.ustc.edu.cn/alpine/v3.6/community/'
/etc/apk/repositories; \  
sed -i '1ihttps://mirrors.tuna.tsinghua.edu.cn/alpine/v3.6/main/'
/etc/apk/repositories; \  
sed -i '1ihttps://mirrors.tuna.tsinghua.edu.cn/alpine/v3.6/community/'
/etc/apk/repositories; \  
apk update && apk add --no-cache \  
wget \  
ca-certificates \  
&& \  
mkdir -p ${WORKDIR} ${BITCOIN_DATADIR}  
  
WORKDIR ${WORKDIR}  
  
ADD sgerrand.rsa.pub /etc/apk/keys/sgerrand.rsa.pub  
#ADD . /opt  
RUN set -xe; \  
# "wget -q -O /etc/apk/keys/sgerrand.rsa.pub
${GLIBC_DOWNLOAD_URL}/sgerrand.rsa.pub"  
wget ${GLIBC_DOWNLOAD_URL}/${GLIBC_PKG} && \  
wget ${GLIBC_DOWNLOAD_URL}/${GLIBC_BIN} && \  
wget ${BITCOIN_URL} && \  
apk add \--no-cache ${GLIBC_PKG} && \  
apk add --no-cache ${GLIBC_BIN} && \  
tar xvf ${BITCOIN_TGZ} && \  
mv bitcoin-${BITCOIN_VER} bitcoin && \  
apk del wget ca-certificates && \  
rm -rf /var/cache/apk/* ~/.cache/ /tmp/* *.apk *.tar.gz  
  
VOLUME ${BITCOIN_DATADIR}  
  
EXPOSE 8333 8332  
CMD ["sh", "-c", "bitcoind -datadir=${BITCOIN_DATADIR} -printtoconsole"]  

