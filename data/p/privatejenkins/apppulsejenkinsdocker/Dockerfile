FROM jenkins  
# if we want to install via apt  
#COPY plugins2.txt /usr/share/jenkins/plugins2.txt  
#RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
#RUN /usr/local/bin/install-plugins.sh ant antisamy-markup-formatter antisamy-
markup-formatter build-flow-plugin buildgraph-view cloudbees-folder
credentials cvs envfile envinject external-monitor-job greenballs groovy
htmlpublisher javadoc junit ldap mailer matrix-auth matrix-project pam-auth
scm-api script-security ssh-credentials ssh-slaves translation windows-slaves
workflow-step-api workflow-scm-step credentials authentication-tokens docker-
commons icon-shim docker-build-publish token-macro jobConfigHistory ssh-agent
structs slack parameterized-trigger git git-client git-changelog git-parameter
maven-plugin subversion notification build-name-setter text-file-operations
block-queued-job jacoco cobertura  
USER root  
#Add OpenJdk repo  
RUN echo deb http://http.debian.net/debian jessie-backports main >>
/etc/apt/sources.list  
#Install 3rd party  
RUN apt-get update -qq && apt-get install -qqy \  
git-core \  
nodejs \  
npm \  
vim  
  
# software-properties-common \  
# python-software-properties \  
  
RUN apt-get install -qqy \  
net-tools \  
tofrodos \  
maven \  
rpm \  
ruby-dev \  
ruby  
  
#RUN add-apt-repository --yes ppa:openjdk-r/ppa  
  
#RUN apt-get update  
RUN apt-get install -y openjdk-7-jdk  
RUN apt-get install -y openjdk-8-jdk  
RUN ln -s /usr/bin/fromdos /usr/bin/dos2unix  
  
#install Chromium  
#RUN apt-get update && apt-get install -y xvfb chromium-browser  
  
#ADD xvfb-chromium /usr/bin/xvfb-chromium  
#RUN ln -s /usr/bin/xvfb-chromium /usr/bin/google-chrome  
#RUN ln -s /usr/bin/xvfb-chromium /usr/bin/chromium-browser  
#UI installs  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g grunt-cli@1.2.0  
RUN npm install -g bower@1.7.9  
RUN npm install -g phantomjs-prebuilt  
#RUN npm install -g phantomjs@1.9.18  
RUN gem update --system  
RUN gem install sass  
RUN gem install compass  
  
# Install android sdk  
#RUN wget http://dl.google.com/android/android-sdk_r23-linux.tgz  
#RUN tar -xvzf android-sdk_r23-linux.tgz  
#RUN mv android-sdk-linux /usr/local/android-sdk  
#RUN rm android-sdk_r23-linux.tgz  
#ENV ANDROID_HOME=/usr/local/android-sdk  
# Install Android tools  
#RUN echo y | /usr/local/android-sdk/tools/android update sdk --filter
platform,tool,platform-tool,extra,addon-google_apis-google-19,addon-
google_apis_x86-google-19,build-tools-19.1.0 \--no-ui -a  
  
#Install nodejs6  
#RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
#RUN apt-get install -qqy nodejs  
  
  
#Install docker  
#RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D  
#RUN echo deb http://apt.dockerproject.org/repo ubuntu-trusty main
>/etc/apt/sources.list.d/docker.list  
#RUN apt-get update  
#RUN apt-get install -y docker-engine  
# Install Docker from Docker Inc. repositories.  
  
#RUN curl -sSL https://get.docker.com/ | sh  
#RUN echo export http_proxy="http://web-proxy.il.hpecorp.net:8080/" >>
/etc/default/docker  
#RUN echo export https_proxy="http://web-proxy.il.hpecorp.net:8080/" >>
/etc/default/docker  
#RUN echo DOCKER_OPTS="\"--insecure-registry myd-
vm02816.hpswlabs.adapps.hp.com:5000\"" >> /etc/default/docker  
  
# Define additional metadata for our image.  
#VOLUME /var/lib/docker  
  
