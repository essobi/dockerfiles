FROM opensuse:tumbleweed  
MAINTAINER Alex Geer <monoflash@gmail.com>  
  
RUN zypper --non-interactive --gpg-auto-import-keys ref && \  
zypper --non-interactive --quiet dup && \  
zypper --non-interactive --quiet in tar curl net-tools ca-certificates git
mercurial subversion && \  
update-ca-certificates  
  
## Minimal set of tools for compiling and linking applications and Tools and
libraries for software development using C/C++ and other  
RUN zypper --non-interactive --quiet in patterns-devel-base-devel_basis
patterns-devel-C-C++-devel_C_C++  
  
## Setup the locale  
RUN zypper --non-interactive --quiet in bundle-lang-common-ru bundle-lang-
common-en glibc-i18ndata glibc-locale  
ENV LANG ru_RU.UTF-8  
ENV LC_ALL $LANG  
RUN localedef --charmap=UTF-8 --inputfile=ru_RU $LANG  
  
## Clean  
RUN zypper --non-interactive clean --all  
  
RUN curl --insecure --silent
https://nodejs.org/dist/v10.1.0/node-v10.1.0-linux-x64.tar.xz | xz -d | tar x
-C /usr/local  
RUN ln -s --directory -v /usr/local/node-v10.1.0-linux-x64 /usr/local/nodejs  
RUN echo "export PATH=\$PATH:/usr/local/nodejs/bin" >> /etc/bash.bashrc  
RUN cp -v /etc/login.defs /etc/login.defs.origin && cat /etc/login.defs.origin
| grep -v ENV_PATH > /etc/login.defs.tmp  
RUN cat /etc/login.defs.tmp | grep -v ENV_ROOTPATH > /etc/login.defs && rm
/etc/login.defs.tmp  
RUN echo "ENV_PATH PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/nodejs/bin" >>
/etc/login.defs  
RUN echo "ENV_ROOTPATH
PATH=/usr/local/bin:/usr/bin:/bin:/usr/local/nodejs/bin" >> /etc/login.defs  
  
ENV PATH /usr/local/nodejs/bin:$PATH  
RUN npm install -g --silent npm-check@latest  
RUN npm install -g --silent --unsafe-perm @angular/cli@latest  
  
ADD build.bash /usr/sbin/build  
RUN chmod 755 /usr/sbin/build  
WORKDIR /home  
  
ENTRYPOINT ["/usr/sbin/build"]  

