FROM oscarmartin/zmqbase  
MAINTAINER oscarmartinvicente@gmail.com  
  
# Install DEB packages where to find sbt  
RUN apt-get update && apt-get install -y apt-transport-https \  
&& echo "deb https://dl.bintray.com/sbt/debian /" | sudo tee -a
/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823  
  
# Install needed packages  
RUN apt-get update && apt-get install -y --fix-missing \  
openjdk-7-jre-headless \  
openjdk-7-jdk \  
libtool \  
pkg-config \  
build-essential \  
autoconf \  
automake \  
git \  
sbt  
  
# Install JZMQ  
RUN mkdir -p /tmp/zeromq  
WORKDIR /tmp/zeromq  
RUN git clone https://github.com/zeromq/jzmq.git \  
&& cd jzmq \  
&& ./autogen.sh \  
&& ./configure \  
&& make \  
&& sudo make install  
  
# Clean up  
RUN rm -rf /tmp/zeromq  
RUN apt-get purge -y libtool \  
pkg-config \  
build-essential \  
autoconf \  
automake  
RUN apt-get clean && apt-get autoclean && apt-get -y autoremove  
  
VOLUME /project  
WORKDIR /project  
  
# The installation process will set shared objects (libraries) in
/usr/local/lib  
ENTRYPOINT ["sbt", "-Djava.library.path=/usr/local/lib"]  

