FROM centos:7  
LABEL maintainer="gie.spaepen@rombit.be"  
  
RUN yum -y update && yum -y install wget && yum -y install curl && \  
yum -y groupinstall "Development tools" && \  
yum -y install libpng-devel && \  
wget https://dl.yarnpkg.com/rpm/yarn.repo -O /etc/yum.repos.d/yarn.repo && \  
curl --silent --location https://rpm.nodesource.com/setup_6.x | bash - && \  
yum -y install yarn && \  
mkdir /build && \  
cd /build  
  
WORKDIR /build  
  
ENTRYPOINT pwd && ls && yarn install && npm rebuild && echo "Building env:
${BUILD_ENV}" && yarn build-${BUILD_ENV} && npm test  

