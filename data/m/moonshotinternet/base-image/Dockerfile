FROM node:9.2.0-alpine  
  
LABEL vendor=Moonshot-Internet  
LABEL com.moonshot.name=base-image  
LABEL com.moonshot.version=1.0.0  
  
RUN \  
apk update \  
&& apk add ca-certificates wget \  
&& update-ca-certificates \  
&& cd /usr \  
&& mkdir java \  
&& cd /usr/java/ \  
&& wget -c --header "Cookie: oraclelicense=accept-securebackup-cookie"
http://download.oracle.com/otn-
pub/java/jdk/10.0.1+10/fb4372174a714e6b8c52526dc134031e/jdk-10.0.1_linux-x64_bin.tar.gz
\  
&& tar -xvzf jdk-10.0.1_linux-x64_bin.tar.gz \  
&& rm -rf jdk-10.0.1_linux-x64_bin.tar.gz  
  
ENV JAVA_HOME /usr/java/jdk-10.0.1  
ENV PATH=$JAVA_HOME/bin:$PATH  
  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
\  
apk add --no-cache --virtual .gosu-deps \  
dpkg \  
gnupg \  
openssl \  
; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
# gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
# gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true; \  
\  
apk del .gosu-deps  
  
ARG ANSIBLE_VERSION=2.4.2.0  
ENV SONAR_VERSION=7.0 \  
SONARQUBE_HOME=/opt/sonarqube \  
SONARQUBE_JDBC_USERNAME=sonar \  
SONARQUBE_JDBC_PASSWORD=sonar \  
SONARQUBE_JDBC_URL=' '  
RUN apk --no-cache add python py-pip openssl ca-certificates \  
&& apk --update add --virtual build-dependencies \  
python py-pip openssl ca-certificates python-dev libffi-dev openssl-dev build-
base \  
&& pip install --upgrade pip cffi \  
&& pip install ansible \  
&& apk del build-dependencies  
  
# RUN apk del python py-pip openssl ca-certificates  
RUN ln -sf /usr/bin/python3 /usr/bin/python \  
&& ln -sf /usr/bin/pip3 /usr/bin/pip \  
&& rm -r /root/.cache  
  
# install tools  
RUN apk --no-cache add \  
python3 \  
git \  
curl \  
jq \  
rsync \  
openssh \  
gnupg unzip \  
libressl wget \  
su-exec \  
bash  
  
RUN pip install \  
awscli \  
boto3 \  
botocore  
  
# do some tweaks  
RUN mkdir /etc/ansible/ /ansible \  
&& echo "[local]" >> /etc/ansible/hosts \  
&& echo "localhost ansible_connection=local" >> /etc/ansible/hosts \  
&& echo "[defaults]" >> /etc/ansible/ansible.cfg \  
&& echo "retry_files_save_path = \"/tmp\"" >> /etc/ansible/ansible.cfg \  
&& rm -rf /root/.cache  
  
RUN python --version \  
&& pip --version \  
&& ansible --version  
  
EXPOSE 9000  
RUN addgroup -S sonarqube && adduser -S -G sonarqube sonarqube  
  
# get sonarqube  
RUN set -x \  
# pub 2048R/D26468DE 2015-05-25  
# Key fingerprint = F118 2E81 C792 9289 21DB CAB4 CFCA 4A29 D264 68DE  
# uid sonarsource_deployer (Sonarsource Deployer) <infra@sonarsource.com>  
# sub 2048R/06855C1D 2015-05-25  
# && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
F1182E81C792928921DBCAB4CFCA4A29D26468DE \  
&& cd /opt \  
&& wget -O sonarqube.zip --no-verbose
https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONAR_VERSION.zip
\  
&& wget -O sonarqube.zip.asc --no-verbose
https://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONAR_VERSION.zip.asc
\  
# && gpg --batch --verify sonarqube.zip.asc sonarqube.zip \  
&& unzip sonarqube.zip \  
&& mv sonarqube-$SONAR_VERSION sonarqube \  
&& chown -R sonarqube:sonarqube sonarqube \  
&& rm sonarqube.zip* \  
&& rm -rf $SONARQUBE_HOME/bin/*  
  
  
# get sonar scanner  
RUN set -x \  
&& cd /opt \  
&& wget -O sonarscanner.zip sonarsource.bintray.com/Distribution/sonar-
scanner-cli/sonar-scanner-cli-3.1.0.1141.zip \  
&& wget -O sonarscanner.zip.asc --no-verbose
https://sonarsource.bintray.com/Distribution/sonar-scanner-cli/sonar-scanner-
cli-3.1.0.1141.zip.asc \  
&& unzip sonarscanner.zip \  
&& rm sonarscanner.zip  
  
VOLUME "$SONARQUBE_HOME/data"  
  
WORKDIR $SONARQUBE_HOME  
COPY run.sh $SONARQUBE_HOME/bin/  
# ENTRYPOINT ["./bin/run.sh"]  
ENV SONAR_RUNNER_HOME=/root/sonar-scanner-cli-3.1.0.1141  
ENV PATH $PATH:/root/sonar-scanner-cli-3.1.0.1141/bin  
  
COPY sonar-runner.properties ./sonar-scanner-cli-3.1.0.1141/conf/sonar-
runner.properties

