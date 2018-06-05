FROM debian:stretch as builder  
  
RUN set -xe \  
&& echo 'deb http://ftp.debian.org/debian stretch-backports main' >>
/etc/apt/sources.list.d/stretch-backports.list \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -qq \  
&& apt-get dist-upgrade -qq \  
&& apt-get install -qqy --no-install-recommends \  
openjdk-9-jdk-headless \  
git-core \  
&& mkdir /var/sources  
  
COPY gradle /var/sources/gradle  
COPY gradlew /var/sources/gradlew  
  
# Download gradle in a separate layer  
RUN set -xe \  
&& cd /var/sources \  
&& ./gradlew --no-daemon --version  
  
COPY . /var/sources  
  
RUN set -xe \  
&& cd /var/sources \  
&& ./gradlew --no-daemon jar  
  
  
  
FROM debian:stretch  
  
RUN set -xe \  
&& echo 'deb http://ftp.debian.org/debian stretch-backports main' >>
/etc/apt/sources.list.d/stretch-backports.list \  
&& export DEBIAN_FRONTEND=noninteractive \  
&& apt-get update -qq \  
&& apt-get dist-upgrade -qq \  
&& apt-get install -qqy --no-install-recommends \  
openjdk-9-jre-headless \  
&& SUDO_FORCE_REMOVE=yes apt-get autoremove -qq \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& mkdir -p /etc/beholder \  
&& mkdir -p /var/log/beholder  
  
COPY --from=builder /var/sources/build/libs /root  
COPY docker/beholder /sbin/  
COPY docker/beholder.conf /etc/beholder/  
  
CMD [ \  
"/usr/bin/java", \  
"-server", \  
"-Xms12m", \  
"-jar", \  
"/root/beholder-0.1.jar", \  
"--config-file=/etc/beholder/beholder.conf" \  
]  

