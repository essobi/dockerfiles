FROM centos:7.3.1611  
LABEL maintainer="rajesh.jonnalagadda@phenompeople.com"  
ARG APP_HOME=/opt/deployment  
RUN useradd phenom -d ${APP_HOME} -u 1000 && \  
yum install wget -y -q  
  
ARG JAVA_VERSION=8u172  
ARG JRE_DIR=jre1.8.0_172  
ARG JAVA_BUILD=b11  
  
RUN wget -q -O /tmp/jdk-linux-x64.tar.gz --no-cookies --no-check-certificate
--header "Cookie: oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/${JAVA_VERSION}-${JAVA_BUILD}/a58eab1ec242421181065cdc37240b08/jre-${JAVA_VERSION}-linux-x64.tar.gz"
&& \  
tar -xzf /tmp/jdk-linux-x64.tar.gz -C /usr/local && \  
rm -f /usr/local/${JRE_DIR}/{COPYRIGHT LICENSE README
THIRDPARTYLICENSEREADME.txt Welcome.html} && \  
ln -sf /usr/local/${JRE_DIR}/bin/java /usr/local/bin && \  
ln -sf /usr/local/${JRE_DIR} /usr/local/jre && \  
rm -rf /tmp/jdk-linux-x64.tar.gz  
ENV JAVA_HOME=/usr/local/${JRE_DIR}  
ENV LANG en_US.UTF-8  
ENV PATH=$JAVA_HOME/bin:$PATH

