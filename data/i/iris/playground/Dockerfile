# Copyright (c) 2014 Project Iris. All rights reserved.  
#  
# The current Docker container is the official playground for the Iris  
# client libraries, and as such, the same licensing terms apply.  
# For details please see http://iris.karalabe.com/downloads#License  
# Notes:  
# - Disable IP forwarding to prevent malicious egress traffic  
# - Add monitoring to automatically restart if container crashes  
# crontab -l  
# */1 * * * * /root/playground.sh  
#  
# $ cat playground.sh  
# # Check if no active playground container exists  
# if [ "`docker ps | grep iris/playground`" == "" ]; then  
# # Clean up any previous leftovers  
# docker rm -f $(docker ps -a -q)  
#  
# # Start a fresh container  
# docker run -d -p 3999:3999 iris/playground  
# fi  
FROM opensuse:13.1  
MAINTAINER Péter Szilágyi <peterke@gmail.com>  
  
# Inject fresh language repositories, install them and do a system upgrade  
RUN \  
zypper ar -f
http://download.opensuse.org/repositories/devel:/languages:/go/openSUSE_13.1/
Go && \  
zypper ar -f
http://download.opensuse.org/repositories/devel:/languages:/python3/openSUSE_13.1
Python && \  
zypper ar -f
http://download.opensuse.org/repositories/devel:/languages:/erlang:/Factory/openSUSE_13.1/
Erlang && \  
zypper ar -f
http://download.opensuse.org/repositories/Java:/Factory/openSUSE_13.1/ Java &&
\  
zypper ar -f
http://download.opensuse.org/repositories/devel:/tools:/building/openSUSE_13.1/
BuildTools && \  
zypper --gpg-auto-import-keys --non-interactive ref && \  
zypper --non-interactive dup && \  
zypper --non-interactive install go erlang java-1_8_0-openjdk
java-1_8_0-openjdk-devel maven python3 python3-devel \  
python3-pip libzmq3 zeromq-devel wget tar git mercurial && \  
pip install circus  
  
# Create a small script to download binaries and validate their checksum  
ENV FETCH ./fetch.sh  
RUN \  
echo '#!/bin/bash' > $FETCH && \  
echo 'set -e' >> $FETCH && \  
echo 'file=`basename $1`' >> $FETCH && \  
echo 'echo "Downloading $1..."' >> $FETCH && \  
echo 'wget -q $1' >> $FETCH && \  
echo 'echo "$2 $file" > $file.sum' >> $FETCH && \  
echo 'sha1sum -c $file.sum' >> $FETCH && \  
echo 'rm $file.sum' >> $FETCH && \  
chmod +x $FETCH  
  
# Download and configure the Scala distribution  
ENV SCALA_HOME /usr/local/share/scala  
RUN \  
export SCALA_VER=2.11.2 && \  
export SCALA_TAR=scala-$SCALA_VER.tgz && \  
export SCALA_SHA=904e9ee3bb96e8350b1e0f2502a704f836c0cdf1 && \  
$FETCH http://downloads.typesafe.com/scala/$SCALA_VER/$SCALA_TAR $SCALA_SHA &&
\  
\  
mkdir -p $SCALA_HOME && \  
tar -xvf $SCALA_TAR \--directory $SCALA_HOME \--strip-components=1  
ENV PATH $PATH:$SCALA_HOME/bin  
  
# Ensure git can cross over corporate firewalls  
RUN git config --global url."https://".insteadOf git://  
  
# Download the Iris node and allow execution  
ENV IRIS iris-v0.3.2-linux-amd64  
RUN \  
$FETCH http://iris.karalabe.com/downloads/$IRIS
111c781c26b1df04e9366009cce773b415afe1ed && \  
chmod +x $IRIS  
  
# Download and install the Go binding  
ENV GOPATH /binds/go  
RUN go get gopkg.in/project-iris/iris-go.v1  
  
# Download and install the Erlang binding (needs some rebar hacks to gather
the dependencies)  
ENV ERL_LIBS /binds/erlang  
RUN \  
export ERLTEMP=/binds/erltmp && \  
mkdir -p $ERLTEMP && \  
cd $ERLTEMP && \  
wget https://github.com/rebar/rebar/wiki/rebar && \  
chmod +x rebar && \  
\  
echo '{deps, [{iris, ".*", {git, "https://github.com/project-iris/iris-
erl.git", {branch, "v1"}}}]}.' > rebar.config && \  
./rebar get-deps && \  
./rebar compile && \  
\  
mv ./deps $ERL_LIBS && \  
rm -rf $ERLTEMP  
  
