FROM fedora  
MAINTAINER Dávid Halász <skateman@skateman.eu>  
LABEL Description="Rubinius docker image" Version="2.5.8"  
  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV RBX_VERSION='2.5.8'  
ENV RBX_HOME /opt/rubinius  
ENV GEM_HOME $RBX_HOME/gems  
  
RUN buildDeps='ruby \  
rubygem-bundler \  
rubygem-rake \  
ruby-devel \  
make \  
gcc-c++ \  
llvm-static \  
llvm-devel \  
zlib-devel \  
openssl-devel \  
libedit-devel \  
perl' \  
&& runDeps='curl tar bzip2 libstdc++ llvm libedit zlib' \  
&& dnf -y install $runDeps $buildDeps \  
&& echo 'gem: --no-document' >> "$HOME/.gemrc" \  
&& srcDir='/usr/src/rbx' \  
&& mkdir -p $srcDir \  
&& curl
"https://s3.amazonaws.com/releases.rubini.us/rubinius-${RBX_VERSION}.tar.bz2"
| tar -xjC $srcDir \--strip-components=1 \  
&& cd $srcDir \  
&& bundle \  
&& ./configure --prefix=$RBX_HOME \  
&& rake build \  
&& rake install \  
&& cd \  
&& rm -rf $srcDir \  
&& dnf -y remove $buildDeps \  
&& dnf -y autoremove \  
&& dnf -y clean all  
  
ENV PATH $GEM_HOME/bin:$RBX_HOME/bin:$PATH  
  
RUN gem install bundler  
  
CMD [ "irb" ]  

