FROM ubuntu:trusty  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV MONGO_MAJOR 3.0  
ENV MONGO_VERSION 3.0.6  
# setting up ssh  
RUN mkdir -p /var/run/sshd  
RUN useradd dev -m -p idatadev -s /bin/bash  
RUN echo "dev:idatadev" | chpasswd  
RUN echo "dev ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers  
  
# chinese language package  
RUN locale-gen zh_CN.UTF-8  
  
COPY deltmp.py /usr/bin/deltmp  
RUN chmod ugo+x /usr/bin/deltmp  
  
# change timezone  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  
  
# use 163 sources list  
# RUN cp /etc/apt/sources.list /etc/apt/sources.list.orig  
# COPY sources.list.trusty /etc/apt/sources.list  
COPY sources.list.trusty /etc/apt/sources.list.163  
COPY resolv.conf /etc/resolv.conf  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0
multiverse" > /etc/apt/sources.list.d/mongodb-org.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10  
  
# update  
RUN apt-get update  
RUN set -x \  
&& apt-get install -y \  
software-properties-common \  
curl  
RUN curl --silent --location https://deb.nodesource.com/setup_4.x | sudo bash
-  
RUN add-apt-repository ppa:fkrull/deadsnakes -y && apt-get update  
RUN apt-get dist-upgrade -y  
  
# install basic software  
RUN apt-get install -y \  
bpython \  
build-essential \  
clang \  
cmake \  
coffeescript \  
dstat \  
git \  
git-all \  
htop \  
ipython \  
libclang-dev \  
libncurses5-dev \  
libpcre3-dev \  
libreadline-dev \  
libssl-dev \  
lsof \  
make \  
mercurial \  
mlocate \  
mongodb-org-mongos=$MONGO_VERSION \  
mongodb-org-shell=$MONGO_VERSION \  
mongodb-org-tools=$MONGO_VERSION \  
mongodb-org=$MONGO_VERSION \  
nginx \  
nodejs \  
openssh-client \  
openssh-server \  
perl \  
python-dev \  
python-pip \  
python3.5 \  
python3.5-dev \  
redis-server \  
rpl \  
rubygems-integration \  
silversearcher-ag \  
tmux \  
tree \  
vim \  
xtail  
  
ENV OPENRESTY_DIR /root/download/openresty  
RUN mkdir -p $OPENRESTY_DIR  
WORKDIR $OPENRESTY_DIR  
RUN wget https://openresty.org/download/ngx_openresty-1.7.10.2.tar.gz  
RUN tar xzf ngx_openresty-1.7.10.2.tar.gz  
WORKDIR ./ngx_openresty-1.7.10.2  
RUN ./configure && make && make install  
  
# changel npm to local source  
RUN npm config set strict-ssl false  
RUN npm install -g cnpm --registry=https://registry.npm.taobao.org  
  
# install frontend tools  
# RUN cnpm install -g \  
RUN npm install -g \  
avoscloud-code \  
js2coffee \  
avoscloud-sdk \  
base-x \  
body-parser \  
clean-css \  
coffee-script \  
cookie-parser \  
coffeelint \  
dateformat \  
dynamic-dedupe \  
ejs \  
escape-html \  
express \  
fis \  
fis-optimizer-html-minifier \  
fis-optimizer-shutup \  
fis-postpackager-simple \  
fis-postprocessor-autoprefixer \  
fis-postprocessor-require-async \  
fis-pure \  
hiredis \  
html-minifier \  
html-to-text \  
ioredis \  
leanengine \  
marked \  
node-dev \  
node-uuid \  
q \  
qiniu \  
redis-evalsha \  
request \  
rootpath \  
to-markdown \  
underscore \  
underscore.string  
  
# install python 2.7.10  
# ENV PY_DIR /root/download  
# RUN mkdir -p $PY_DIR  
# WORKDIR $PY_DIR  
# RUN wget https://www.python.org/ftp/python/2.7.10/Python-2.7.10.tgz  
# RUN tar xzf Python-2.7.10.tgz  
# WORKDIR ./Python-2.7.10  
# RUN ./configure && make install  
# install vim-plugin  
COPY vimrc /etc/vim/vimrc.local  
RUN git clone https://github.com/gmarik/Vundle.vim.git
/usr/share/vim/vimfiles/bundle/Vundle.vim  
RUN vim +PluginInstall +qall  
ENV YCM_DIR /usr/share/vim/vimfiles/bundle/YouCompleteMe  
WORKDIR $YCM_DIR  
RUN ./install.sh --clang-completer  
  
WORKDIR /home/dev  
RUN gem install sass  
# RUN gem sources --remove http://rubygems.org/  
# RUN gem sources -a http://ruby.taobao.org/  
RUN pip install virtualenv trash-cli  
RUN apt-get install -y python3-markupsafe  
USER dev  
RUN mkdir /home/dev/.hgplugin  
RUN curl https://bitbucket.org/GrahamHelliwell/hg-
sync/raw/cdb1d3f0ca68766d775746b02b301547ce3af0df/sync.py >
/home/dev/.hgplugin/sync.py  
COPY tmux_default /home/dev/.tmux_default  
COPY coffeelint.json /home/dev/.coffeelint.json  
COPY hgrc /home/dev/.hgrc  
COPY hgignore /home/dev/.hgignore  
COPY requirement.txt /home/dev/requirement.txt  
COPY bashrc /home/dev/.bashrc  
  
# python libs  
RUN virtualenv -p /usr/bin/python3.5 /home/dev/.py3env  
RUN ["/bin/bash", "-c", "source ~/.py3env/bin/activate && pip3.5 install -e
hg+https://btyh17mxy@bitbucket.org/pypa/wheel#egg=python-whell"]  
RUN /bin/bash -c "source ~/.py3env/bin/activate && pip3.5 install -r
/home/dev/requirement.txt"  
  
USER root  
COPY fix_print.py /usr/lib/python3.5/lib2to3/fixes/fix_print.py  
  
WORKDIR /root  
ENTRYPOINT ["/usr/sbin/sshd", "-f", "/etc/ssh/sshd_config", "-D"]  

