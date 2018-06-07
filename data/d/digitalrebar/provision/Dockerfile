FROM alpine:3.6  
ARG DRP_VERSION=stable  
ARG DRP_COMMIT=""  
# add glibc so we can run drp executables  
# credit:
http://www.manorrock.com/blog/2016/08/30/docker_tip_6_create_a_base_alpine_glibc_image.html  
RUN ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.23-r3" && \  
ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
apk add --no-cache --virtual=.build-dependencies wget ca-certificates && \  
wget \  
"https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
-O "/etc/apk/keys/sgerrand.rsa.pub" && \  
wget \  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
&& \  
apk add --no-cache \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
\  
rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
\  
apk del glibc-i18n && \  
\  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
ENV LANG=C.UTF-8  
# digital rebar provision install starts here  
EXPOSE 8091 8092 69 67 4011  
ENV INSTALLDIR "/provision"  
# If you set STATICIP, use "--static-ip=<IP>"  
ENV STATICIP ""  
ENV drp "./dr-provision ${STATICIP} --base-root=${INSTALLDIR}/drp-data
--local-content= --default-content="  
COPY tools/install.sh ${INSTALLDIR}/  
WORKDIR ${INSTALLDIR}  
VOLUME ["drp-data"]  
# install provision and its deps  
RUN echo "DRP_VERSION=${DRP_VERSION}"  
RUN apk add --no-cache iproute2 bash ipmitool curl libarchive-tools p7zip &&
./install.sh --isolated install --drp-version=${DRP_VERSION}
\--commit=${DRP_COMMIT}  
# run the api server so we can install sledgehammer image  
RUN ./dr-provision --version || true  
CMD ${drp}  

