# Scala and SBT on CentOS 7 with Oracle Java JDK 8  
# Reference: http://github.com/ecompositor/centos-scala  
# Script to download Oracle JDK:
https://gist.github.com/n0ts/40dd9bd45578556f93e7  
FROM centos:centos7  
MAINTAINER Denis Arnaud <denis.arnaud_github at m4x dot org>  
  
# Import the Centos-7 GPG key to prevent warnings  
RUN rpm --import http://mirror.centos.org/centos/RPM-GPG-KEY-CentOS-7  
  
# Update of CentOS  
RUN yum -y clean all  
RUN yum -y upgrade  
  
# EPEL  
RUN yum -y install epel-release  
  
# Base install  
RUN yum -y install git-all unzip tar wget curl maven rake rubygem-rake which  
  
# Add bintray repository where the SBT binaries are published  
RUN curl -sS https://bintray.com/sbt/rpm/rpm | tee /etc/yum.repos.d/bintray-
sbt-rpm.repo  
RUN yum -y install sbt  
  
# Customization  
ENV JDK_VERSION 8u141  
ENV JDK_VERSION_MINOR b15  
ENV JDK_RPM jdk-$JDK_VERSION-linux-x64.rpm  
ENV JDK_RPM_TOKEN 336fa29ff2bb4ef291e347e091f7f4a7  
ENV JDK_RPM_URL http://download.oracle.com/otn-
pub/java/jdk/$JDK_VERSION-$JDK_VERSION_MINOR/$JDK_RPM_TOKEN  
ENV SCALA_TAR_URL http://www.scala-lang.org/files/archive  
ENV SCALA_VERSION 2.11.8  
ENV SBT_VERSION 0.13.16  
ENV SBT_OPTS -Xmx4G  
ENV JDK_GETTER get_oracle_jdk_linux_x64.sh  
ENV HOME /root  
ENV SBT_GBL $HOME/.sbt/0.13/global.sbt  
ENV BOM4V_DIR=/opt/bom4v  
  
# Download Java in a robust way  
#ADD $JDK_GETTER /usr/local/bin  
#RUN chmod a+x /usr/local/bin/$JDK_GETTER  
#RUN /usr/local/bin/$JDK_GETTER  
# Download Java in a ad hoc way (see
https://stackoverflow.com/questions/10268583/downloading-java-jdk-on-linux-
via-wget-is-shown-license-page-instead)  
RUN wget -c --header "Cookie: oraclelicense=accept-securebackup-cookie"
$JDK_RPM_URL/$JDK_RPM  
  
# Install Java  
RUN yum -y install $JDK_RPM  
# Uncomment the following line when the Docker build process works well
(during development process, it is much quicker not to re-downloading it
everytime)  
#RUN rm -f $JDK_RPM  
# Install Scala  
RUN wget $SCALA_TAR_URL/scala-$SCALA_VERSION.tgz  
RUN tar xvf scala-$SCALA_VERSION.tgz  
RUN mv scala-$SCALA_VERSION /usr/lib  
RUN ln -s /usr/lib/scala-$SCALA_VERSION /usr/lib/scala  
# Uncomment the following line when the Docker build process works well  
#RUN rm -f scala-$SCALA_VERSION.tgz  
ENV PATH $PATH:/usr/lib/scala/bin  
  
# Run SBT once, at Docker build time, so that it does not download the
dependencies at run time  
RUN sbt version  
  
# XML parsing with Ruby, thanks to Nokogiri  
RUN yum -y install rubygem-nokogiri  
  
# Copy the SSH keys  
RUN mkdir -p $HOME/.ssh && chmod 700 $HOME/.ssh  
RUN ssh-keyscan github.com > $HOME/.ssh/known_hosts  
ADD ssh-config $HOME/.ssh/  
RUN mv $HOME/.ssh/ssh-config $HOME/.ssh/config  
RUN chmod 600 $HOME/.ssh/config $HOME/.ssh/known_hosts  
  
# Prepare the build environment  
RUN mkdir -p $BOM4V_DIR  
ADD Rakefile metamodels.yaml.sample $BOM4V_DIR/  
RUN mv $BOM4V_DIR/metamodels.yaml.sample $BOM4V_DIR/metamodels.yaml  
  
# Build the TI Models  
WORKDIR $BOM4V_DIR  
RUN rake clone && rake checkout && rake offline=true deliver  
  
# Give the hand back to the user  
CMD ["bash"]  
  

