FROM tomcat:9  
LABEL maintainer="O: University of Halle (Saale) Germany; OU: ITZ, department
application systems" \  
license="Docker composition: MIT; Components: Please check"  
  
ARG BUILD_NO  
  
ENV MAXIMAPOOL=/opt/maximapool \  
TOMCAT=${CATALINA_HOME} \  
STACK_MAXIMA=/opt/maxima \  
RUN_USER=tomcat \  
RUN_GROUP=tomcat  
  
# Fetch some GPG keys we need to verify downloads  
RUN set -ex \  
&& for key in \  
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
6380DC428747F6C393FEACA59A84159D7001A4E5 \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done  
  
# 1. Update the image and install packages required  
# openjdk-8-jdk, ant --> Building the *.war  
# wget --> Downloading the maxima-sbcl packages  
# gnuplot, sbcl --> for the STACK/maxima application  
# gettext-base --> for envsubst  
#  
# 2. Install Maxima (sbcl) and remove Tomcat's host manager and examples  
#  
# 3. grab gosu for easy step-down from root and tini for signal handling  
#  
# 4. Remove package, which are no longer required  
RUN apt-get update \  
&& apt-get install -y \  
openjdk-${JAVA_VERSION%%[!0-9]*}-jdk \  
ant \  
wget \  
gnuplot \  
sbcl \  
gettext-base \  
ca-certificates \  
curl \  
&& cd ~ \  
&& wget http://downloads.sourceforge.net/project/maxima/Maxima-
Linux/5.41.0-Linux/maxima-common_5.41.0-6_all.deb \  
&& wget http://downloads.sourceforge.net/project/maxima/Maxima-
Linux/5.41.0-Linux/maxima-sbcl_5.41.0-6_amd64.deb \  
&& echo "4b7615699050abd93b65210814e59eef783466f789157422979c7c242aa4661f
maxima-common_5.41.0-6_all.deb" | sha256sum -c \  
&& echo "ebc38cb95833a630469bbad026937e6a4ac87cfb246d9100074a75d03bda1657
maxima-sbcl_5.41.0-6_amd64.deb" | sha256sum -c \  
&& dpkg -i ./maxima-sbcl_5.41.0-6_amd64.deb ./maxima-common_5.41.0-6_all.deb \  
&& rm maxima-common_5.41.0-6_all.deb maxima-sbcl_5.41.0-6_amd64.deb \  
&& cd ${CATALINA_HOME}/webapps \  
&& rm -r docs/ examples/ host-manager/ manager/ \  
&& curl -o /usr/local/bin/gosu -fSL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -fSL
"https://github.com/tianon/gosu/releases/download/1.7/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& curl -o /usr/local/bin/tini -fSL
"https://github.com/krallin/tini/releases/download/v0.9.0/tini" \  
&& curl -o /usr/local/bin/tini.asc -fSL
"https://github.com/krallin/tini/releases/download/v0.9.0/tini.asc" \  
&& gpg --verify /usr/local/bin/tini.asc \  
&& rm /usr/local/bin/tini.asc \  
&& chmod +x /usr/local/bin/tini \  
&& apt-get purge -y --auto-remove wget curl \  
&& rm -r /var/lib/apt/lists/*  
  
# Add a tomcat user  
RUN groupadd -r ${RUN_GROUP} && useradd -g ${RUN_GROUP} -d ${CATALINA_HOME} -s
/bin/bash ${RUN_USER}  
  
# Add pool source code and configuration assets  
COPY assets/init-maxima-pool.sh assets/stack_util_maximapool
assets/optimize.mac assets/servlet.conf.template assets/process.conf.template
assets/maximalocal.mac.template ${MAXIMAPOOL}/  
# Add STACK from the StackQuestion (unfortunately upstream has not separated
the repo into submodules)  
COPY assets/assStackQuestion/classes/stack/maxima ${STACK_MAXIMA}  
  
RUN VER=$(grep stackmaximaversion ${STACK_MAXIMA}/stackmaxima.mac | grep -oP
"\d+") \  
&& mv ${MAXIMAPOOL}/init-maxima-pool.sh / \  
&& chmod +x /init-maxima-pool.sh \  
&& mkdir -p ${MAXIMAPOOL}/${VER} \  
&& mv ${STACK_MAXIMA} ${MAXIMAPOOL}/${VER}/maxima \  
&& mkdir -p ${MAXIMAPOOL}/${VER}/tmp/plots/ \  
&& mkdir -p ${MAXIMAPOOL}/${VER}/tmp/logs/ \  
&& cd ${MAXIMAPOOL}/ \  
&& echo "Configuring Maxima for STACK" \  
&& VER=$VER sh -c 'envsubst < servlet.conf.template > servlet.conf \  
&& envsubst < process.conf.template > ${VER}/process.conf \  
&& envsubst < maximalocal.mac.template > ${VER}/maximalocal.mac \  
&& echo "Successfully configured Maxima for STACK ${VER}" \  
&& echo "Optimizing Maxima (There will be some warnings due to docker
container restrictions and strictness of sbcl) ..." \  
&& mv ${MAXIMAPOOL}/optimize.mac ${MAXIMAPOOL}/${VER} \  
&& cd ${MAXIMAPOOL}/${VER} \  
&& maxima -b optimize.mac \  
&& echo "Successfully optimized Maxima. Building the web application archive
(war)."' \  
&& cd ${MAXIMAPOOL} \  
&& ant \  
&& rm MaximaPool.war  
  
ENTRYPOINT ["tini", "--", "/init-maxima-pool.sh"]  
CMD ["catalina.sh", "run"]  
  

