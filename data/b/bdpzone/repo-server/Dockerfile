FROM bdpzone/bdpfedora21  
MAINTAINER "Mark Olliver" <mark.olliver@bigdatapartnership.com>  
ADD etc /etc  
ADD var /var  
ADD usr /usr  
RUN mkdir /mirror  
RUN rpm --rebuilddb  
RUN curl --insecure -L https://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key -o
/tmp/jenkins-ci.org.key  
RUN rpm --import /tmp/jenkins-ci.org.key  
RUN curl http://rex.linux-files.org/RPM-GPG-KEY-REXIFY-REPO -o /tmp/rex.key  
RUN rpm --import /tmp/rex.key  
RUN curl -L http://pkg.jenkins-ci.org/redhat/jenkins.repo -o
/etc/yum.repos.d/jenkins.repo  
RUN yum -y update  
RUN yum -y install curl git ansible nginx lsof java-1.7.0-openjdk-headless \  
net-tools jenkins sudo python-pip perl perl-Config-General \  
perl-Log-Log4perl perl-XML-LibXML perl-Compress-Zlib \  
perl-common-sense perl-Moose perl-libwww-perl perl-Try-Tiny \  
perl-Params-Validate perl-IO-All wget createrepo perl-ExtUtils-MakeMaker \  
perl-Test-Simple perl-Digest-SHA make perl-XML-Simple perl-TermReadKey tar \  
perl-Mojolicious perl-JSON-XS perl-Term-ProgressBar  
RUN curl -L http://bit.ly/Hqvfi9 -o /tmp/artifactory-3.5.2.1.rpm  
RUN rpm -i /tmp/artifactory-3.5.2.1.rpm  
RUN rpm -i http://download.go.cd/gocd-rpm/go-server-14.4.0-1356.noarch.rpm  
RUN rpm -i http://download.go.cd/gocd-rpm/go-agent-14.4.0-1356.noarch.rpm  
RUN ln -s /mirror/python/localshop /root/.localshop  
RUN ln -s /mirror/artifactory/data/ /opt/jfrog/artifactory/data  
RUN curl -L http://get.repositor.io/downloads/Rex-Repositorio-1.0.0.tar.gz -o
/tmp/Rex-Repositorio-1.0.0.tar.gz  
RUN cd /tmp \  
tar zxf Rex-Repositorio-1.0.0.tar.gz \  
cd Rex-Repositorio-1.0.0 \  
perl Makefile.PL \  
make \  
make install  
RUN systemctl enable localshop.service  
RUN systemctl enable nginx.service  
RUN yum clean all  
  
VOLUME ["/sys/fs/cgroup"]  
EXPOSE 80  
CMD ["/bin/start.sh"]  
  
################################################################################  
# Copyright 2015 Big Data Partnership Ltd #  
# #  
# Licensed under the Apache License, Version 2.0 (the "License"); #  
# you may not use this file except in compliance with the License. #  
# You may obtain a copy of the License at #  
# #  
# http://www.apache.org/licenses/LICENSE-2.0 #  
# #  
# Unless required by applicable law or agreed to in writing, software #  
# distributed under the License is distributed on an "AS IS" BASIS, #  
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. #  
# See the License for the specific language governing permissions and #  
# limitations under the License. #  
################################################################################  
  

