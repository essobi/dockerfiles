FROM debian:jessie  
  
MAINTAINER David Hu <chin33z@gmail.com>  
  
# last line of install packages are Bazel requirements  
RUN \  
apt-get update && \  
apt-get install -y git man gcc vim-nox cscope exuberant-ctags silversearcher-
ag \  
screen wget curl xz-utils ncdu pax-utils \  
pkg-config zlib1g-dev python unzip zip g++ bash-completion \  
make bison flex &&\  
rm -rf /var/lib/apt/lists/* &&\  
apt-get clean -yq  
  
# donwload java 8 directly and extract  
RUN wget -qO- --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" http://download.oracle.com/otn-
pub/java/jdk/8u45-b14/jdk-8u45-linux-x64.tar.gz|tar xvz  
ENV JAVA_HOME /jdk1.8.0_45  
ENV PATH $JAVA_HOME/bin:$PATH  
  
# fix the bazel building sandbox issue by disable sandboxing  
RUN echo "startup --batch" >>/tmp/bazelrc &&\  
echo "build --spawn_strategy=standalone --genrule_strategy=standalone"
>>/tmp/bazelrc  
  
# build bazel from src (tag: 1/25)  
RUN git clone https://github.com/google/bazel.git /bazel && cd /bazel && git
checkout 14aaeb90d14fdd61f109f34d13710815253eaa93 &&\  
BAZELRC=/tmp/bazelrc /bazel/compile.sh  
  
ENV PATH $PATH:/bazel/output/  
  
# config the bazel command complete  
RUN cd /bazel && \  
bazel --bazelrc=/tmp/bazelrc build //scripts:bazel-complete.bash && \  
cp bazel-bin/scripts/bazel-complete.bash /etc/bash_completion.d  
  
# create bazelrc  
RUN cd ~ &&\  
echo "build:arm --crosstool_top=//tools:toolchain --cpu=armeabi-v7a"
>>.bazelrc &&\  
echo "build:i686 --crosstool_top=//tools:toolchain --cpu=i686" >>.bazelrc &&\  
echo "build:x86_64 --crosstool_top=//tools:toolchain --cpu=x86_64" >>.bazelrc  
  
# get the bazel layer  
RUN cd ~ &&\  
echo "rm -fr blayer" >>bazel_layer.sh &&\  
echo "git clone https://github.com/chin33z/bazel_buildfiles.git blayer"
>>bazel_layer.sh &&\  
chmod u+x bazel_layer.sh  
  
# 1. git clone the vim setting  
# 2. git clone the env setting  
RUN \  
rm -fr ~/.vim ~/.vimrc &&\  
cd ~ && git clone https://github.com/chin33z/dotvim.git ~/.vim &&\  
ln -s ~/.vim/vimrc ~/.vimrc &&\  
cd ~ && git clone https://github.com/chin33z/dotfiles.git ~/dotfiles &&\  
cd dotfiles && ./link.sh  
  
ENV HOME /root  
WORKDIR /root  

