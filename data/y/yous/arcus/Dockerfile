FROM centos:centos6  
MAINTAINER Chayoung You <yousbe@gmail.com>  
  
RUN touch /var/lib/rpm/* \  
&& yum install -y \  
gcc gcc-c++ autoconf automake libtool pkgconfig cppunit-devel python-
setuptools python-devel \  
java-1.7.0-openjdk-devel \  
git subversion wget curl nc \  
&& yum clean all  
  
RUN useradd arcus  
RUN git clone https://github.com/naver/arcus.git /arcus  
RUN chown -R arcus:arcus /arcus  
  
USER arcus  
  
WORKDIR /home/arcus  
RUN mkdir vendor  
  
WORKDIR /home/arcus/vendor  
RUN curl -OL http://archive.apache.org/dist/ant/binaries/apache-
ant-1.9.3-bin.tar.gz  
RUN tar xf apache-ant-1.9.3-bin.tar.gz  
RUN ln -s apache-ant-1.9.3 ant  
RUN rm apache-ant-1.9.3-bin.tar.gz  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.7.0-openjdk.x86_64  
ENV ANT_HOME /home/arcus/vendor/ant  
ENV PATH $JAVA_HOME/bin:$ANT_HOME/bin:$PATH  
  
WORKDIR /arcus/scripts  
RUN ./build.sh  
  
WORKDIR /arcus  
VOLUME ["/arcus"]  

