FROM aeonproject/base  
MAINTAINER 'Aeon Builds <builds+dockerfile@aeon.io>'  
# 8.77.03-r0  
ENV JAVA_VERSION_MAJOR 8  
ENV JAVA_VERSION_MINOR 77  
ENV JAVA_VERSION_BUILD 03  
ENV JAVA_VERSION_REVIS r0  
  
WORKDIR /tmp  
  
RUN echo '@edge http://nl.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories \  
&& echo '@community http://nl.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories \  
&& apk update && apk upgrade \  
&& apk add openjdk8-jre-
lib@community=${JAVA_VERSION_MAJOR}.${JAVA_VERSION_MINOR}.${JAVA_VERSION_BUILD}-${JAVA_VERSION_REVIS}
\  
&& apk add openjdk8-jre-
base@community=${JAVA_VERSION_MAJOR}.${JAVA_VERSION_MINOR}.${JAVA_VERSION_BUILD}-${JAVA_VERSION_REVIS}
\  
&& apk add
openjdk8-jre@community=${JAVA_VERSION_MAJOR}.${JAVA_VERSION_MINOR}.${JAVA_VERSION_BUILD}-${JAVA_VERSION_REVIS}
\  
&& apk add
openjdk8@community=${JAVA_VERSION_MAJOR}.${JAVA_VERSION_MINOR}.${JAVA_VERSION_BUILD}-${JAVA_VERSION_REVIS}
\  
&& rm -rf /var/cache/apk/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk  
ENV PATH ${PATH}:${JAVA_HOME}/bin  
  
WORKDIR /  
  
CMD ["java", "-version"]  

