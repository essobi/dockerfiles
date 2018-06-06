FROM sasah/alpine-glibc:latest  
  
ENV JAVA_HOME="/usr/java" \  
JAVA_OPTS="-Dfile.encoding=UTF-8 -Duser.timezone=Europe/Moscow"  
  
RUN JAVA_UPDATE="102" && \  
JAVA_BUILD="14" && \  
  
apk --no-cache add --virtual .build-deps \  
wget \  
ca-certificates && \  
  
cd /tmp && \  
wget -nv --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
https://download.oracle.com/otn-
pub/java/jdk/8u${JAVA_UPDATE}-b${JAVA_BUILD}/server-
jre-8u${JAVA_UPDATE}-linux-x64.tar.gz \  
https://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip \  
https://download.oracle.com/otn-pub/java/tzupdater/2.1.0/tzupdater-2_1_0.zip
&& \  
  
echo "50bc7ff61ba064c471adc2ec08e44690f0dac4cd673a3666b6d7b24a48bd7169 server-
jre-8u${JAVA_UPDATE}-linux-x64.tar.gz" > server-
jre-8u${JAVA_UPDATE}-linux-x64.tar.gz.sha256 && \  
sha256sum -c server-jre-8u${JAVA_UPDATE}-linux-x64.tar.gz.sha256 && \  
echo "f3020a3922efd6626c2fff45695d527f34a8020e938a49292561f18ad1320b59
jce_policy-8.zip" > jce_policy-8.zip.sha256 && \  
sha256sum -c jce_policy-8.zip.sha256 && \  
echo "ab09ceec872eb0c250571628f2f11953bef798945c5ca9b9e5ab6ade978cb63e
tzupdater-2_1_0.zip" > tzupdater-2_1_0.zip.sha256 && \  
sha256sum -c tzupdater-2_1_0.zip.sha256 && \  
  
tar -xzf server-jre-8u${JAVA_UPDATE}-linux-x64.tar.gz && \  
unzip jce_policy-8.zip && \  
unzip tzupdater-2_1_0.zip && \  
mkdir -p /usr/java && \  
cd /tmp/jdk1.8.0_${JAVA_UPDATE} && \  
mv -v * /usr/java && \  
mv -v /tmp/UnlimitedJCEPolicyJDK8/*.jar /usr/java/jre/lib/security && \  
  
/usr/java/bin/jarsigner -verify -verbose -certs
/tmp/tzupdater-2.1.0/tzupdater.jar && \  
/usr/java/bin/java -jar /tmp/tzupdater-2.1.0/tzupdater.jar -V && \  
/usr/java/bin/java -jar /tmp/tzupdater-2.1.0/tzupdater.jar -v -l && \  
  
apk del .build-deps && \  
  
rm -rvf /usr/java/jre/lib/ext/nashorn.jar \  
/usr/java/jre/lib/jfr.jar \  
/usr/java/jre/lib/jfr \  
/usr/java/jre/lib/oblique-fonts \  
/usr/java/jre/lib/tzdb.dat.* \  
  
/usr/java/db \  
/usr/java/include \  
/usr/java/man \  
  
/usr/java/COPYRIGHT \  
/usr/java/LICENSE \  
/usr/java/README.html \  
/usr/java/THIRDPARTYLICENSEREADME.txt \  
  
/usr/java/jre/COPYRIGHT \  
/usr/java/jre/LICENSE \  
/usr/java/jre/README \  
/usr/java/jre/Welcome.html \  
/usr/java/jre/THIRDPARTYLICENSEREADME.txt && \  
  
find -L /usr/java/bin -type f -not -name 'java' -print0 | xargs -0 rm -v -- &&
\  
find -L /usr/java/jre/bin -type f -not -name 'java' -print0 | xargs -0 rm -v
-- && \  
  
ln -sv /usr/java/bin/* /usr/bin/ && \  
  
rm -rvf /tmp/* /root/.oracle_jre_usage  

