FROM sameersbn/gitlab-ci-multi-runner:1.1.4-7  
MAINTAINER Peter Reisz <peter@reisz.tk>  
  
ENV GITLAB_CI_MULTI_RUNNER_VERSION=9.3.0 \  
JAVA_HOME="/opt/java" \  
JAVA_VERSION="8u131" \  
JAVA_BUILD="b11" \  
JAVA_VERSION_HASH="d54c1d3a095b4ff2b6607d096fa80163" \  
NODE_HOME="/opt/node" \  
NODE_VERSION="6.11.0"  
ENV PATH="$PATH:$JAVA_HOME/bin:$NODE_HOME/bin"  
RUN buildDeps='xz-utils'; \  
set -x && \  
apt-get update && apt-get upgrade -y && apt-get install -y sshpass $buildDeps
\--no-install-recommends  
  
RUN wget -O /usr/local/bin/gitlab-ci-multi-runner https://gitlab-ci-multi-
runner-
downloads.s3.amazonaws.com/v${GITLAB_CI_MULTI_RUNNER_VERSION}/binaries/gitlab-
ci-multi-runner-linux-amd64  
RUN chmod 0755 /usr/local/bin/gitlab-ci-multi-runner  
  
# java  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-
pub/java/jdk/$JAVA_VERSION-$JAVA_BUILD/$JAVA_VERSION_HASH/jdk-$JAVA_VERSION-
linux-x64.tar.gz" -O /tmp/java.tar.gz  
RUN tar -zxvf /tmp/java.tar.gz -C /opt  
RUN mv /opt/jdk* $JAVA_HOME  
  
# node  
RUN wget "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" -O /tmp/node.tar.xz  
RUN tar xf /tmp/node.tar.xz -C /opt  
RUN mv /opt/node-* $NODE_HOME  
RUN npm install yarn -g  
RUN cd $(npm root -g)/npm && npm install fs-extra && sed -i -e s/graceful-
fs/fs-extra/ -e s/fs.rename/fs.move/ ./lib/utils/rename.js  
  
# clean up  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN apt-get purge -y --auto-remove $buildDeps  
RUN apt-get autoremove -y && apt-get clean  

