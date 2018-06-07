FROM debian:stretch  
MAINTAINER juniorcesar.utfpr@gmail.com  
  
ENV LINK_JRE=http://download.oracle.com/otn-
pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jre-8u151-linux-x64.tar.gz
\  
JAVA_BIN="/usr/java/jre1.8.0_151/bin/java"  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install wget nano net-tools htop
apt-utils --no-install-recommends -y \  
&& mkdir /usr/java \  
&& wget --no-cookies --no-check-certificate --header "Cookie:
gpw_e24=http%3A%2F%2Fwww.oracle.com%2F; oraclelicense=accept-securebackup-
cookie" ${LINK_JRE} -O /tmp/jre.tar.gz \  
&& tar -xvzf /tmp/jre.tar.gz -C /usr/java/ \  
&& rm -f /usr/java/jre.tar.gz \  
&& update-alternatives --install "/usr/bin/java" "java" ${JAVA_BIN} 1 \  
&& echo "America/Sao_Paulo" > /etc/timezone \  
&& ln -fs /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \  
&& apt-get clean  
  
CMD [ "bash" ]  

