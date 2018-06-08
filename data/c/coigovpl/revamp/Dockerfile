FROM centos:7  
MAINTAINER Krzysztof Suszyński <krzysztof.suszynski@coi.gov.pl>  
  
ENV REVAMP_USER revamp  
ENV REVAMP_VERSION 1.1.1  
ENV REVAMP_USER_ID 764  
ENV REVAMP_HOMEDIR /home/$REVAMP_USER  
  
RUN yum install -y ruby rpm-build  
RUN gem install revamp --version $REVAMP_VERSION  
RUN useradd --system --create-home --uid $REVAMP_USER_ID \--home-dir
$REVAMP_HOMEDIR $REVAMP_USER  
USER $REVAMP_USER  
RUN mkdir -p $REVAMP_HOMEDIR/rpmbuild  
CMD ["revamp", "--help"]  

