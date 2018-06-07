# arguments : development or production for profiles  
FROM centos:latest  
MAINTAINER koseungbin <kosb1563@gmail.com>  
  
ARG profiles  
ARG projects  
  
ENV JAVA_HOME /usr/lib/jvm/java-1.8.0  
ENV PROFILES $profiles  
ENV PROJECTS $projects  
ENV BASE_SHELL_DIR_PATH /app/shellscript  
  
WORKDIR /${HOME}/  
  
EXPOSE 80  
EXPOSE 443  
EXPOSE 8080  
EXPOSE 9090  
RUN yum install -y java-1.8.0-openjdk-devel.x86_64  
RUN mkdir app  
  
COPY . ${HOME}/app  
  
RUN ls -al /app/  
RUN ls -al /app/handicraft-web/  
  
# arg : arguments for profiles  
# RUN sh ${BASE_SHELL_DIR_PATH}/core.sh ${PROFILES}  
RUN sh ${BASE_SHELL_DIR_PATH}/package.sh ${PROFILES} ${PROJECTS}  
  
# When Run Container, Execute  
# CMD /app/handicraft-web/handicraft-${PROJECTS}/target/  
ENTRYPOINT sh ${BASE_SHELL_DIR_PATH}/deploy.sh ${PROFILES} ${PROJECTS}  

