FROM ubuntu:14.04  
MAINTAINER nasuno@ascade.co.jp  
  
# install_base_packages  
RUN apt-get update \  
&& apt-get -y install software-properties-common \  
&& add-apt-repository ppa:openjdk-r/ppa -y \  
&& apt-get update \  
&& apt-get -y install \  
bison \  
curl \  
wget \  
git \  
jq \  
libapr1-dev \  
libcurl4-nss-dev \  
libsasl2-dev \  
libsvn-dev \  
openjdk-8-jdk-headless \  
python-dev \  
iptables \  
xz-utils \  
&& update-alternatives --set java /usr/lib/jvm/java-8-openjdk-
amd64/jre/bin/java \  
&& apt-get install -y zookeeperd \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv E56151BF \  
&& echo "deb http://repos.mesosphere.io/ubuntu trusty main" >
/etc/apt/sources.list.d/mesosphere.list \  
&& apt-get update \  
&& apt-get -y install mesos=0.28.2*  
  
# install Docker-in-Docker <https://hub.docker.com/_/docker/>  
RUN curl -sSL https://get.docker.com/builds/Linux/x86_64/docker-1.10.3 >
/usr/local/bin/docker \  
&& curl -sSL
https://raw.githubusercontent.com/docker/docker/3b5fac462d21ca164b3778647420016315289034/hack/dind
> /usr/local/bin/dind \  
&& curl -sSL https://raw.githubusercontent.com/docker-
library/docker/83b2eab8bdb5d35bf343313154ab55938fca3807/1.10/dind/dockerd-
entrypoint.sh > /usr/local/bin/dockerd-entrypoint.sh \  
&& chmod +x /usr/local/bin/docker /usr/local/bin/dind  
  
# install thrift  
RUN curl -sSL http://apache.org/dist/thrift/KEYS | gpg --import - \  
&& gpg --export --armor 66B778F9 | apt-key add - \  
&& echo 'deb http://www.apache.org/dist/thrift/debian 0.9.1 main' >
/etc/apt/sources.list.d/thrift.list \  
&& apt-get update \  
&& apt-get install thrift-compiler=0.9.1  
  
RUN git clone -b rel/0.15.0 https://github.com/apache/aurora.git /aurora \  
&& mkdir -p /aurora/third_party \  
&& cd /aurora/third_party \  
&& wget
https://svn.apache.org/repos/asf/aurora/3rdparty/ubuntu/trusty64/python/mesos.native-0.28.2-py2.7-linux-x86_64.egg  
  
# build aurora  
RUN cd /aurora \  
&& ./pants binary src/main/python/apache/aurora/kerberos:kaurora_admin \  
&& ./pants binary src/main/python/apache/aurora/kerberos:kaurora \  
&& ./pants binary src/main/python/apache/aurora/executor:thermos_executor \  
&& ./pants binary src/main/python/apache/thermos/runner:thermos_runner \  
&& ./pants binary src/main/python/apache/aurora/tools:thermos_observer \  
&& ./pants binary src/main/python/apache/aurora/tools:thermos \  
&& cp dist/kaurora_admin.pex /usr/local/bin/aurora_admin \  
&& cp dist/kaurora.pex /usr/local/bin/aurora \  
&& build-support/embed_runner_in_executor.py \  
&& chmod +x dist/thermos_executor.pex \  
&& cp dist/thermos.pex /usr/local/bin/thermos \  
&& CLASSPATH_PREFIX=dist/resources/main ./gradlew installDist \  
&& rm -rf /root/.cache /root/.gradle /root/.gnupg /root/.ivy2  
  
# init script  
ADD init.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/init.sh  
  
CMD ["/usr/local/bin/init.sh"]  

