FROM maven:3-jdk-8-alpine  
# ##########################################################  
#  
# DISCLAIMER  
#  
# #### usage ######################################################  
#  
# --- Building this docker image  
# docker build -t asqa.mvn:jdk8.alpine .  
# docker build -t asqa.mvn:jdk8.alpine --build-arg GIT_BRANCH=develop .  
# docker build -t asqa.mvn:jdk8.alpine --build-arg GIT_BRANCH=v4.0.3 .  
#  
# --- Compiling Asqatasun with this docker image  
# docker run -it --rm -v "$PWD":/usr/src/ -w /usr/src/ asqa.mvn:jdk8.alpine
mvn clean install  
# docker run -it --rm -v "$PWD":/usr/src/ -w /usr/src/ asqa.mvn:jdk8.alpine
mvn clean  
#  
# --- Playing with this docker image  
# docker run -it --rm asqa.mvn:jdk8.alpine /bin/bash  
# docker run -it --rm asqa.mvn:jdk8.alpine javac -version  
# docker run -it --rm asqa.mvn:jdk8.alpine java -version  
# docker run -it --rm asqa.mvn:jdk8.alpine mvn -version  
#  
#  
# #### source code ###############################################  
# https://github.com/Asqatasun/Asqatasun/archive/master.zip  
# could be overridden with \--build-arg GIT_BRANCH=<branch_name>  
# could be overridden with \--build-arg GIT_BRANCH=<tag_name>  
#  
# #### FROM ######################################################  
# maven:3-jdk-8-alpine https://github.com/carlossg/docker-
maven/blob/alpine/jdk-8/Dockerfile  
# |-- openjdk:8-jdk-alpine https://github.com/docker-
library/openjdk/blob/master/8-jdk/alpine/Dockerfile  
# |-- alpine:3.4 https://github.com/gliderlabs/docker-
alpine/blob/master/versions/library-3.4/Dockerfile  
###################################################################  
  
# build variables  
ARG GIT_BRANCH=master  
ARG SRC_URL_PREFIX=https://github.com/Asqatasun/Asqatasun/archive  
ARG SRC_URL="${SRC_URL_PREFIX}/${GIT_BRANCH}.zip"  
  
# build  
RUN cd /tmp/ && \  
apk add --no-cache openssl && \  
wget ${SRC_URL} && unzip *.zip && \  
rm *.zip && mv Asqa* src && \  
cd src && mvn clean install && \  
cp -r /root/.m2 /root/.m2_backup && \  
rm -rf /tmp/src /root/.m2/* && \  
rm -rf /root/.m2_backup/repository/org/asqa* && \  
FIND='exec "$@"' && \  
ADD='mv -f \/root\/.m2_backup\/repository \/root\/.m2\/;' && \  
FILE=/usr/local/bin/mvn-entrypoint.sh && \  
sed -i "s/${FIND}/${ADD}\n${FIND}/g" $FILE && \  
echo "--------------------------------------------------" && \  
echo "-----> backup maven plugins : OK" && \  
echo "-----> clean : OK" && \  
echo "-----> configuration" && cd /root/ && \  
mvn -version && echo "----------------------------" && \  
javac -version && echo "----------------------------" && \  
java -version && echo "----------------------------" && \  
echo ${SRC_URL} && echo "----------------------------"  
  
  
# environment variables  
ENV SRC_PRELOAD=${SRC_URL}  
  
  
  

