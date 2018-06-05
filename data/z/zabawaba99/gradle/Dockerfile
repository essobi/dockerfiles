FROM java:8-jdk  
MAINTAINER Steven Berlanga <zabawaba99@gmail.com>  
  
ENV GRADLE_VERSION 2.7  
ENV GRADLE_HASH fe801ce2166e6c5b48b3e7ba81277c41  
  
# download  
WORKDIR /usr/lib  
RUN wget
"https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip"  
RUN echo "${GRADLE_HASH} gradle-${GRADLE_VERSION}-bin.zip" >
gradle-${GRADLE_VERSION}-bin.zip.md5  
RUN md5sum -c gradle-${GRADLE_VERSION}-bin.zip.md5  
RUN rm gradle-${GRADLE_VERSION}-bin.zip.md5  
  
# install  
RUN unzip "gradle-${GRADLE_VERSION}-bin.zip"  
RUN ln -s "/usr/lib/gradle-${GRADLE_VERSION}/bin/gradle" /usr/bin/gradle  
RUN rm "gradle-${GRADLE_VERSION}-bin.zip"

