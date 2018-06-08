#Seiichiro Kurihara Dev  
FROM debian:jessie  
MAINTAINER Seiichiro Kurihara <strange.fruits.d.u.c.a@gmail.com>  
  
#APT-GET INSTALL  
RUN apt-get update  
RUN apt-get -y install git --no-install-recommends  
RUN apt-get -y install git-flow --no-install-recommends  
RUN apt-get -y install wget --no-install-recommends  
RUN apt-get -y install gcc --no-install-recommends  
RUN apt-get -y install make --no-install-recommends  
RUN apt-get -y install lua5.2 --no-install-recommends  
RUN apt-get -y install liblua5.2-dev --no-install-recommends  
RUN apt-get -y install bzip2 --no-install-recommends  
RUN apt-get -y install bash-completion --no-install-recommends  
RUN apt-get -y install ca-certificates --no-install-recommends  
RUN apt-get -y install openssh-server --no-install-recommends  
RUN apt-get -y install supervisor --no-install-recommends  
RUN apt-get -y install locales --no-install-recommends  
RUN apt-get upgrade -y && apt-get clean && rm -rf /var/cache/apt/archives/*
/var/lib/apt/lists/*  
  
#Install Vim  
RUN cd /usr/local/src \  
&& wget ftp://ftp.vim.org/pub/vim/unix/vim-7.4.tar.bz2 \  
&& tar -xvf vim-7.4.tar.bz2 \  
&& cd vim74 \  
&& ./configure \  
\--enable-multibyte \  
\--with-features=huge \  
\--enable-luainterp \  
&& make \  
&& make install  
  
#Install Golang  
RUN cd /usr/local/src \  
&& wget --no-check-certificate
https://storage.googleapis.com/golang/go1.6.linux-amd64.tar.gz \  
&& tar -xvf go1.6.linux-amd64.tar.gz \  
&& mv go /usr/local/  
  
#Cleaning Dir  
RUN rm -rf /usr/local/src/*  
  
ENV DEVELOPER=${DEVELOPER:-skadmin}  
ENV DEVELOPER_GROUP=${DEVELOPER_GROUP:-skadmin}  
ENV DEVELOPER_HOME=/home/${DEVELOPER}  
ENV DEVELOPER_PASSWORD=${DEVELOPER_PASSWORD:-skadmin}  
ENV GIt_DEVELOPER_NAME=${GIt_DEVELOPER_NAME:-seiichiro}  
ENV GIT_DEVELOPER_MAIL=${GIT_DEVELOPER_MAIL:-example@example.com}  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
ENV TZ=Asia/Tokyo  
ENV PATH="$PATH":/usr/local/go/bin  
ENV GOPATH=${DEVELOPER_HOME}/go  
  
#Supervisor  
RUN mkdir -p /var/log/supervisor  
  
COPY . /usr/local/src/  
  
ONBUILD RUN groupadd -g 1000 ${DEVELOPER_GROUP} \  
&& useradd -u 1000 -d ${DEVELOPER_HOME} -g ${DEVELOPER_GROUP} -m -s /bin/bash
${DEVELOPER} \  
&& echo ${DEVELOPER}:${DEVELOPER_PASSWORD} | chpasswd \  
&& echo '${DEVELOPER} ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \  
&& mkdir ${GOPATH}  
  
ONBUILD RUN echo alias vi=\'vim\' >> ${DEVELOPER_HOME}/.bashrc \  
&& echo alias ls=\'ls --color=auto\' >> ${DEVELOPER_HOME}/.bashrc \  
&& echo alias ll=\'ls -la\' >> ${DEVELOPER_HOME}/.bashrc  
  
ONBUILD RUN mkdir /var/run/sshd \  
&& sed -ri 's/PermitRootLogin without-password/PermitRootLogin no/'
/etc/ssh/sshd_config \  
&& sed -ri 's/^UsePAM yes/UsePAM no/' /etc/ssh/sshd_config \  
&& sed -ri 's/^#PasswordAuthentication yes/PasswordAuthentication no/'
/etc/ssh/sshd_config \  
&& sed -ri 's/^#AuthorizedKeysFile/AuthorizedKeysFile/' /etc/ssh/sshd_config \  
&& echo "AllowUsers ${DEVELOPER}" >> /etc/ssh/sshd_config  
  
#RUN mkdir -p ${DEVELOPER_HOME}/.vim/bundle \  
# && mkdir -p ${DEVELOPER_HOME}/.vim/colors \  
# && git clone https://github.com/Shougo/vimproc.vim
${DEVELOPER_HOME}/.vim/bundle/vimproc.vim \  
# && git clone https://github.com/tomasr/molokai \  
# && mv molokai/colors/molokai.vim ${DEVELOPER_HOME}/.vim/colors/ \  
# && rm -rf molokai \  
# && git clone https://github.com/fatih/vim-go.git
${DEVELOPER_HOME}/.vim/bundle/vim-go  
#GIT CONFIG  
ONBUILD RUN git config --global user.name "${GIt_DEVELOPER_NAME}" \  
&& git config --global user.email "${GIT_DEVELOPER_MAIL}" \  
&& git config --global color.ui auto \  
&& git config --global color.diff auto \  
&& git config --global color.status auto \  
&& git config --global color.branch auto \  
&& git config --global core.editor vim \  
&& git config --global core.excludesfile ${DEVELOPER_HOME}/.gitignore  
  
#SSH RSA KEY  
ONBUILD RUN mkdir -p ${DEVELOPER_HOME}/.ssh \  
&& cd ${DEVELOPER_HOME}/.ssh \  
&& ssh-keygen -t rsa -N '' -f id_rsa \  
&& cat id_rsa.pub >> authorized_keys  
  
#GIT RSA KEY  
ONBUILD RUN cd ${DEVELOPER_HOME}/.ssh \  
&& ssh-keygen -t rsa -N '' -f git_rsa  
  
ONBUILD RUN mv /usr/local/src/supervisord.conf
/etc/supervisor/conf.d/supervisord.conf  
ONBUILD RUN mv /usr/local/src/* ${DEVELOPER_HOME}/  
ONBUILD COPY . ${DEVELOPER_HOME}/  
  
#SSH PERMISSION  
ONBUILD RUN chmod 700 ${DEVELOPER_HOME}/.ssh \  
&& chmod 600 ${DEVELOPER_HOME}/.ssh/id_rsa \  
&& chmod 600 ${DEVELOPER_HOME}/.ssh/id_rsa.pub \  
&& chmod 600 ${DEVELOPER_HOME}/.ssh/authorized_keys  
  
#GIT PERMISSION  
ONBUILD RUN chmod 600 ${DEVELOPER_HOME}/.ssh/git_rsa \  
&& chmod 600 ${DEVELOPER_HOME}/.ssh/git_rsa.pub  
  
#DEVELOPERDIR PERMISSION  
ONBUILD RUN chown -R ${DEVELOPER}:${DEVELOPER} ${DEVELOPER_HOME}  
  
ONBUILD RUN cat ${DEVELOPER_HOME}/.ssh/id_rsa  
ONBUILD RUN cat ${DEVELOPER_HOME}/.ssh/git_rsa.pub  
  
#PORT  
EXPOSE 22  
#CMD  
CMD ["/usr/bin/supervisord"]  

