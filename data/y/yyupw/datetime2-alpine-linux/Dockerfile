# TeXOSQuery uses Java  
FROM openjdk:8-alpine  
  
MAINTAINER Yuu YOSHIMURA <yyu [at] mental.poker>  
  
# If you bulid this not in Japanese, you should use the following argument:  
# ARG REPOSITORY=http://ctan.sharelatex.com/tex-archive/systems/texlive/tlnet  
ARG REPOSITORY=http://ftp.jaist.ac.jp/pub/CTAN/systems/texlive/tlnet  
  
ENV PATH=/usr/local/texlive/bin/x86_64-linux:$PATH  
  
ENV LANG=ja_JP.UTF-8  
# Install glibc and Set ja_JP.UTF-8 locale as default  
# This is referred from frolvlad/alpine-glibc  
RUN ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
ALPINE_GLIBC_PACKAGE_VERSION="2.25-r0" && \  
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
ja_JP.UTF-8 || true && \  
echo "export LANG=ja_JP.UTF-8" > /etc/profile.d/locale.sh && \  
\  
apk del glibc-i18n && \  
\  
rm "/root/.wget-hsts" && \  
apk del .build-dependencies && \  
rm \  
"$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
"$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"  
  
# Set timezone to Tokyo  
RUN apk --no-cache add tzdata && \  
cp /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
echo 'Asia/Tokyo' > /etc/timezone && \  
apk --no-cache del tzdata  
  
# Copy TeXLive install profile  
RUN mkdir -p /tmp/install-tl-unx  
  
COPY texlive.profile /tmp/install-tl-unx/texlive.profile  
  
# Install TeXLive  
RUN apk --no-cache add wget perl fontconfig-dev xz tar && \  
wget -qO- "$REPOSITORY/install-tl-unx.tar.gz" | \  
tar -xz -C /tmp/install-tl-unx --strip-components=1 && \  
/tmp/install-tl-unx/install-tl \  
-profile /tmp/install-tl-unx/texlive.profile \  
-repository http://ftp.jaist.ac.jp/pub/CTAN/systems/texlive/tlnet && \  
tlmgr \  
-repository $REPOSITORY \  
install \  
collection-luatex collection-fontsrecommended datetime2 texosquery \  
tracklang etoolbox xkeyval && \  
apk --no-cache del wget fontconfig-dev xz tar && \  
rm -rf /tmp/install-tl-unx  
  
# Make working directory  
RUN mkdir /workdir  
  
# Compile TeX file  
COPY dtmnow.tex /workdir/dtmnow.tex  
  
COPY mwe.tex /workdir/mwe.tex  
  
RUN cd /workdir && \  
lualatex dtmnow.tex && \  
lualatex --shell-escape mwe.tex  
  
# Install bash  
RUN apk --no-cache add bash  
  
WORKDIR /workdir  
  
VOLUME ["/workdir"]  
  
CMD ["bash"]  