# Download and install the Java bindings  
ENV CLASSPATH /binds/java  
RUN \  
export JAR_VER=1.0.0 && \  
mkdir -p $CLASSPATH && \  
cd $CLASSPATH && \  
\  
wget
http://repo1.maven.org/maven2/com/karalabe/iris/iris/$JAR_VER/iris-$JAR_VER.pom
&& \  
mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:copy-dependencies \  
-f $CLASSPATH/iris-$JAR_VER.pom \  
-DoutputDirectory=$CLASSPATH && \  
\  
rm -f $CLASSPATH/iris-$JAR_VER.pom && \  
mvn org.apache.maven.plugins:maven-dependency-plugin:2.8:copy \  
-Dartifact=com.karalabe.iris:iris:$JAR_VER \  
-DoutputDirectory=$CLASSPATH  
ENV CLASSPATH $CLASSPATH/*  
  
# Install and patch (multi-lang) the Go presentation tool  
ADD patches /patches  
RUN \  
go get code.google.com/p/go.tools/cmd/present && \  
cd $GOPATH/src/code.google.com/p/go.tools && \  
hg import --no-commit /patches/playground.diff && \  
go install code.google.com/p/go.tools/cmd/present && \  
\  
useradd -MU present  
  
# Copy over the demo presentations  
ADD base /present/base  
ADD binds /present/root/talks/binds  
  
# Configure the circus monitoring daemon  
ENV ORIGHOST play.iris.karalabe.com  
ENV CIRCUS_INI circus.ini  
RUN \  
echo '[circus]' > $CIRCUS_INI && \  
echo 'statsd = 1' >> $CIRCUS_INI && \  
echo >> $CIRCUS_INI && \  
echo '[watcher:iris]' >> $CIRCUS_INI && \  
echo 'cmd = $(circus.env.IRIS)' >> $CIRCUS_INI && \  
echo 'args = -dev' >> $CIRCUS_INI && \  
echo 'stdout_stream.class = FileStream' >> $CIRCUS_INI && \  
echo 'stdout_stream.filename = $(circus.env.IRIS).out.log' >> $CIRCUS_INI && \  
echo 'stderr_stream.class = FileStream' >> $CIRCUS_INI && \  
echo 'stderr_stream.filename = $(circus.env.IRIS).err.log' >> $CIRCUS_INI && \  
echo >> $CIRCUS_INI && \  
echo '[watcher:present]' >> $CIRCUS_INI && \  
echo 'cmd = $(circus.env.GOPATH)/bin/present' >> $CIRCUS_INI && \  
echo 'working_dir = /present/root' >> $CIRCUS_INI && \  
echo 'args = -base=/present/base -http=0.0.0.0:3999
-orighost=$(circus.env.ORIGHOST)' >> $CIRCUS_INI && \  
echo 'uid = present' >> $CIRCUS_INI && \  
echo 'gid = present' >> $CIRCUS_INI && \  
echo 'copy_env = True' >> $CIRCUS_INI && \  
echo 'stdout_stream.class = FileStream' >> $CIRCUS_INI && \  
echo 'stdout_stream.filename = present.out.log' >> $CIRCUS_INI && \  
echo 'stderr_stream.class = FileStream' >> $CIRCUS_INI && \  
echo 'stderr_stream.filename = present.err.log' >> $CIRCUS_INI && \  
echo >> $CIRCUS_INI && \  
echo '[env:present]' >> $CIRCUS_INI && \  
echo 'HOME=/' >> $CIRCUS_INI && \  
echo >> $CIRCUS_INI && \  
echo '[watcher:portal]' >> $CIRCUS_INI && \  
echo 'cmd = go' >> $CIRCUS_INI && \  
echo 'args = run /present/root/talks/binds/go.v1/src/portalhidden.go' >>
$CIRCUS_INI && \  
echo 'copy_env = True' >> $CIRCUS_INI && \  
echo 'stdout_stream.class = FileStream' >> $CIRCUS_INI && \  
echo 'stdout_stream.filename = portal.out.log' >> $CIRCUS_INI && \  
echo 'stderr_stream.class = FileStream' >> $CIRCUS_INI && \  
echo 'stderr_stream.filename = portal.err.log' >> $CIRCUS_INI  
  
ENTRYPOINT ["circusd", "circus.ini"]  

