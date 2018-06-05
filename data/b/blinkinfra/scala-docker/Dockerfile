# Pull base image  
FROM openjdk:8-jdk-alpine  
  
ARG SCALA_VERSION  
ARG SBT_VERSION  
  
ENV SCALA_VERSION ${SCALA_VERSION:-2.12.3}  
ENV SBT_VERSION ${SBT_VERSION:-1.0.2}  
  
ENV TERRAFORM_VERSION=0.10.6  
ENV
TERRAFORM_SHA256SUM=fbb4c37d91ee34aff5464df509367ab71a90272b7fab0fbd1893b367341d6e23  
  
# Install glibc (and some other pkgs)  
RUN apk --no-cache add ca-certificates wget zip jq\  
&& wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
&& wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.26-r0/glibc-2.26-r0.apk \  
&& apk add glibc-2.26-r0.apk  
  
# Install Scala  
RUN \  
echo "$SCALA_VERSION $SBT_VERSION" && \  
mkdir -p /usr/lib/jvm/java-1.8-openjdk/jre && \  
touch /usr/lib/jvm/java-1.8-openjdk/jre/release && \  
apk add --no-cache bash && \  
apk add --no-cache curl && \  
curl -fsL
http://downloads.typesafe.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz |
tar xfz - -C /usr/local && \  
ln -s /usr/local/scala-$SCALA_VERSION/bin/* /usr/local/bin/ && \  
scala -version && \  
scalac -version  
  
# Install sbt  
RUN \  
curl -fsL
https://github.com/sbt/sbt/releases/download/v$SBT_VERSION/sbt-$SBT_VERSION.tgz
| tar xfz - -C /usr/local && \  
$(mv /usr/local/sbt-launcher-packaging-$SBT_VERSION /usr/local/sbt || true) \  
ln -s /usr/local/sbt/bin/* /usr/local/bin/ && \  
sbt sbtVersion  
  
# Install aws-cli  
RUN apk --no-cache update && \  
apk --no-cache add python py-pip py-setuptools ca-certificates curl groff less
&& \  
pip --no-cache-dir install awscli && \  
rm -rf /var/cache/apk/*  
  
# Install Teraform  
RUN apk add --update git bash wget curl openssh && \  
curl
https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
> terraform_${TERRAFORM_VERSION}_linux_amd64.zip && \  
echo "${TERRAFORM_SHA256SUM} terraform_${TERRAFORM_VERSION}_linux_amd64.zip" >
terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
sha256sum -cs terraform_${TERRAFORM_VERSION}_SHA256SUMS && \  
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip -d /bin && \  
rm -f terraform_${TERRAFORM_VERSION}_linux_amd64.zip  

