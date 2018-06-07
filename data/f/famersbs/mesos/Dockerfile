FROM famersbs/delauncher_base  
MAINTAINER Sean <famersbs@gmail.com>  
  
# install oracle java  
RUN apt-get -y update  
  
# Install the latest OpenJDK.  
RUN apt-get install -y openjdk-7-jdk  
  
# Install autotools (Only necessary if building from git repository).  
RUN apt-get install -y autoconf libtool  
  
# Install other Mesos dependencies.  
RUN apt-get -y install build-essential python-dev python-boto libcurl4-nss-dev
libsasl2-dev maven libapr1-dev libsvn-dev  
  
RUN apt-get -y install wget  
  
# download mesos  
WORKDIR /opt  
  
RUN wget http://www.apache.org/dist/mesos/0.25.0/mesos-0.25.0.tar.gz  
RUN tar -zxf /opt/mesos-0.25.0.tar.gz  
RUN mv ./mesos-0.25.0 ./mesos  
  
RUN mkdir ./mesos/build  
  
WORKDIR /opt/mesos/build  
  
RUN ../configure  
RUN make  
  
# copy run script  
WORKDIR /  
ADD run.sh run.sh  

