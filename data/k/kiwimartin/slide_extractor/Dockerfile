FROM java:openjdk-8-jdk  
  
MAINTAINER Martin Paulo "martin.paulo@gmail.com"  
ENV REFRESHED_AT 7_1_2016_1  
  
# by default the official maven Dockerfile puts the repository in a volume  
# at the moment we don't want that  
ENV MAVEN_VERSION=3.3.9 \  
MAVEN_HOME=/usr/share/maven \  
TARGETDIR=/work  
  
# setup maven  
RUN curl -fsSL
https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
# need to put the source code into the container  
COPY src src  
  
# and the pom. Wish we could combine these two copies into one :(  
COPY pom.xml pom.xml  
  
RUN mvn compile && \  
mvn exec:java -Dexec.args="-h"  
  
# given the quotes how do we get the arguments into here?  
# doing it as an environment variable sucks IMHO  
# to run, we simply need to map the target directory on the host to the work
path:  
# docker run -v /Users/martinpaulo/IdeaProjects/nectar-cloud-lessons:/work
kiwimartin/slide_extractor  
CMD mvn exec:java -Dexec.args="-d $TARGETDIR"

