FROM fedora:21  
MAINTAINER fabric8.io <fabric8@googlegroups.com>  
  
#RUN curl -L https://raw.githubusercontent.com/Netflix-Skunkworks/jenkins-
cli/master/bin/jenkins > ./jenkins && \  
# chmod 755 ./jenkins  
RUN yum install -y cpan tar make git gcc  
  
RUN git clone https://github.com/Netflix-Skunkworks/jenkins-cli.git
/home/jenkins-cli  
WORKDIR /home/jenkins-cli  
  
RUN cpan YAML::Syck  
RUN cpan LWP::UserAgent  
ADD builder.sh builder.sh  
CMD bash '/home/jenkins-cli/builder.sh';

