FROM centos:7.3.1611  
LABEL maintainer="rajesh.jonnalagadda@phenompeople.com"  
ARG APP_HOME=/opt/deployment  
RUN useradd phenom -d ${APP_HOME} -u 1000 && \  
yum install wget -y -q  
  
ARG JAVA_VERSION=8u144  
ARG JAVA_DIR=jdk1.8.0_144  
ARG JAVA_BUILD=b01  
  
RUN wget -q -O /tmp/jdk-linux-x64.tar.gz --no-cookies --no-check-certificate
--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}-${JAVA_BUILD}/090f390dda5b47b9b721c7dfaa008135/jdk-${JAVA_VERSION}-linux-x64.tar.gz"
&& \  
tar -xzf /tmp/jdk-linux-x64.tar.gz -C /usr/local && \  
rm -f /usr/local/${JAVA_DIR}/jdk/{COPYRIGHT LICENSE README
THIRDPARTYLICENSEREADME.txt Welcome.html} && \  
ln -s /usr/local/${JAVA_DIR}/bin/java /usr/local/bin && \  
ln -sf /usr/local/${JAVA_DIR} /usr/local/jdk && \  
rm -rf /tmp/jdk-linux-x64.tar.gz  
ENV JAVA_HOME=/usr/local/${JAVA_DIR}  
ENV PATH=$JAVA_HOME/bin:$PATH  

