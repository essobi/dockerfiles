FROM frebib/debian-builder as builder  
  
# Hacky fix for installing openjdk  
RUN mkdir -p /usr/share/man/man1 && \  
apt-get -qy update && \  
apt-get -qy install \  
openjdk-8-jdk \  
cpio \  
unzip \  
zip \  
libcups2-dev \  
libx11-dev \  
libxext-dev \  
libxrender-dev \  
libxtst-dev \  
libxt-dev \  
libasound2-dev \  
libfreetype6-dev \  
libgif-dev  
  
ARG JDK_VER=8  
ARG JDK_UPD=141  
ARG JDK_BLD=15  
ARG JDK_FULLVER=jdk${JDK_VER}u${JDK_UPD}-b${JDK_BLD}  
  
WORKDIR /tmp/${JDK_FULLVER}  
  
# Much of this is adapted from the Linux From Scratch guide  
# http://www.linuxfromscratch.org/blfs/view/svn/general/openjdk.html  
# Fetch and decompress sources  
RUN curl -sSL
http://hg.openjdk.java.net/jdk${JDK_VER}u/jdk${JDK_VER}u/archive/${JDK_FULLVER}.tar.bz2
\  
| tar xj --strip-components=1 && \  
\  
for proj in corba hotspot jaxp jaxws langtools jdk nashorn; do \  
mkdir -p ${proj}; \  
curl -sSL
http://hg.openjdk.java.net/jdk${JDK_VER}u/jdk${JDK_VER}u/${proj}/archive/${JDK_FULLVER}.tar.bz2
\  
| tar xj --strip-components=1 -C ${proj}; \  
done  
  
# Apply appropriate patches  
RUN curl -sSL
https://git.archlinux.org/svntogit/packages.git/plain/trunk/build_with_gcc6.patch?h=packages/java8-openjdk
\  
| patch -p1  
  
# Configure OpenJDK  
RUN sh configure \  
\--prefix=/usr/lib/jvm \  
\--sysconfdir=/etc \  
\--localstatedir=/var \  
\--with-update-version="${JDK_UPD}" \  
\--with-build-number="${JDK_BLD}" \  
\--with-jvm-variants=server \  
\--with-debug-level=release \  
\--disable-debug-symbols \  
\--disable-zip-debug-info \  
\--enable-unlimited-crypto \  
\--with-zlib=system \  
\--with-giflib=system \  
\--with-jobs="$(nproc)" \  
\--with-boot-jdk=/usr/lib/jvm/java-8-openjdk-amd64/ \  
\--with-extra-cflags="${CFLAGS} -Wno-error -fno-delete-null-pointer-checks
-fno-lifetime-dse" \  
\--with-extra-cxxflags="${CXXFLAGS} -fno-delete-null-pointer-checks -fno-
lifetime-dse" \  
\--disable-freetype-bundling \  
\--disable-headful && \  
\  
# Compile OpenJDK  
make images COMPRESS_JARS=true  
# Move and cleanup  
RUN mkdir /output && \  
cp -r build/*/images/j2re-image /output/jvm && \  
cd /output/jvm && \  
# Strip libraries because space  
find . -iname '*.so' -exec strip -s {} + && \  
find . -iname "*.diz" -delete && \  
find . -iname "*.debuginfo" -delete && \  
find . -name "*.jar" -o -name "*.sym" \\! -perm /006 \  
| xargs chmod go+r && \  
rm -rf \  
man \  
release \  
plugin \  
bin/javaws \  
lib/missioncontrol \  
lib/visualvm \  
lib/*jfx* \  
lib/*javafx* \  
lib/plugin.jar \  
lib/ext/jfxrt.jar \  
lib/ext/nashorn.jar \  
lib/javaws.jar \  
lib/images \  
lib/desktop \  
lib/management \  
lib/deploy* \  
lib/amd64/libdecora_sse.so \  
lib/amd64/libprism_*.so \  
lib/amd64/libfxplugins.so \  
lib/amd64/libglass.so \  
lib/amd64/libgstreamer-lite.so \  
lib/amd64/libjavafx*.so \  
lib/amd64/libjfx*.so  
# Generate java/cacerts keystore  
RUN apt-get -qy install p11-kit && \  
mkdir -p /output/certs/java && \  
# Copy cacerts from the debian builder  
# TODO: Move this into a separate package with update scripts  
cp /etc/ssl/certs/ca-certificates.crt /output/certs && \  
trust extract \  
\--format=java-cacerts \  
\--filter=ca-anchors \  
\--purpose=server-auth \  
/output/certs/java/cacerts && \  
# Make Java cacerts keystore available to the JVM  
rm -f /output/jvm/lib/security/cacerts && \  
ln -s /etc/ssl/certs/java/cacerts /output/jvm/lib/security  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
  
FROM adamant/amp  
  
USER root  
  
COPY --from=builder /output/jvm /usr/lib/jvm  
COPY --from=builder /output/certs /etc/ssl/certs  
COPY --from=builder /lib/x86_64-linux-gnu/libz.so.1 /usr/lib  
COPY mc-* /usr/bin/  
  
RUN ldconfig && \  
ln -sv /usr/lib/jvm/bin/* /usr/bin && \  
chmod +rx /usr/bin/mc-*  
  
USER amp  
  
ENV MODULE=Minecraft \  
EXTRAS="+MinecraftModule.Minecraft.PortNumber 25565
+MinecraftModule.Java.MaxHeapSizeMB 3072"  
  
EXPOSE 25565  

