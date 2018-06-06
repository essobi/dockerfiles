FROM openjdk:6-jdk  
  
ARG MAVEN_VERSION=2.2.1  
ARG USER_HOME_DIR="/root"  
ARG SHA=b9a36559486a862abfc7fb2064fd1429f20333caae95ac51215d06d72c02d376  
ARG
BASE_URL=https://archive.apache.org/dist/maven/maven-2/$MAVEN_VERSION/binaries  
  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-
maven-${MAVEN_VERSION}-bin.tar.gz \  
&& echo "${SHA} /tmp/apache-maven.tar.gz" | sha256sum -c - \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"  
COPY mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh  
COPY settings-docker.xml /usr/share/maven/ref/  
  
VOLUME "$USER_HOME_DIR/.m2"  
  
ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]  
CMD ["mvn"]  
  
#  
# Build and run:  
#  
# docker build -t trade4chor/maven:2.2.1-jdk6 .  
#  
# docker run -it --rm --name mvn2 -w=/data -v [absolute-path-to-the-source-
root-directory]:/data trade4chor/maven:2.2.1-jdk6 [MAVEN COMMAND, e.g., 'mvn
clean install']  
#  
# In order to share a directory on a Windows host with a container, the
directory has to be added to the list of shared drives in the Docker settings.  
#  
#  
# Reusing the Maven local repository [https://github.com/carlossg/docker-
maven/blob/master/README.md]  
#  
# The local Maven repository can be reused across containers by creating a
volume and mounting it in /root/.m2.  
#  
# docker volume create --name maven-repo  
# docker run -it --rm --name mvn2 -w=/data -v ode-maven-repo:/root/.m2 -v
path/to/sources:/data trade4chor/maven:2.2.1-jdk6 mvn clean install
-DskipTests=true  
#  
# or if the libraries are also required on the dev machine, a local folder of
the host can be specified  
# docker run -it --rm --name mvn2 -w=/data -v path/to/local-repo/.m2:/root/.m2
-v path/to/sources:/data trade4chor/maven:2.2.1-jdk6 mvn clean install
-DskipTests=true  
#  
# Based on that, later runs are reusing downloaded artifacts in the volume  
#  

