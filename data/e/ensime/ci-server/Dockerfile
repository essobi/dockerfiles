# https://docs.docker.com/reference/builder/  
# NOTE dockerignore is ignored https://github.com/docker/docker/issues/9455  
  
FROM debian:jessie  
  
MAINTAINER Sam Halliday, sam.halliday@gmail.com  
  
ENV PATH /root/.jenv/shims:/root/.jenv/bin:$PATH  
  
################################################  
# Package Management  
RUN\  
echo 'deb http://repos.azulsystems.com/debian stable main' >>
/etc/apt/sources.list &&\  
echo 'deb http://ftp.debian.org/debian jessie-backports main' >>
/etc/apt/sources.list &&\  
cat /etc/apt/sources.list | sed 's/^deb /deb-src /' >> /etc/apt/sources.list
&&\  
echo 'APT::Install-Recommends "0";' >> /etc/apt/apt.conf &&\  
echo 'APT::Install-Suggests "0";' >> /etc/apt/apt.conf &&\  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 0x219BD9C9
&&\  
apt-get update -qq &&\  
apt-get autoremove -qq &&\  
apt-get clean  
  
################################################  
# Base System  
RUN\  
apt-get install -y host jq curl unzip git locales ca-certificates &&\  
echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen &&\  
locale-gen &&\  
apt-get clean  
  
################################################  
# Java  
RUN\  
apt-get install -y zulu-6 zulu-7 zulu-8 &&\  
git clone https://github.com/gcuisinier/jenv.git /root/.jenv &&\  
apt-get clean &&\  
mkdir /root/.jenv/versions &&\  
jenv add /usr/lib/jvm/zulu-6-amd64 &&\  
jenv add /usr/lib/jvm/zulu-7-amd64 &&\  
jenv add /usr/lib/jvm/zulu-8-amd64 &&\  
jenv global 1.8  
  
################################################  
# SBT (and by implication, Scala)  
ADD https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt /usr/bin/sbt  
RUN chmod a+x /usr/bin/sbt  
RUN\  
mkdir -p ~/.sbt/0.13 &&\  
mkdir /tmp/sbt &&\  
cd /tmp/sbt &&\  
mkdir -p project src/main/scala &&\  
touch src/main/scala/scratch.scala &&\  
touch LICENSE &&\  
touch NOTICE &&\  
echo 'sonatypeGithub := ("ensime", "ensime-docker")' > build.sbt &&\  
echo 'licenses := Seq(Apache2)' >> build.sbt &&\  
echo 'addSbtPlugin("com.fommil" % "sbt-sensible" % "1.2.0")' >
project/plugins.sbt &&\  
for SBT_VERSION in 0.13.16 ; do\  
echo "sbt.version=$SBT_VERSION" > project/build.properties ;\  
for JAVA_VERSION in 1.6 1.7 1.8 ; do\  
echo $JAVA_VERSION > .java-version ;\  
for SCALA_VERSION in 2.10.6 2.11.11 ; do\  
sbt ++$SCALA_VERSION clean updateClassifiers updateSbtClassifiers compile ;\  
done ;\  
done ;\  
echo 1.8 > .java-version ;\  
sbt ++2.12.3 clean updateClassifiers updateSbtClassifiers compile ;\  
done &&\  
rm -rf /tmp/sbt  
  
################################################  
# Emacs  
RUN\  
apt-get -t jessie-backports install -y emacs24 &&\  
apt-get clean  
  
################################################  
# Cask  
RUN\  
apt-get install -y python &&\  
curl -fsSL https://raw.githubusercontent.com/cask/cask/master/go | python &&\  
apt-get clean  
ENV PATH /root/.cask/bin:${PATH}  
  
################################################  
# ensime-vim  
RUN\  
apt-get install -yy make g++ gcc openssl libssl-dev ruby ruby-dev python-mock
python-pip &&\  
pip install websocket-client &&\  
gem install bundle &&\  
apt-get clean  
  
################################################  
# Drone deployment support  
RUN\  
apt-get install -yy openssh-client ccrypt &&\  
apt-get clean &&\  
mkdir /root/.ssh &&\  
chmod 0700 /root/.ssh  
  
################################################  
# ENSIME 1.0 Cache (stable used by ensime-sbt)  
RUN\  
cd /root &&\  
git clone --depth 1 \--branch 1.0 https://github.com/ensime/ensime-server.git
&&\  
cd ensime-server &&\  
for SCALA_VERSION in 2.10.6 2.11.8 ; do\  
sbt ++$SCALA_VERSION ensimeConfig ensimeConfigProject ;\  
done &&\  
cd /root &&\  
rm -rf /root/ensime-server  

