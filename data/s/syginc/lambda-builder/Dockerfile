FROM amazonlinux:2017.03  
  
RUN yum -y groupinstall 'Development Tools' && \  
yum -y install ImageMagick-devel python27-pip python36 python36-pip nasm && \  
pip-2.7 install pipenv && \  
pip-3.6 install pipenv && \  
curl --silent --location https://rpm.nodesource.com/setup_8.x | bash - && \  
curl --silent --location https://dl.yarnpkg.com/rpm/yarn.repo | tee
/etc/yum.repos.d/yarn.repo && \  
yum -y install nodejs-8.10.0 yarn && \  
yum -y clean all  
  
# For pipenv  
ENV LANG en_US.UTF-8  

