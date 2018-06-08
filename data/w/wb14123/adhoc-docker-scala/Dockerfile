FROM debian:7  
# install jdk1.8  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" |
tee -a /etc/apt/sources.list.d/webupd8team-java.list && \  
echo "deb http://repo.mongodb.org/apt/debian wheezy/mongodb-org/3.2 main" |
tee /etc/apt/sources.list.d/mongodb-org-3.2.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 &&
\  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 99E82A75642AC823 && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927 && \  
apt-get install -f && apt-get clean && rm -rf /var/lib/apt/lists/* && \  
apt-get update -y && apt-get install -y wget && \  
echo "deb http://packages.dotdeb.org wheezy all" | tee -a
/etc/apt/sources.list.d/dotdeb.list && \  
echo "deb-src http://packages.dotdeb.org wheezy all" | tee -a
/etc/apt/sources.list.d/dotdeb.list && \  
wget http://www.dotdeb.org/dotdeb.gpg && \  
apt-key add dotdeb.gpg && \  
apt-get update -y && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
apt-get install -y --force-yes oracle-java8-installer oracle-java8-set-default
mongodb-org redis-server redis-tools unzip wget procps  
  
# install sbt  
RUN wget -c 'http://repo1.maven.org/maven2/org/scala-sbt/sbt-
launch/1.0.0-M4/sbt-launch.jar' && \  
mv sbt-launch.jar /var && \  
echo '#!/bin/bash' > /usr/bin/sbt && \  
echo 'java -Xms512M -Xmx1536M -Xss1M -XX:+CMSClassUnloadingEnabled
-XX:MaxPermSize=256M -jar /var/sbt-launch.jar "$@"' >> /usr/bin/sbt && \  
chmod u+x /usr/bin/sbt  
  
# install jprofiler  
RUN wget -c http://download-keycdn.ej-
technologies.com/jprofiler/jprofiler_linux_9_2.sh && bash
jprofiler_linux_9_2.sh -q  
  
RUN echo "Asia/Harbin" > /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
ONBUILD COPY ./project /data/project  
ONBUILD COPY ./build.sbt /data/build.sbt  
ONBUILD COPY ./script/sbt-repositories /root/.sbt/repositories  
ONBUILD RUN cd /data && sbt update -Dsbt.override.build.repos=true  
ONBUILD COPY . /data  
  
# build and test  
ONBUILD RUN service mongod restart && service redis-server restart \ && cd
/data \  
&& sbt -Dsbt.override.build.repos=true -Dfile.encoding=UTF-8 test \  
&& sbt -Dsbt.override.build.repos=true -Dfile.encoding=UTF-8 dist \  
&& cd /data/target/universal/ && unzip *.zip  
  
# run cron and project  
ONBUILD RUN cd /data && export proj_name=`sbt settings name | tail -1 | cut
-d' ' -f2 |tr -dc [:print:] | sed 's/\\[0m//g'` && \  
mkdir -p /release/${proj_name} && mv /data/target/universal/${proj_name}*
/release && \  
cd /release/${proj_name}*/bin && \  
ln -s `pwd`/$proj_name /entrypoint  
  
# cleanup  
ONBUILD RUN rm -r /data  
  
ONBUILD CMD ["/entrypoint", "-Dconfig.resource=prod.conf",
"-Dfile.encoding=UTF8"]  

