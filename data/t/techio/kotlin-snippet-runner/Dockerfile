FROM openjdk:8-jdk  
  
LABEL maintainer <coders@tech.io>  
  
# Install K2JVMCompiler && Kotlin runtime  
ADD docker/k2.tar.gz /opt/techio/  
RUN wget https://github.com/JetBrains/kotlin/releases/download/v1.1.50/kotlin-
compiler-1.1.50.zip -O /opt/kotlinc.zip \  
&& unzip /opt/kotlinc.zip -d /opt \  
&& rm -f /opt/kotlinc.zip \  
&& (cd /opt/techio/k2 ; find ../../kotlinc/lib -type f -exec ln -s {} \;)  
  
COPY docker/kotlin-compiler-runner.sh /opt/techio/  
  
RUN chmod ugo+x /opt/techio/kotlin-compiler-runner.sh  
  
ENTRYPOINT ["/opt/techio/kotlin-compiler-runner.sh"]  

