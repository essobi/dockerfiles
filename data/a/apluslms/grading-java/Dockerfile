FROM apluslms/grading-base:debian-stretch  
  
ARG JAVA_URL=http://download.oracle.com/otn-
pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jdk-8u131-linux-x64.tar.gz  
ARG JAVA_DIR=/usr/local/java  
ARG JAVA_VER=jdk1.8.0_131  
  
RUN mkdir -p $JAVA_DIR && cd $JAVA_DIR \  
&& (curl -Lsb "oraclelicense=accept-securebackup-cookie" $JAVA_URL | tar zx) \  
&& update-alternatives --install "/usr/bin/java" "java"
"$JAVA_DIR/$JAVA_VER/bin/java" 1 \  
&& update-alternatives --install "/usr/bin/javac" "javac"
"$JAVA_DIR/$JAVA_VER/bin/javac" 1  
  
ADD bin /usr/local/bin  
  
RUN mkdir -p $JAVA_DIR/lib && cd $JAVA_DIR/lib \  
&& curl -LsO
http://search.maven.org/remotecontent?filepath=junit/junit/4.12/junit-4.12.jar
\  
&& curl -LsO
http://search.maven.org/remotecontent?filepath=org/hamcrest/hamcrest-
core/1.3/hamcrest-core-1.3.jar  

