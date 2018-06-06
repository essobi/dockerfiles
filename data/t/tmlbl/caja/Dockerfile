FROM ubuntu:zesty  
  
WORKDIR /opt  
  
RUN apt-get update && apt-get install -y \  
wget \  
git \  
locales \  
openjdk-8-jdk \  
&& apt-get clean  
  
# Set the locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV ANT_VERSION 1.10.1  
RUN wget \  
http://apache.mirrors.pair.com//ant/binaries/apache-ant-$ANT_VERSION-
bin.tar.gz && \  
tar xf apache-ant-$ANT_VERSION-bin.tar.gz -C /usr/local \  
&& rm apache-ant-$ANT_VERSION-bin.tar.gz  
  
ENV ANT_HOME /usr/local/apache-ant-$ANT_VERSION  
  
ENV CAJA_VERSION 6011-es53  
  
RUN wget https://github.com/google/caja/archive/v$CAJA_VERSION.tar.gz \  
&& tar xf v$CAJA_VERSION.tar.gz \  
&& rm v$CAJA_VERSION.tar.gz  
  
WORKDIR /opt/caja-$CAJA_VERSION  
  
RUN $ANT_HOME/bin/ant  
  
EXPOSE 8887  
CMD ["./bin/runcaja", "com.google.caja.service.CajolingServiceMain"]  

