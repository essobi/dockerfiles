FROM antik486/centos71  
MAINTAINER antik486 <antik486@gmail.com>  
  
ARG ERL_VERSION=18.3  
ENV ERL_VERSION ${ERL_VERSION}  
  
RUN yum -y update; \  
yum -y install \  
tar \  
gcc \  
glibc-devel \  
make \  
ncurses-devel \  
openssl-devel \  
autoconf \  
curl \  
git; \  
yum clean all  
  
RUN curl -O https://raw.githubusercontent.com/spawngrid/kerl/master/kerl; \  
chmod +x kerl; \  
mv kerl /usr/bin; \  
kerl update releases; \  
KERL_CONFIGURE_OPTIONS=--enable-hipe kerl build ${ERL_VERSION} ${ERL_VERSION};
\  
kerl install ${ERL_VERSION} /DATA/${ERL_VERSION}; \  
kerl cleanup all; \  
rm -f .kerl/archives/*.tar.gz  
  
ENV PATH /DATA/${ERL_VERSION}/bin:$PATH  
  
#VOLUME ["/DATA"]  
#  
#WORKDIR /DATA  

