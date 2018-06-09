# docker build -t sylvainleroy/byoskill-circleci:0.1 .  
# docker build -t sylvainleroy/byoskill-circleci:0.1 .  
# docker build -t us.gcr.io/byoskill-178715/circleci:0.1  
FROM docker:17.05.0-ce-git  
MAINTAINER sleroy <sleroy0@gmail.com>  
  
# GKE build & testing environment for Circle CI 2.0  
USER root  
ENV NODEJS_VERSION v8  
ENV DOCKER_VERSION 17.05.0-ce  
  
RUN mkdir /work  
WORKDIR /work  
  
RUN apk add --update --no-cache \  
vim \  
curl ca-certificates \  
git \  
openjdk8 \  
git \  
zip \  
curl \  
perl \  
coreutils \  
bash \  
wget \  
unzip \  
python  
  
# Download Gradle  
RUN wget https://services.gradle.org/distributions/gradle-2.4-bin.zip -O
gradle-2.4-bin.zip  
RUN unzip gradle-2.4-bin.zip  
  
# Download GCloud  
RUN wget -O google-cloud-sdk.tar.gz
https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-
sdk-158.0.0-linux-x86_64.tar.gz && \  
tar -zxvf google-cloud-sdk.tar.gz && \  
rm google-cloud-sdk.tar.gz && \  
./google-cloud-sdk/install.sh --quiet  
  
ENV PATH=/work/google-cloud-
sdk/bin:/root/.nodebrew/current/bin:$GRADLE_HOME/bin:$PATH  
RUN gcloud components update --quiet  
RUN gcloud --quiet components install docker-credential-gcr kubectl  
  
# Downlod node.js  
RUN apk add --update nodejs  
  
# Env variables  
ENV GRADLE_HOME=/work/gradle-2.4  
# setup PATH  
# setup openjdk environment  
ENV JAVA_HOME /usr/lib/jvm/java-1.8-openjdk/jre  
ENV PATH /work/google-cloud-
sdk/bin:/root/.nodebrew/current/bin:$GRADLE_HOME/bin:$PATH  
ENV PATH
$PATH:/usr/lib/jvm/java-1.8-openjdk/jre/bin:/usr/lib/jvm/java-1.8-openjdk/bin  
#RUN echo "export PATH=/work/google-cloud-
sdk/bin:/root/.nodebrew/current/bin:$GRADLE_HOME/bin:$PATH" >> /root/.bashrc  
RUN java -version  
RUN gradle -v  
RUN node -v  
RUN gcloud -v  

