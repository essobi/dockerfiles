FROM openjdk:8u151-jre  
  
ARG VERSION  
ARG DOCKERIZE_VERSION=v0.6.0  
ARG JENKINS_AGENT_VERSION=3.14  
ENV AGENT_WORKDIR=/work/agent  
COPY ./scripts/jenkins-agent.sh /opt/jenkins/jenkins-agent  
USER root  
  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
vim \  
locales \  
git \  
make \  
rake \  
build-essential \  
automake \  
autoconf \  
nasm \  
python \  
libpng-dev \  
procps \  
&& wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-alpine-linux-
amd64-$DOCKERIZE_VERSION.tar.gz \  
&& rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias
en_US.UTF-8 \  
&& rm -rf /var/lib/apt/lists/* \  
&& groupadd --gid 1000 sprout \  
&& useradd --uid 1000 --gid sprout --shell /bin/bash --create-home sprout \  
&& echo "alias l='ls -laFHh'" > /home/sprout/.bash_aliases \  
&& mkdir -p /work/app/src /work/libs /work/npm \  
&& echo "prefix = /work/npm" > /home/sprout/.npmrc \  
&& chown -R sprout:sprout /home/sprout /work \  
&& echo fs.inotify.max_user_watches=524288 > /etc/sysctl.d/increase-
watches.conf \  
&& sysctl -p \  
&& curl --create-dirs -sSLo /usr/share/jenkins/agent.jar https://repo.jenkins-
ci.org/public/org/jenkins-
ci/main/remoting/${JENKINS_AGENT_VERSION}/remoting-${JENKINS_AGENT_VERSION}.jar
\  
&& chmod 755 /usr/share/jenkins \  
&& chmod 644 /usr/share/jenkins/agent.jar \  
&& chmod 755 /opt/jenkins/jenkins-agent  
  
USER sprout  
  
RUN set -x \  
&& mkdir /home/sprout/.jenkins && mkdir -p ${AGENT_WORKDIR} \  
&& curl https://install.meteor.com/ | sh \  
&& METEOR_LOG=debug METEOR_OFFLINE_CATALOG=1 /home/sprout/.meteor/meteor
create /work/app/src --release 1.6.0.1 \  
&& rm -rf /work/app/src  
  
ENV LANG en_US.utf8  
ENV METEOR_LOG=debug  
ENV METEOR_OFFLINE_CATALOG=1  
ENV PATH /home/sprout/.meteor:/opt/jenkins/:$PATH  
WORKDIR /work/app/src  
VOLUME /home/sprout/.jenkins  
VOLUME ${AGENT_WORKDIR}  
CMD ["meteor","run"]  

