FROM jenkins:2.7.2  
USER root  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apt-get update && apt-get install -y --no-install-recommends ca-
certificates wget && rm -rf /var/lib/apt/lists/* \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true  
#Docker inside:  
RUN set -x \  
&& apt-get update \  
&& apt-get -y install apt-transport-https ca-certificates curl lxc iptables\  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get -y install docker-engine  
  
ENV DOCKER_COMPOSE_VERSION 1.8.0  
ENV DOCKER_MACHINE_VERSION v0.7.0  
RUN set -x \  
&& curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose \  
&& chmod +x /usr/local/bin/docker-compose \  
&& curl -L https://raw.githubusercontent.com/docker/compose/$(docker-compose
version --short)/contrib/completion/bash/docker-compose >
/etc/bash_completion.d/docker-compose \  
&& curl -L
https://github.com/docker/machine/releases/download/${DOCKER_MACHINE_VERSION}/docker-
machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine \  
&& chmod +x /usr/local/bin/docker-machine \  
&& curl -L
https://raw.githubusercontent.com/docker/machine/${DOCKER_MACHINE_VERSION}/contrib/completion/bash/docker-
machine-wrapper.bash > /etc/bash_completion.d/docker-machine-wrapper \  
&& curl -L
https://raw.githubusercontent.com/docker/machine/${DOCKER_MACHINE_VERSION}/contrib/completion/bash/docker-
machine.bash > /etc/bash_completion.d/docker-machine  
  
# Build tools:  
RUN set -x \  
&& mkdir -p /tools \  
&& wget https://services.gradle.org/distributions/gradle-3.0-bin.zip -O
/tmp/gradle-3.0-bin.zip \  
&& unzip /tmp/gradle-3.0-bin.zip -d /tools/ \  
&& rm -f /tmp/gradle-3.0-bin.zip \  
&& wget https://services.gradle.org/distributions/gradle-2.14.1-bin.zip -O
/tmp/gradle-2.14.1-bin.zip \  
&& unzip /tmp/gradle-2.14.1-bin.zip -d /tools/ \  
&& rm -f /tmp/gradle-2.14.1-bin.zip  
  
#bullshit  
RUN usermod -a -G docker jenkins && groupadd -g 998 external_docker && usermod
-a -G external_docker jenkins  
  
#switch to jenkins to customize  
USER jenkins  
COPY config/hudson.plugins.gradle.Gradle.xml /usr/share/jenkins/ref/  
COPY groovies/executors.groovy
/usr/share/jenkins/ref/init.groovy.d/executors.groovy  
COPY plugins.txt /usr/share/jenkins/ref/  
  
#you can use script to get all plugins from existing installation:  
#println "Running plugin enumerator"  
#println ""  
#def plugins = jenkins.model.Jenkins.instance.getPluginManager().getPlugins()  
#plugins.sort{it.getShortName()}.each {println
"${it.getShortName()}:${it.getVersion()}"}  
#println ""  
#println "Total number of plugins: ${plugins.size()}"  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/ref/plugins.txt  
  
#switch to root to run  
USER root  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod u+x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["jenkins", "/bin/tini", "--", "/usr/local/bin/jenkins.sh"]  

