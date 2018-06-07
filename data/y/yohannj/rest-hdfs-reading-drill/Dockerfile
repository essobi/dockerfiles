FROM alpine:3.7  
  
ENV DRILL_VERSION 1.12.0  
ENV DRILL_HOME /opt/drill  
  
##################################################################  
  
# Base environment  
  
RUN set -x \  
&& apk --no-cache add \  
bash \  
curl \  
java-snappy-native \  
libc6-compat \  
openjdk8  
  
# Drill installation  
  
#If you already have drill available, uncomment the following line, and
comment wget, tar-xzf and rm -f in the next RUN command  
#ADD apache-drill-${DRILL_VERSION}.tar.gz /  
  
RUN \  
wget
https://dist.apache.org/repos/dist/release/drill/drill-${DRILL_VERSION}/apache-
drill-${DRILL_VERSION}.tar.gz && \  
tar -xzf apache-drill-${DRILL_VERSION}.tar.gz && \  
rm -f apache-drill-${DRILL_VERSION}.tar.gz && \  
mkdir opt && \  
mv apache-drill-${DRILL_VERSION} $DRILL_HOME && \  
echo 'PATH=$PATH:$DRILL_HOME/bin' >> ~/.bashrc  
  
ADD drill-override.conf $DRILL_HOME/conf/drill-override.conf  
  
# Startup Drill  
  
ADD run.sh /run.sh  
RUN chmod a+x /run.sh  
  
EXPOSE 8047 31010-31012  
  
CMD ash /run.sh  

