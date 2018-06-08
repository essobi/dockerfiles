# props to WoTio Devs for inspiration (WoTio/docker-postgres)  
FROM centos  
MAINTAINER DIGIT Devs <devs@dreamitget.it>  
  
# install pg repo  
RUN rpm -i http://yum.postgresql.org/9.3/redhat/rhel-6-x86_64/pgdg-
centos93-9.3-1.noarch.rpm  
  
# install dependencies  
RUN yum install -y tar git patch make  
  
# install pgtap  
RUN yum install -y perl-CPAN  
RUN curl -LO http://xrl.us/cpanm && chmod +x cpanm  
# pg_prove  
RUN ./cpanm TAP::Parser::SourceHandler::pgTAP  
ENV PATH /usr/pgsql-9.3/bin/:$PATH  
RUN git clone git://github.com/theory/pgtap.git  
  
# install dev libraries used by pgtap  
RUN yum install -y postgresql93-devel  
  
WORKDIR /  
ADD ./install.sh /install.sh  
RUN chmod u+x /install.sh  
RUN /install.sh  
  
ADD ./test.sh /test.sh  
RUN chmod +x /test.sh  
  
CMD ["/test.sh"]  
ENTRYPOINT ["/test.sh"]  

