FROM alpine  
MAINTAINER Xavier Garnier 'xavier.garnier@irisa.fr'  
# Environment variables  
ENV VIRTUOSO https://github.com/openlink/virtuoso-opensource.git  
ENV VIRTUOSO_DIR /virtuoso-opensource  
ENV VIRTUOSO_VERSION 7.2.4.2  
# Copy patch file  
COPY vos-alpine-build.diff.txt /vos-alpine-build.diff.txt  
  
# Install prerequisites, Download, Patch, compile and install  
RUN apk add --update git automake autoconf automake libtool bison flex gawk
gperf openssl g++ openssl-dev make py-pip && \  
pip install crudini && \  
git clone -b v${VIRTUOSO_VERSION} \--single-branch --depth=1 ${VIRTUOSO}
${VIRTUOSO_DIR} && \  
cd ${VIRTUOSO_DIR} && \  
cd ${VIRTUOSO_DIR}/libsrc/odbcsdk/include && patch < /vos-alpine-
build.diff.txt && cd ${VIRTUOSO_DIR} && \  
./autogen.sh && \  
CFLAGS="-O2 -m64" && export CFLAGS && \  
./configure --disable-bpel-vad --enable-conductor-vad --enable-fct-vad
--disable-dbpedia-vad --disable-demo-vad --disable-isparql-vad --disable-ods-
vad --disable-sparqldemo-vad --disable-syncml-vad --disable-tutorial-vad
--program-transform-name="s/isql/isql-v/" && \  
make -j $(grep -c '^processor' /proc/cpuinfo) && \  
make -j $(grep -c '^processor' /proc/cpuinfo) install && \  
ln -s /usr/local/virtuoso-opensource/var/lib/virtuoso/ /var/lib/virtuoso && \  
ln -s /var/lib/virtuoso/db /data && \  
cd / && rm -rf ${VIRTUOSO_DIR} vos-alpine-build.diff.txt /var/cache/apk/*  
  
# Add Virtuoso bin to the PATH  
ENV PATH /usr/local/virtuoso-opensource/bin/:$PATH  
  
# Copy files  
COPY virtuoso.ini /virtuoso.ini  
COPY dump_nquads_procedure.sql /dump_nquads_procedure.sql  
COPY clean-logs.sh /clean-logs.sh  
COPY virtuoso.sh /virtuoso.sh  
  
VOLUME /data  
WORKDIR /data  
EXPOSE 8890 1111  
CMD ["/virtuoso.sh"]  

