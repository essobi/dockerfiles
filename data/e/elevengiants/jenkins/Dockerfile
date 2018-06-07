FROM jenkins/jenkins:lts  
MAINTAINER Markus Dolic <aroha@elevengiants.com>  
  
ARG docker_version=17.06.0  
ARG docker_gid=999  
ENV JAVA_OPTS="-Xmx512m"  
ENV JENKINS_OPTS="--webroot=/var/cache/jenkins/war"  
# make sure war cache directory exists (with the right permissions)  
USER root  
RUN mkdir /var/cache/jenkins && chown -R jenkins:jenkins /var/cache/jenkins  
  
# install tools required by build/deployment jobs  
RUN apt-get update && \  
apt-get install -y --no-install-recommends rsync && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install Docker binaries and set up required permissions for the jenkins user  
RUN curl -sSL "https://download.docker.com/linux/static/stable/$(uname
-m)/docker-${docker_version}-ce.tgz" | \  
tar xz && \  
mv ./docker/* /usr/bin && \  
rmdir ./docker && \  
groupadd -g ${docker_gid} docker && \  
usermod -aG docker jenkins  
  
# copy reference config files  
# see https://hub.docker.com/_/jenkins/  
COPY ref/ /usr/share/jenkins/ref/  
RUN chown -R jenkins:jenkins /usr/share/jenkins/ref  
  
# install predefined list of plugins  
USER jenkins  
RUN /usr/local/bin/install-plugins.sh \  
blueocean \  
docker-workflow \  
git \  
github-oauth \  
matrix-auth \  
slack \  
workflow-aggregator  

