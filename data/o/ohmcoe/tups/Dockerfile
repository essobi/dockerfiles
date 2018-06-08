FROM debian:jessie  
LABEL "MAINTAINER"="Sakarin Kammanee <Sakarin@coe.phuket.psu.ac.th>"  
  
ENV TZ=Asia/Bangkok  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
STOPSIGNAL SIGINT  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends gcc g++ git make gdb \  
autoconf automake libtool \  
openjdk-7-jdk libmysql++-dev wget unzip pkg-config flex  
  
#beanstalk client  
RUN git clone \--depth=1 https://github.com/deepfryed/beanstalk-client.git
/tmp/beanstalk && \  
cd /tmp/beanstalk && \  
make install  
  
#libodb  
RUN mkdir -pv /tmp/odb && \  
cd /tmp/odb && \  
wget http://www.codesynthesis.com/download/odb/2.4/libodb-2.4.0.zip && \  
unzip libodb-2.4.0.zip && cd libodb-2.4.0 && \  
./configure && make install  
  
#libodb mysql  
RUN cd /tmp/odb && \  
wget http://www.codesynthesis.com/download/odb/2.4/libodb-mysql-2.4.0.zip && \  
unzip libodb-mysql-2.4.0.zip && \  
cd libodb-mysql-2.4.0 && \  
./configure && make install  
  
#sandbox  
RUN mkdir -pv /tmp/sandbox && \  
cd /tmp/sandbox && \  
git clone \--depth=1 https://github.com/openjudge/sandbox.git /tmp/sandbox &&
\  
cd libsandbox && \  
./configure && make install  
  
#ling Lib  
RUN cd /usr/lib && \  
ln -s /usr/local/lib/libsandbox* . && \  
ln -s /usr/local/lib/libodb* .  
  
#add source to image  
#Deplecated ADD tups /tmp/tups  
RUN mkdir -v /tmp/tups  
ADD . /tmp/tups/  
  
RUN cd /tmp/tups && \  
aclocal && \  
autoreconf --install; exit 0;  
  
#Deplecated RUN cd /tmp/tups && autoreconf --install  
RUN cd /tmp/tups && \  
./configure --prefix=/etc/tups && \  
make && make install-strip  
  
#clean  
RUN apt-get purge -y git autoconf automake libtool wget unzip && \  
apt-get autoremove -y && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/* && \  
rm -rf /var/log/apt/*.log  
  
WORKDIR /etc/tups/bin  
RUN mv /tmp/tups/start.sh /etc/tups/bin  
CMD /bin/bash start.sh  
  

