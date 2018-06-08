#  
# Ubuntu Dockerfile  
#  
# https://github.com/dockerfile/ubuntu  
#  
# Test comment  
# Pull base image.  
FROM ubuntu:14.04  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget  
  
# Install Java.  
RUN \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-
selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java7-installer  
apt-get install openjdk-7-jdk  
  
RUN echo 'JAVA_HOME=/usr/lib/jvm/java-7-oracle' >> /etc/profile; \  
echo 'PATH=$PATH:$JAVA_HOME/bin' >> /etc/profile; \  
echo 'export JAVA_HOME' >> /etc/profile; \  
echo 'export PATH' >> /etc/profile  
ENV JAVA_HOME /usr/lib/jvm/java-7-oracle  
ENV JRE_HOME /usr/lib/jvm/java-7-oracle  
ENV PATH $PATH:$JAVA_HOME/bin  
  
  
#install ruby  
RUN apt-get update  
RUN apt-get install -y git-core curl  
RUN apt-get install wget vim git --assume-yes  
RUN apt-get install build-essential curl --assume-yes  
RUN gpg --keyserver hkp://keys.gnupg.net --recv-keys D39DC0E3  
RUN \curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c rvm requirements  
RUN /bin/bash -l -c rvm install 2.1.3  
RUN /bin/bash -l -c rvm install jruby  
  
ENV PATH
/usr/local/rvm/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
#RUN /bin/bash -l -c rvm use 2.1.2 --default  
#Install ffmepg  
#RUN wget http://johnvansickle.com/ffmpeg/releases/ffmpeg-2.3.3-64bit-
static.tar.bz2  
#RUN tar xvf ~/ffmpeg-2.3.3-64bit-static.tar.bz2  
#RUN cp ~/ffmpeg-2.3.3-64bit-static/ffmpeg ~/bin  
#RUN cp ~/ffmpeg-2.3.3-64bit-static/ffprobe ~/bin  
#Install imagemagick  
RUN apt-get install -y imagemagick  
  
#Install Prince  
RUN apt-get install libgif4  
RUN wget http://www.princexml.com/download/prince_9.0-5_ubuntu14.04_amd64.deb  
RUN dpkg -i prince_9.0-5_ubuntu14.04_amd64.deb  
  
#Install RabbitMQ  
RUN apt-get install -y rabbitmq-server  
  
#Install Sphinx  
RUN apt-get install -y sphinxsearch  
  
#Install Nano  
RUN apt-get install -y nano  
  
#insalling some imp Dependencey  
RUN apt-get install -y libxslt-dev libxml2-dev  
RUN apt-get install -y libmysqlclient-dev  
RUN apt-get install -y libpq-dev  
  
#Install SSH  
RUN apt-get install -y openssh-client  
RUN apt-get install -y openssh-server  
  
#Expose port numbers  
EXPOSE 3000 8080 5800  
# Add files.  
RUN mkdir /workspace  
WORKDIR /workspace  
ADD .bashrc /.bashrc  
ADD fasternotes-set.zip /workspace/fasternotes-set.zip  
RUN unzip fasternotes-set.zip  
  
#ADD root/.gitconfig /root/.gitconfig  
#ADD root/scripts /root/scripts  
# Set environment variables.  
ENV HOME /root  
  
  
# Define working directory.  
WORKDIR /root  
  
# Define default command.  
CMD ["/bin/bash"]  

