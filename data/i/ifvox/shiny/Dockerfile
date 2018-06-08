FROM alpine:3.5  
  
ENV LANG=C.UTF-8  
  
COPY shiny-server.sh /usr/bin/shiny-server.sh  
COPY shiny-server.conf /etc/shiny-server/shiny-server.conf  
  
################################################################################  
# 0. General setup  
################################################################################  
RUN \  
date && \  
GROUP999=$(grep 999 /etc/group) &&\  
if [ -n "$GROUP999" ]; then delgroup $(echo $GROUP999|cut -f1 -d:); fi && \  
adduser -h /home/shiny -s /sbin/nologin -D -H -u 999 shiny && \  
mkdir ~/.R /home/shiny && \  
chown shiny.shiny /home/shiny && \  
echo "CFLAGS = -D__USE_MISC" > ~/.R/Makevars && \  
apk add --no-cache bash libstdc++ R freetype fontconfig ttf-dejavu libxml2 &&
\  
apk add --no-cache --virtual=.build-dependencies ca-certificates cmake gcc g++
git linux-headers R-dev python unzip wget && \  
  
################################################################################  
# 1. GLIBC setup  
#  
################################################################################  
# blatantly stolen from: https://github.com/frol/docker-alpine-glibc  
# Here we install GNU libc (aka glibc) and set C.UTF-8 locale as default.  
################################################################################  
# ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download" && \  
# ALPINE_GLIBC_PACKAGE_VERSION="2.25-r0" && \  
# ALPINE_GLIBC_BASE_PACKAGE_FILENAME="glibc-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
# ALPINE_GLIBC_BIN_PACKAGE_FILENAME="glibc-
bin-$ALPINE_GLIBC_PACKAGE_VERSION.apk" && \  
#
ALPINE_GLIBC_I18N_PACKAGE_FILENAME="glibc-i18n-$ALPINE_GLIBC_PACKAGE_VERSION.apk"
&& \  
# wget \  
# "https://raw.githubusercontent.com/andyshinn/alpine-pkg-
glibc/master/sgerrand.rsa.pub" \  
# -O "/etc/apk/keys/sgerrand.rsa.pub" && \  
# wget \  
#
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BASE_PACKAGE_FILENAME"
\  
#
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_BIN_PACKAGE_FILENAME"
\  
#
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE_VERSION/$ALPINE_GLIBC_I18N_PACKAGE_FILENAME"
&& \  
# apk add --no-cache \  
# "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
# "$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
# "$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
# \  
# rm "/etc/apk/keys/sgerrand.rsa.pub" && \  
# /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true && \  
# echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
# \  
# apk del glibc-i18n && \  
# \  
# rm "/root/.wget-hsts" && \  
# rm \  
# "$ALPINE_GLIBC_BASE_PACKAGE_FILENAME" \  
# "$ALPINE_GLIBC_BIN_PACKAGE_FILENAME" \  
# "$ALPINE_GLIBC_I18N_PACKAGE_FILENAME" && \  
  
################################################################################  
# 2. SHINY setup  
# https://github.com/rstudio/shiny-server/wiki/Building-Shiny-Server-from-
Source  
################################################################################  
  
cd /usr/local && \  
git clone https://github.com/rstudio/shiny-server.git && \  
  
sed -i.bak
"s/2bf1d83ce3bf3ae856d2af9453832952/9d53413f3d69fbf0bd369f5cebb7dc8b/"
/usr/local/shiny-server/external/pandoc/CMakeLists.txt && \  
  
mkdir -p /usr/local/shiny-server/tmp && \  
cd /usr/local/shiny-server/tmp && \  
PATH=$(pwd)/../bin:$PATH && \  
PYTHON=`which python` && \  
cmake -DCMAKE_INSTALL_PREFIX=/usr/local -DPYTHON="$PYTHON" ../ && \  
make && \  
mkdir ../build && \  
(cd .. && ./bin/npm --python="$PYTHON" install) && \  
(cd .. && ./bin/node ./ext/node/lib/node_modules/npm/node_modules/node-
gyp/bin/node-gyp.js --python="$PYTHON" rebuild) && \  
make install && \  
ln -s /usr/local/shiny-server/bin/shiny-server /usr/bin/shiny-server && \  
mkdir -p /var/log/shiny-server /srv/shiny-server /var/lib/shiny-server
/etc/shiny-server /var/lib/shiny-server/bookmarks/shiny && \  
chown shiny /var/log/shiny-server && \  
R -e "install.packages('shiny', repos='https://cran.rstudio.com/')" R && \  
  
################################################################################  
# 3. Extra SHINY font setup  
################################################################################  
R -e "install.packages(c('Rttf2pt1', 'extrafontdb', 'extrafont'),
repos='https://cran.rstudio.com/');Sys.setlocale('LC_ALL','C');library(extrafont);font_import(prompt=FALSE)"
&& \  
  
################################################################################  
# 4. Build cleanup  
################################################################################  
cd /usr/local/shiny-server/external/node/node-v6.* && \  
make clean && \  
rm -rf /usr/local/shiny-server/tmp /root/.node-gyp /root/.npm && \  
find / -type f -perm /u=x,g=x,o=x -xdev -exec strip -v {} \; && \  
apk del .build-dependencies && \  
date  
  
ENTRYPOINT ["/usr/bin/shiny-server.sh"]  

