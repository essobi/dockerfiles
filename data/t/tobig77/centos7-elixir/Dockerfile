FROM centos:centos7  
  
MAINTAINER Tobias Gerschner <tobias.gerschner@gmail.com>  
  
ENV ERLANG_VERSION 20.2.2  
ENV ELIXIR_VERSION 1.6.1  
ENV ELIXIR_BINARIES mix elixirc elixir iex  
  
# Set the locale(en_US.UTF-8)`  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN yum clean all && \  
yum -y install --setopt=tsflags=nodocs epel-release wget unzip uuid less bzip2
git-core inotify-tools && \  
yum -y install http://packages.erlang-solutions.com/erlang-
solutions-1.0-1.noarch.rpm && \  
yum -y install esl-erlang-${ERLANG_VERSION} && \  
yum -y update && \  
yum -y reinstall glibc-common glibc && \  
yum clean all && \  
find /var/cache/yum -type f -exec rm -f '{}' \;  
  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8  
  
RUN cd /tmp && \  
wget https://github.com/elixir-
lang/elixir/releases/download/v${ELIXIR_VERSION}/Precompiled.zip && \  
unzip -d /usr/local/elixir -x Precompiled.zip && \  
rm -f /tmp/Precompiled.zip  
  
ADD elixir_profile.sh /etc/profile.d/elixir.sh  
  
RUN echo "export LANG=en_US.utf-8" >> /etc/bashrc  
RUN echo "export LANGUAGE=en_US:en" >> /etc/bashrc  
RUN echo "export LC_ALL=en_US.UTF-8" >> /etc/bashrc  
  
RUN PATH=$PATH:/usr/local/elixir/bin mix local.hex --force  
RUN PATH=$PATH:/usr/local/elixir/bin mix local.rebar --force  

