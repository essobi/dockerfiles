FROM fedora:latest  
RUN yum -y update && yum clean all  
RUN yum -y install \  
autoconf \  
automake \  
bison \  
bzip2 \  
gcc-c++ \  
git \  
glibc-devel \  
glibc-headers \  
libffi-devel \  
libtool \  
libxml2-devel \  
libxslt-devel \  
libyaml-devel \  
make \  
openssl-devel \  
patch \  
patch \  
readline-devel \  
sqlite-devel \  
which \  
zlib-devel \  
&& yum clean all  
  
RUN useradd -m awestruct  
  
USER awestruct  
WORKDIR /home/awestruct  
  
ENV HOME /home/awestruct  
ENV RUBY_VERSION 2.2.0  
ENV AWESTRUCT_VERSION 0.5.6.beta8  
  
RUN gpg2 --keyserver hkp://keys.gnupg.net --recv-keys
409B6B1796C275462A1703113804BB82D39DC0E3  
RUN curl -sSL https://get.rvm.io | bash -s stable --ruby=$RUBY_VERSION  
RUN bash -l -c "rvm use $RUBY_VERSION"  
RUN bash -l -c "rvm cleanup all"  
RUN bash -l -c "gem install awestruct -v $AWESTRUCT_VERSION \--no-rdoc --no-
ri"  
  
EXPOSE 4242  
CMD ["bash", "--login"]  

