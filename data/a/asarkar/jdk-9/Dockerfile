FROM asarkar/alpine-plus  
  
ENV JAVA_HOME=/opt/java JSHELLEDITOR=vim PATH=$PATH:$JAVA_HOME/bin  
  
WORKDIR /opt  
  
RUN apk update && apk upgrade && \  
curl -sSL -b "oraclelicense=a"
http://download.java.net/java/jdk9-alpine/archive/179/binaries/jdk-9-ea+179_linux-x64-musl_bin.tar.gz
| tar xz && \  
find . -maxdepth 1 -type d -name "*jdk*" -exec ln -sf {} $JAVA_HOME \;  
  
CMD ["/bin/bash"]  

