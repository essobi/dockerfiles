FROM fujiwarakoubou/centos7-ruby  
  
# I'll have the usual.  
RUN yum -y update && yum clean all  
  
# install epel for rubygem-nokogiri  
RUN yum -y install epel-release  
  
# install nokogiri for centos  
RUN yum -y install rubygem-nokogiri  
  
# install rails  
RUN gem install rails --no-document  
  
# install libs for (rails new) and (rails server)  
RUN yum -y install ruby-devel gcc make libxslt-devel sqlite-devel git nodejs
&& yum clean all  
  
# rails server port  
EXPOSE 3000  

