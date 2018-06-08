FROM lambci/lambda:build-python3.6  
ENV AWS_DEFAULT_REGION us-esast-1  
# This is a nasty solution, but necessary for now. I tried to solve why this
is  
# failing, but cannot  
RUN yum install -y libxml2-devel libxslt-devel || yum install -y libxml2-devel
libxslt-devel  
  
RUN useradd circleci  
#USER circleci:circleci  

