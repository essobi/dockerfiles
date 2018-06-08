## Build for AWS Lint  
FROM centos:centos7  
## specify the group or individual maintaining image  
MAINTAINER George Rolston <grolston@outlook.com>  
  
## Do not change the follow  
##
----------------------------------------------------------------------------  
## Update and install necessary pacakges.  
RUN yum update -y  
RUN yum install -y epel-release  
RUN yum clean all  
RUN yum install -y awscli \  
yamllint python python-pip git \  
curl make which wget tar \  
gcc patch readline-devel zlib-devel \  
libyaml-devel libffi-devel openssl-devel \  
gdbm-devel ncurses-devel libxml-devel bzip2  
  
RUN pip install --upgrade pip  
RUN pip install boto3 \  
json-spec  
  
ENV RUBY_DIR /ruby  
ENV RUBY_VERSION 2.5.0  
ENV RUBY_INSTALL $RUBY_DIR/$RUBY_VERSION  
  
RUN cd /usr/src && \  
git clone https://github.com/sstephenson/ruby-build.git && \  
./ruby-build/install.sh && \  
mkdir -p $RUBY_INSTALL && \  
/usr/local/bin/ruby-build $RUBY_VERSION $RUBY_INSTALL && \  
rm -rf /usr/src/ruby-build  
  
ENV NODE_VERSION 8.9.4  
RUN wget
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
-O /tmp/node-v${NODE_VERSION}-linux-x64.tar.gz && \  
tar --strip-components 1 -xzvf /tmp/node-v* -C /usr/local  
  
ENV PATH $RUBY_INSTALL/bin:$PATH  
RUN gem install cfn-nag  
  
RUN yum clean all  
RUN rm -rf /var/cache/yum

