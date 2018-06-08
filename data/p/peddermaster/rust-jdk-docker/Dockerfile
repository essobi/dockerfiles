FROM rustlang/rust:nightly  
  
RUN apt-get update -yqq && \  
apt-get install -yq openjdk-8-jdk && \  
apt-get install -yq llvm-3.9-dev libclang-3.9-dev clang-3.9 && \  
rm -rf /var/lib/apt/lists/*  
  
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/  
  
RUN cd /opt && \  
wget http://www-eu.apache.org/dist/maven/maven-3/3.5.2/binaries/apache-
maven-3.5.2-bin.tar.gz && \  
tar xzvf apache-maven-3.5.2-bin.tar.gz && \  
rm apache-maven-3.5.2-bin.tar.gz  
  
ENV PATH=/opt/apache-maven-3.5.2/bin:$PATH  

