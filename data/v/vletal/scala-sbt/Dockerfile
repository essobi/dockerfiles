#  
# Scala and sbt Dockerfile  
#  
# https://github.com/hseeberger/scala-sbt  
#  
# -------------------------------------------------- Pull base image  
FROM openjdk:8-jdk  
  
ENV SCALA_VERSION 2.11.11  
ENV SBT_VERSION 0.13.16  
# -------------------------------------------------- Scala expects this file  
RUN touch /usr/lib/jvm/java-8-openjdk-amd64/release  
  
# -------------------------------------------------- Install Scala  
## Piping curl directly in tar  
RUN \  
curl -fsL
https://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /root/ && \  
echo >> /root/.bashrc && \  
echo 'export PATH=~/scala-$SCALA_VERSION/bin:~/bin:$PATH' >> /root/.bashrc  
  
# -------------------------------------------------- Add debian testing
repository  
RUN echo 'deb http://ftp.de.debian.org/debian testing main' >>
/etc/apt/sources.list  
RUN echo 'APT::Default-Release "stable";' | tee -a /etc/apt/apt.conf.d/00local  
RUN apt-get update  
  
# -------------------------------------------------- Install sbt  
RUN \  
curl -L -o sbt-$SBT_VERSION.deb
https://dl.bintray.com/sbt/debian/sbt-$SBT_VERSION.deb && \  
dpkg -i sbt-$SBT_VERSION.deb && \  
rm sbt-$SBT_VERSION.deb && \  
apt-get update && \  
apt-get install sbt && \  
sbt sbtVersion  
  
# -------------------------------------------------- Postgres for testing  
RUN apt-get -y -t testing install postgresql  
RUN apt-get -y -t testing install gcc  
RUN apt-get -y -t testing install \  
libdpkg-perl \  
python3.6 \  
python3.6-tk \  
python3.6-venv \  
python3.6-numpy \  
python3.6-dev  
  
RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6  
  
RUN pip3 install Cython==0.28.1  
  
# -------------------------------------------------- Clean up and stuff  
RUN apt-get -y clean  
RUN apt-get -y autoremove  
  
# -------------------------------------------------- Define working directory  
ENV MATPLOTLIBRC="/root"  
RUN echo "backend : Agg" >> $MATPLOTLIBRC/matplotlibrc  
  
COPY initdb /root/bin/  
COPY postgres /root/bin/  
COPY parse_argument /root/bin/  
  
WORKDIR "/root"  

