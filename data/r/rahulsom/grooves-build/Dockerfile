FROM quay.io/travisci/travis-jvm  
  
USER travis  
  
WORKDIR /home/travis  
  
RUN curl
https://raw.githubusercontent.com/michaelklishin/jdk_switcher/master/jdk_switcher.sh
> jdk_switcher.sh  
RUN git clone \--depth=50 --branch=kotlin
https://github.com/rahulsom/grooves.git  
  
COPY build.sh /home/travis  
RUN ./build.sh  

