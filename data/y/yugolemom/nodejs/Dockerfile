FROM centos/s2i-base-centos7  
  
MAINTAINER Hugo C. Lima <yugolemom@gmail.com>  
  
EXPOSE 8080  
  
ENV NODE_VERSION 7.5.0  
  
LABEL io.k8s.description="Nodejs - NPM" \  
io.k8s.display-name="Nodejs" \  
io.openshift.expose-services="8080:http,8888:ping" \  
io.openshift.tags="builder,nodejs" \  
com.redhat.dev-mode="DEV_MODE:false" \  
com.redhat.deployments-dir="/opt/app-root/src"  
# Install NodeJS e NPM  
RUN yum install -y \--enablerepo=centosplus tar unzip bc which lsof wget curl
\  
&& yum clean all -y \  
&& wget "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" \  
&& ln -s /usr/local/bin/node /usr/local/bin/nodejs \  
&& curl -L "https://www.npmjs.org/install.sh" | sh \  
&& npm install -g nodemon  
  
COPY .s2i/bin/ $STI_SCRIPTS_PATH  
RUN chown -R 1001:0 /opt/app-root && chmod -R ug+rwx /opt/app-root  
  
USER 1001  

