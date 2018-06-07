FROM openjdk:8-jdk  
  
#ARG PROXY=http://10.0.2.2:8888  
ARG PROXY=  
  
ENV HTTP_PROXY=$PROXY  
ENV HTTPS_PROXY=$PROXY  
ENV http_proxy=$PROXY  
ENV https_proxy=$PROXY  
  
  
  
ENV TZ=America/Buenos_Aires  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN echo deb http://ftp.us.debian.org/debian testing main contrib non-free >
/etc/apt/sources.list  
RUN apt-get update && apt-get install -y sudo && apt-get install -y
git/testing && apt-get install -y dos2unix less mc nano docker-compose  
RUN apt-get install -y curl && curl -sSL https://get.docker.com/ | sh && sh -c
sleep 3; apt-get clean  
RUN echo "app ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/user && chmod 0440
/etc/sudoers.d/user  
  
RUN groupadd -r app -g 1000 && useradd -u 1000 -r -g app -m -d /app -p zzz -s
/sbin/nologin -c "Compiler user" app && chmod 755 /app  
  
RUN echo ". /app/bin/init.sh" >> /app/.bashrc  
RUN echo "alias ll='ls -alF'" >> /app/.bashrc  
RUN echo "alias cls='clear'" >> /app/.bashrc  
RUN echo "export PATH=$PATH:/app/bin:/app/gitbin" >> /app/.bashrc  
RUN echo 'export PS1="\\[\e]0;\u@\h:
\w\a\\]${debian_chroot:+($debian_chroot)}\\[\033[01;32m\\]\u@\h\\[\033[00m\\]:\\[\033[01;34m\\]\w\\[\033[00m\\]\$
"' >> /app/.bashrc  
RUN echo 'sudo chown -R app:app /var/run/docker.sock' >> /app/.bashrc  
  
RUN mkdir /app/bin && chown -R app.app /app/bin  
#RUN groupadd docker  
RUN usermod -aG docker app  
  
ARG MAVEN_VERSION=3.5.2  
ARG USER_HOME_DIR="/app"  
ARG SHA=707b1f6e390a65bde4af4cdaf2a24d45fc19a6ded00fff02e91626e3e42ceaff  
ARG BASE_URL=https://apache.osuosl.org/maven/maven-3/${MAVEN_VERSION}/binaries  
  
  
RUN mkdir -p /usr/share/maven /usr/share/maven/ref \  
&& curl -fsSL -o /tmp/apache-maven.tar.gz ${BASE_URL}/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
&& echo "${SHA} /tmp/apache-maven.tar.gz" | sha256sum -c - \  
&& tar -xzf /tmp/apache-maven.tar.gz -C /usr/share/maven --strip-components=1
\  
&& rm -f /tmp/apache-maven.tar.gz \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
ENV MAVEN_CONFIG "$USER_HOME_DIR/.m2"  
COPY mvn-entrypoint.sh /usr/local/bin/mvn-entrypoint.sh  
COPY settings-docker.xml /usr/share/maven/ref/  
COPY settings.xml /usr/share/maven/ref/  
COPY bin /app/bin  
RUN chmod +x /app/bin/* && dos2unix /app/bin/* && chown -R app.app /app/bin/*
&& for a in $(find bin | grep .sh$) ; do echo chmod +x $a; dos2unix $a ;done  
RUN chmod 777 /usr/local/bin/mvn-entrypoint.sh  
  
ARG GITLAB_USER=  
ARG GITLAB_PASSWORD=  
  
RUN git clone
https://$GITLAB_USER:$GITLAB_PASSWORD@github.com/coc1961/repobin.git
$USER_HOME_DIR/gitbin  
RUN chown -R app.app $USER_HOME_DIR/gitbin && cd $USER_HOME_DIR/gitbin && git
pull && $USER_HOME_DIR/bin/git-save-pass.sh  
#RUN cd $USER_HOME_DIR/gitbin && git remote set-url origin
https://github.com/coc1961/repobin.git  
VOLUME "$USER_HOME_DIR/.m2"  
VOLUME "$USER_HOME_DIR/bin"  
  
WORKDIR $USER_HOME_DIR  
  
RUN chown -R app $USER_HOME_DIR  
  
RUN chown app $USER_HOME_DIR  
  
USER app  
  
ENTRYPOINT ["/usr/local/bin/mvn-entrypoint.sh"]  
CMD ["/bin/bash","--login"]  

