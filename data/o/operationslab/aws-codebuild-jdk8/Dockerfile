FROM openjdk:8  
  
WORKDIR /app  
  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
  
RUN apt-get update \  
&& apt-get install -y apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common \  
git  
  
RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu xenial stable"  
  
RUN apt-get update \  
&& apt-cache policy docker-ce \  
&& apt-get install -y docker-ce  
  
RUN wget "https://bootstrap.pypa.io/get-pip.py" -O /tmp/get-pip.py \  
&& python /tmp/get-pip.py \  
&& pip install awscli==1.11.25 \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
ENV MAVEN_VERSION=3.3.3 \  
MAVEN_HOME="/usr/share/maven" \  
MAVEN_CONFIG="/root/.m2" \  
GRADLE_VERSION=4.3.1  
  
RUN apt-get update \  
&& apt-get -y install python-setuptools \  
&& apt-get clean \  
&& mkdir -p /usr/share/maven /usr/share/maven/ref $MAVEN_CONFIG \  
&& curl -fsSL
"https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" \  
| tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
&& mkdir -p /usr/src/gradle \  
&& wget "https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-
bin.zip" -O /usr/src/gradle/gradle-$GRADLE_VERSION-bin.zip \  
&& unzip /usr/src/gradle/gradle-$GRADLE_VERSION-bin.zip -d /usr/local \  
&& ln -s /usr/local/gradle-$GRADLE_VERSION/bin/gradle /usr/bin/gradle \  
&& rm -rf /usr/src/gradle \  
&& rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*  

