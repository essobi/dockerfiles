FROM centos:7  
RUN yum -y install http://yum.postgresql.org/9.5/redhat/rhel-7-x86_64/pgdg-
redhat95-9.5-2.noarch.rpm  
  
RUN yum update -y && \  
yum install -y wget python-virtualenv rpm-python libxml2-devel libxslt-devel
wget \  
postgresql95 postgresql95-server postgresql95-contrib postgresql95-devel \  
perl-core perl-devel perl-DBD-Pg  
  
RUN wget --no-cookies --no-check-certificate \  
\--header "Cookie: gpw_e24=http%3A%2F%2Fwww.oracle.com%2F;
oraclelicense=accept-securebackup-cookie" \  
"http://download.oracle.com/otn-
pub/java/jdk/8u112-b15/jre-8u112-linux-x64.rpm" && \  
yum localinstall -y /jre-8u112-linux-x64.rpm && \  
rm -f /jre-8u102-linux-x64.rpm  
  
RUN yum -y groupinstall "Development Tools"  
  
RUN curl -L https://cpanmin.us/ -o /usr/bin/cpanm && chmod +x /usr/bin/cpanm  
RUN cpanm --notest App::Sqitch  
  
RUN curl -L
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein -o
/usr/bin/lein && chmod +x /usr/bin/lein  
  
RUN yum clean all  
  
# Set environment variables.  
ENV HOME /root  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["bash"]  

