FROM centos:6  
MAINTAINER kbinani  
RUN yum install -y sudo tar git epel-release which  
COPY setup_gitlab_omnibus_builder.sh /tmp/setup_gitlab_omnibus_builder.sh  
RUN bash /tmp/setup_gitlab_omnibus_builder.sh  
COPY build_gitlab_omnibus.sh /tmp/build_gitlab_omnibus.sh  

