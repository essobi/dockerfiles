FROM jenkins/jenkins:lts-alpine  
MAINTAINER Hleb Rubanau <g.rubanau@gmail.com>  
  
USER root  
  
# prebuilt compose is not compatible with alpine -- copycatting  
# https://github.com/tjamet-docker/docker-compose/blob/master/Dockerfile  
ARG compose_version=1.18.0  
RUN apk --no-cache add python py-pip git &&\  
git clone \--branch ${compose_version} https://github.com/docker/compose.git
/code/compose &&\  
cd /code/compose &&\  
pip --no-cache-dir install -r requirements.txt -r requirements-dev.txt
pyinstaller==3.1.1 &&\  
git rev-parse --short HEAD > compose/GITSHA &&\  
ln -s /lib /lib64 && ln -s /lib/libc.musl-x86_64.so.1 ldd && ln -s /lib/ld-
musl-x86_64.so.1 /lib64/ld-linux-x86-64.so.2 && \  
pyinstaller docker-compose.spec &&\  
unlink /lib/ld-linux-x86-64.so.2 /lib64 ldd ||true &&\  
mv dist/docker-compose /usr/local/bin/docker-compose-original &&\  
pip freeze | xargs pip uninstall -y &&\  
rm -rf /code /root/.cache /var/cache/apk/* &&\  
chmod +x /usr/local/bin/docker-compose-original  
  
#ENV GLIBC 2.23-r3  
#RUN apk update && apk add --no-cache openssl ca-certificates && \  
# wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
# wget https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$GLIBC/glibc-$GLIBC.apk && \  
# apk add --no-cache glibc-$GLIBC.apk && rm glibc-$GLIBC.apk && \  
# ln -s /lib/libz.so.1 /usr/glibc-compat/lib/ && \  
# ln -s /lib/libc.musl-x86_64.so.1 /usr/glibc-compat/lib  
#  
#COPY dist/docker-compose-Linux-x86_64 /usr/local/bin/docker-compose  
# get back to desired set of packages  
RUN apk add --update \  
sudo pwgen ansible py-pip terraform git jq \  
&& rm -rf /var/cache/apk/*  
  
RUN pip install awscli --upgrade  
  
# not sure what is in the alpine package -- we only need docker cli  
ARG DOCKER_CLI_VERSION=17.03.2  
RUN wget -q -O /tmp/docker.tgz \  
https://download.docker.com/linux/static/stable/$(uname
-m)/docker-${DOCKER_CLI_VERSION}-ce.tgz \  
&& cd /tmp \  
&& tar -xzf docker.tgz \  
&& cp docker/docker /usr/local/bin/docker-cli \  
&& rm -rf /tmp/docker*  
  
# hack to bypass issue with .dockercfg location, as we tend to run wrapped
docker client via sudo  
RUN touch /var/jenkins_home/.dockercfg \  
&& chown jenkins:jenkins /var/jenkins_home/.dockercfg \  
&& ln -sf /var/jenkins_home/.dockercfg /root/.dockercfg  
  
# preconfigure admin user from secrets -- thanks
https://technologyconversations.com/2017/06/16/automating-jenkins-docker-
setup/  
ENV JAVA_OPTS="-Djenkins.install.runSetupWizard=false"  
COPY security.groovy /usr/share/jenkins/ref/init.groovy.d/security.groovy  
  
# Viktor Farcic, thanks again! (see link above)  
COPY plugins.txt /usr/share/jenkins_cloudbuilder/default_plugins_list.txt  
RUN /usr/local/bin/install-plugins.sh <
/usr/share/jenkins_cloudbuilder/default_plugins_list.txt  
  
# installation and validation of public keys from major Git services  
COPY ssh_keyscan.sh /usr/local/bin  
RUN chmod a+x /usr/local/bin/ssh_keyscan.sh && /bin/bash
/usr/local/bin/ssh_keyscan.sh  
  
### TODO: https://github.com/edx/jenkins-
configuration/tree/master/src/main/groovy  
# install logging template, used in custom entrypoint  
COPY jenkins_log.properties.template
/usr/share/jenkins_cloudbuilder/jenkins_log.properties.template  
  
# now let's make it more friendly to local docker with proxied socked and
possible uids mismatch  
COPY sudoers /etc/sudoers  
COPY docker_wrapper /usr/local/bin/docker  
COPY docker_compose_wrapper /usr/local/bin/docker-compose  
  
# install custom entrypoint and make everything executable  
COPY secrets_adapter.sh /usr/local/bin/jenkins_cloudbuilder_secrets_adapter.sh  
RUN chmod 0544 /usr/local/bin/jenkins_cloudbuilder_secrets_adapter.sh  
  
COPY bootstrapper.sh /usr/share/jenkins_cloudbuilder/bootstrapper.sh  
  
COPY docker-sigkill.sh /usr/local/bin/docker-sigkill  
COPY fix_mount_permissions.sh /usr/local/bin/fix_mount_permissions.sh  
COPY entrypoint.sh /usr/local/bin/jenkins_cloudbuilder_entrypoint.sh  
COPY sudoers_injector.sh /usr/local/bin/sudoers_injector.sh  
RUN bash -c 'for util in docker docker-compose
jenkins_cloudbuilder_entrypoint.sh sudoers_injector.sh
fix_mount_permissions.sh docker-sigkill; do chown jenkins:jenkins
/usr/local/bin/$util && chmod 0554 /usr/local/bin/$util ; done'  
  
ENTRYPOINT [ "/usr/local/bin/jenkins_cloudbuilder_entrypoint.sh" ]  
  
USER jenkins  
ENV PRIVATE_REGISTRY_PORT=443  

