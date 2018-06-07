FROM openjdk:8-jdk  
  
ARG KOTLIN_NATIVE_VERSION=master  
  
RUN apt-get update && apt-get install -yq \  
libncurses-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN git clone -b ${KOTLIN_NATIVE_VERSION} \--single-branch --depth 1
https://github.com/JetBrains/kotlin-native.git && \  
cd /kotlin-native && ./gradlew wrapper --gradle-version 3.5 && \  
cd /kotlin-native && ./gradlew dependencies:update && \  
cd /kotlin-native && ./gradlew dist --info --stacktrace && \  
mkdir -p /opt/kotlin-native/ && \  
cp -R /kotlin-native/dist/* /opt/kotlin-native && \  
chmod 755 ${pkgdir}/opt/kotlin-native && \  
ln -s /opt/kotlin-native/bin/cinterop /usr/bin/cinterop && \  
ln -s /opt/kotlin-native/bin/klib /usr/bin/klib && \  
ln -s /opt/kotlin-native/bin/konanc /usr/bin/konanc && \  
ln -s /opt/kotlin-native/bin/kotlinc /usr/bin/kotlinc && \  
ln -s /opt/kotlin-native/bin/kotlinc-native /usr/bin/kotlinc-native && \  
ln -s /opt/kotlin-native/bin/run_konan /usr/bin/run_konan && \  
rm -rf /kotlin-native && \  
rm -rf /root/.gradle && \  
rm -rf /root/.konan && \  
rm -rf /root/.kotlin

