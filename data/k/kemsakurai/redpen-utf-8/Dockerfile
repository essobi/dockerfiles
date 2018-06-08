# Java 1.8 & RedPen Dockerfile  
# https://github.com/kemsakurai/docker-redpen-UTF-8  
# Pull base image.  
FROM ubuntu:14.04  
# maintainer details  
MAINTAINER Ken Sakurai "sakurai.kem@gmail.com"  
# Set locale  
RUN locale-gen ja_JP.UTF-8  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:ja  
ENV LC_ALL ja_JP.UTF-8  
# Accecpt Oracle license before installing java  
RUN echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-
set-selections  
RUN echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections  
  
# Install java  
RUN apt-get update  
RUN apt-get -y install software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get -y install oracle-java8-installer oracle-java8-set-default  
RUN echo "export JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment  
  
# DownLoad Redpen  
WORKDIR /tmp  
RUN wget -q https://github.com/redpen-
cc/redpen/releases/download/redpen-1.7.0/redpen-1.7.0.tar.gz -O - | tar xz &&
\  
cp -av redpen-distribution-1.7.0/* /usr/local/ && \  
rm -rf redpen-distribution-1.7.0  
  
RUN export PATH=$PATH:/usr/local/bin  
WORKDIR /data  
  
CMD ["/usr/local/bin/redpen"]  

