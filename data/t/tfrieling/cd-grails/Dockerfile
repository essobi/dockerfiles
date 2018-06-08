FROM java:8  
LABEL maintainer="thomas.frieling@gmail.com"  
  
# Set Berlin timezone  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
# Set customizable env vars defaults.  
# Set Grails version (default: 3.2.8; min: 3.0.0; max: 3.2.8).  
ENV GRAILS_VERSION 3.3.5  
# Set Gradle user home to share caching  
ENV GRADLE_USER_HOME=/gradle  
  
# Install Grails  
WORKDIR /usr/lib/jvm  
RUN wget https://github.com/grails/grails-
core/releases/download/v$GRAILS_VERSION/grails-$GRAILS_VERSION.zip && \  
unzip grails-$GRAILS_VERSION.zip && \  
rm -rf grails-$GRAILS_VERSION.zip && \  
ln -s grails-$GRAILS_VERSION grails  
  
# Setup Grails path.  
ENV GRAILS_HOME /usr/lib/jvm/grails  
ENV PATH $GRAILS_HOME/bin:$PATH  
  
# Install python  
RUN apt-get update  
RUN apt-get install -y python-dev  
RUN curl -O https://bootstrap.pypa.io/get-pip.py  
RUN python get-pip.py  
  
# run grails once to fill the gradle cache  
WORKDIR /gradle  
WORKDIR /grails-apps  
RUN echo $GRADLE_USER_HOME  
RUN grails create-app helloworld  
RUN ls -lh /gradle  
WORKDIR helloworld  
RUN grails clean  
  
# select workdir  
WORKDIR /build  
  

