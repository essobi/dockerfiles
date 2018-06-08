FROM buildpack-deps:stretch-scm  
LABEL maintainer "iimuz"  
  
# set locale  
RUN apt-get update && apt-get install -y --no-install-recommends \  
apt-utils \  
locales \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo en_US.UTF-8 UTF-8 > /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
# hugo  
ENV HUGO_VERSION=0.37  
ENV HUGO_ARCHIVE=hugo_${HUGO_VERSION}_Linux-64bit.tar.gz  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_ARCHIVE}
/usr/local  
RUN tar xzf /usr/local/${HUGO_ARCHIVE} -C /usr/local/bin/ \  
&& rm /usr/local/bin/*.md \  
&& rm /usr/local/${HUGO_ARCHIVE}  
  
# vim  
RUN apt-get update && apt-get install -y --no-install-recommends \  
gcc \  
libc-dev \  
make \  
vim \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# add dev user  
ENV HOME /home/dev  
COPY ./home $HOME  
RUN adduser dev --disabled-password --gecos "" \  
&& echo "ALL ALL = (ALL) NOPASSWD: ALL" >> /etc/sudoers \  
&& chown -R dev:dev /home/dev  
USER dev  
  
# install dein.vim  
RUN mkdir -p ${HOME}/.cache/dein \  
&& curl -L
https://raw.githubusercontent.com/Shougo/dein.vim/master/bin/installer.sh >
$HOME/installer.sh \  
&& sh $HOME/installer.sh $HOME/.cache/dein \  
&& rm $HOME/installer.sh \  
&& vim +":silent! call dein#install()" +qall  
  
WORKDIR ${HOME}  
  

