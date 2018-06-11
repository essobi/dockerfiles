FROM centos:7  
ARG remoting_version=2.9  
ARG jenkins_dir=/usr/local/jenkins  
ARG jenkins_user=jenkins  
ARG jenkins_uid=219  
ARG jenkins_group=jenkins  
ARG jenkins_gid=497  
ENV JENKINS_HOME ${jenkins_dir}  
  
RUN /sbin/groupadd -g ${jenkins_gid} ${jenkins_group}  
RUN /sbin/useradd -c "Jenkins user" -d ${jenkins_dir} -g ${jenkins_gid} -m
jenkins  
  
RUN yum install --noplugins -y java-1.8.0-openjdk-devel git; yum clean all  
  
RUN curl --create-dirs -sSLo ${jenkins_dir}/remoting.jar \  
http://repo.jenkins-ci.org/public/org/jenkins-
ci/main/remoting/${remoting_version}/remoting-${remoting_version}.jar \  
&& chmod 644 ${jenkins_dir}/remoting.jar  
  
COPY jenkins-worker /usr/local/bin/jenkins-worker  
  
VOLUME ${jenkins_dir}  
USER ${jenkins_user}  

