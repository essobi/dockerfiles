# Start from alpine linux 3.6.*  
FROM alpine:3.6  
  
# Install glib 2.26  
RUN ALPINE_GLIBC_APK_BASE_URL="https://github.com/MihaiBogdanEugen/alpine-
glibc-apk/releases/download" && \  
ALPINE_GLIBC_APK_VERSION="2.26-r1" && \  
ALPINE_GLIBC_APK="glibc-$ALPINE_GLIBC_APK_VERSION.apk" && \  
ALPINE_GLIBC_BIN_APK="glibc-bin-$ALPINE_GLIBC_APK_VERSION.apk" && \  
ALPINE_GLIBC_I18N_APK="glibc-i18n-$ALPINE_GLIBC_APK_VERSION.apk" && \  
ID_RSA_PUB_SHA256_SUM="26df3c56980ba67f5dda27d290bfa708dc8d991f9f5fcc74bea87b7191e255f9"
&& \  
ALPINE_GLIBC_APK_SHA256_SUM="b1344b3f859dbeba5a777d0778b242f6915151b431db5e36883099def4e5bd49"
&& \  
ALPINE_GLIBC_BIN_APK_SHA256_SUM="8a079d22262be9d4f410f5cf24f7eb6fcb49f747aedade4ea3b2560bc0250032"
&& \  
ALPINE_GLIBC_I18N_APK_SHA256_SUM="99844762b136d6a11f1355c251166cfcdc1cb03a34cd3d9d8744b52c84b3ec48"
&& \  
apk add \--no-cache \--virtual=.build-dependencies wget ca-certificates && \  
wget \  
"https://raw.githubusercontent.com/MihaiBogdanEugen/alpine-glibc-
apk/master/user.abuild/mbe1224%40gmail.com.rsa.pub" \  
-O "/etc/apk/keys/mbe1224@gmail.com.rsa.pub" && \  
echo "${ID_RSA_PUB_SHA256_SUM} /etc/apk/keys/mbe1224@gmail.com.rsa.pub" |
sha256sum -c - && \  
wget "$ALPINE_GLIBC_APK_BASE_URL/$ALPINE_GLIBC_APK_VERSION/$ALPINE_GLIBC_APK"
&& \  
echo "${ALPINE_GLIBC_APK_SHA256_SUM} ${ALPINE_GLIBC_APK}" | sha256sum -c - &&
\  
wget
"$ALPINE_GLIBC_APK_BASE_URL/$ALPINE_GLIBC_APK_VERSION/$ALPINE_GLIBC_BIN_APK"
&& \  
echo "${ALPINE_GLIBC_BIN_APK_SHA256_SUM} ${ALPINE_GLIBC_BIN_APK}" | sha256sum
-c - && \  
wget
"$ALPINE_GLIBC_APK_BASE_URL/$ALPINE_GLIBC_APK_VERSION/$ALPINE_GLIBC_I18N_APK"
&& \  
echo "${ALPINE_GLIBC_I18N_APK_SHA256_SUM} ${ALPINE_GLIBC_I18N_APK}" |
sha256sum -c - && \  
apk add \--no-cache \  
"$ALPINE_GLIBC_APK" \  
"$ALPINE_GLIBC_BIN_APK" \  
"$ALPINE_GLIBC_I18N_APK" && \  
\  
rm "/etc/apk/keys/mbe1224@gmail.com.rsa.pub" && \  
/usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
\  
apk del glibc-i18n && \  
\  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm \  
"$ALPINE_GLIBC_APK" \  
"$ALPINE_GLIBC_BIN_APK" \  
"$ALPINE_GLIBC_I18N_APK"  
# set UTF-8 locale as default  
ENV LANG=C.UTF-8