#RUN service docker start  
#RUN gem install compass:0.12.2  
#Edit hosts file  
#RUN cat /etc/hosts |sed 's/localhost/localhost
mydev.devdomain.com/'>/etc/hosts  
RUN cat /etc/bash.bashrc |sed "s/PS1='/PS1='Docker_/" | tee /etc/bash.bashrc  
RUN echo "cd /var/jenkins_home" >> /etc/bash.bashrc  
  
  
#Configure Jenkins  
COPY bin/ /var/jenkins_home/bin/  
COPY resources/proxy.xml /var/jenkins_home/proxy.xml  
COPY resources/config.xml /var/jenkins_home/config.xml  
COPY resources/credentials.xml /var/jenkins_home/credentials.xml  
COPY resources/hudson.tasks.Maven.xml /var/jenkins_home/hudson.tasks.Maven.xml  
COPY resources/hudson.maven.MavenModuleSet.xml
/var/jenkins_home/hudson.maven.MavenModuleSet.xml  
#COPY resources/jobs /var/jenkins_home/jobs  
#COPY resources/SUN/JDK/1.7.0_51/linux64 /var/jdk/1.7.0_51  
#COPY resources/SUN/JDK/1.8.0_51/linux64 /var/jdk/1.8.0_51  
#COPY resources/java-1.8.0-openjdk-amd64 /usr/lib/jvm/java-1.8.0-openjdk-amd64  
#COPY resources/Apache/maven/3.0.3/multi-platform /var/maven/3.0.3  
#COPY resources/plugins /var/jenkins_home/plugins  
RUN ln -s /usr/lib/jvm/java-1.8.0-openjdk-amd64
/usr/lib/jvm/java-1.8.0-openjdk  
RUN rm -rf /var/jenkins_home/credentials.xml  
#COPY bin/installDocker.sh /var/jenkins_home/bin/installDocker.sh  
#COPY bin/runNewRedis.sh /var/jenkins_home/bin/runNewRedis.sh  
#COPY bin/runNewDockerRegistry.sh
/var/jenkins_home/bin/runNewDockerRegistry.sh  
#RUN service docker restart  
#RUN /var/jenkins_home/bin/runNewRedis.sh  
#RUN chown -R jenkins:jenkins /var/jenkins_home  
  
#Install Jenkins Plugins  
#COPY plugins.txt /usr/share/jenkins/plugins.txt  
#RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
#RUN /usr/local/bin/install-plugins.sh git  
RUN install-plugins.sh ant \  
antisamy-markup-formatter \  
authentication-tokens \  
block-queued-job \  
branch-api \  
build-name-setter \  
buildgraph-view \  
cloudbees-folder \  
credentials \  
cobertura \  
cvs \  
durable-task \  
envfile \  
envinject \  
external-monitor-job \  
git \  
git-client \  
git-changelog \  
git-parameter \  
greenballs \  
groovy \  
htmlpublisher \  
jacoco \  
javadoc \  
icon-shim \  
junit \  
jobConfigHistory \  
ldap \  
mailer \  
matrix-auth \  
matrix-project \  
maven-plugin \  
notification \  
pam-auth \  
parameterized-trigger \  
pipeline-utility-steps \  
pipeline-stage-view \  
pipeline-rest-api \  
pipeline-graph-analysis \  
pipeline-input-step \  
pipeline-stage-step \  
pipeline-build-step \  
pipeline-milestone-step \  
scm-api \  
script-security \  
ssh-agent \  
ssh-credentials \  
ssh-slaves \  
structs \  
timestamper \  
translation \  
token-macro \  
text-file-operations \  
windows-slaves \  
workflow-aggregator \  
workflow-basic-steps \  
workflow-durable-task-step \  
workflow-cps-global-lib \  
workflow-cps \  
workflow-multibranch \  
workflow-support \  
workflow-api \  
workflow-job  
  
#USER jenkins  
# drop back to the regular jenkins user - good practice  
ENV http_proxy="http://web-proxy.il.hpecorp.net:8080/"  
ENV https_proxy="http://web-proxy.il.hpecorp.net:8080/"  
ENV
no_proxy="127.0.0.1,localhost,hpeswlab.net,mydyumserver,mydyumserver.hpswlabs.adapps.hp.com,*.hp.com,16.59.0.0,hpswlabs.adapps.hp.com:80"  
#ENV M2_HOME="/usr/share/maven"  
#ENV M2="/usr/share/maven"  
#ENV JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk  
RUN sed -i 's# <proxies># <proxies>\n <proxy>\n <id>HPQNETPROXY</id>\n
<active>true</active>\n <host>proxy.il.hpecorp.net</host>\n
<port>8080</port>\n <nonProxyHosts>*.devlab.ad</nonProxyHosts>\n </proxy>\n#'
/usr/share/maven/conf/settings.xml

