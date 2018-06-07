FROM java:openjdk-8-jre  
  
RUN apt-get -qq update  
RUN apt-get install -y curl git  
  
# Gerrit config  
ENV GERRIT_HOME=/var/gerrit  
ENV GERRIT_USER=gerrit \  
GERRIT_WAR=${GERRIT_HOME}/gerrit.war \  
GERRIT_SITE=${GERRIT_HOME}/review_site \  
GERRIT_VERSION=2.13.5  
RUN groupadd -r ${GERRIT_USER} \--gid=1000 \  
&& useradd -r -m -g ${GERRIT_USER} -d ${GERRIT_HOME} \--uid=1000
${GERRIT_USER}  
  
RUN mkdir -p ${GERRIT_HOME}/plugins \  
${GERRIT_SITE}/plugins \  
${GERRIT_SITE}/etc  
  
# Install Gerrit plugins  
ADD jar/download-commands.jar ${GERRIT_HOME}/plugins  
  
RUN cd ${GERRIT_HOME}/plugins \  
&& wget -q https://gerrit-ci.gerritforge.com/job/plugin-serviceuser-bazel-
master/lastSuccessfulBuild/artifact/bazel-
genfiles/plugins/serviceuser/serviceuser.jar \  
&& wget -q https://gerrit-ci.gerritforge.com/job/plugin-delete-project-
stable-2.13/lastSuccessfulBuild/artifact/buck-out/gen/plugins/delete-
project/delete-project.jar \  
&& wget -q https://gerrit-ci.gerritforge.com/job/plugin-project-download-
commands-stable-2.13/lastSuccessfulBuild/artifact/buck-
out/gen/plugins/project-download-commands/project-download-commands.jar \  
&& wget -q https://github.com/davido/gerrit-oauth-
provider/releases/download/v2.13.2/gerrit-oauth-provider.jar \  
&& wget -q https://github.com/tomaswolf/gerrit-gitblit-
plugin/releases/download/v2.13.171.2/gitblit-plugin-2.13.171.2.jar  
  
# Install Gerrit  
WORKDIR ${GERRIT_HOME}  
RUN wget -q https://gerrit-
releases.storage.googleapis.com/gerrit-${GERRIT_VERSION}.war -O ${GERRIT_WAR}  
  
COPY bin/gerrit-start.sh /usr/local/bin/gerrit-start.sh  
  
# Install Kaigara  
RUN curl -sL https://kaigara.org/get | sh  
COPY operations /opt/kaigara/operations  
COPY resources /etc/kaigara/resources  
  
RUN chown -R ${GERRIT_USER}:${GERRIT_USER} ${GERRIT_HOME}  
  
USER ${GERRIT_USER}  
  
# Add Theme files  
ADD theme/GerritSite.css ${GERRIT_HOME}  
ADD theme/GerritSiteFooter.html ${GERRIT_HOME}  
ADD theme/logo.png ${GERRIT_HOME}  
  
EXPOSE 8080 29418  
ENTRYPOINT ["kaigara"]  
  
CMD ["start", "gerrit-start.sh"]  

