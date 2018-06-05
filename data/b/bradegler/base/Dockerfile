FROM debian:wheezy  
MAINTAINER Brad Egler "begler@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
# Fix the locale  
RUN localedef -v -c -i en_US -f UTF-8 en_US.UTF-8 || :  
# Fix initctl, in case it hasn't been fixed already  
RUN dpkg-divert --local \--rename --add /sbin/initctl && rm -f /sbin/initctl
&& ln -s /bin/true /sbin/initctl  
  
# Correct the timezone to eastern  
RUN echo "America/New_York" tee /etc/timezone && dpkg-reconfigure --frontend
noninteractive tzdata  
  
# apt-get update because we _do_ need it :(  
RUN apt-get -yq update && apt-get -yq install \  
git vim wget curl build-essential software-properties-common python-software-
properties \  
python python-dev python-pip python-virtualenv git-svn subversion mercurial
unzip zip procps \  
procps supervisor \  
&& apt-get clean  
  
RUN sed -i -e 's/\\[supervisord\\]/\\[supervisord\\]\nnodaemon=true/'
/etc/supervisor/supervisord.conf  
  
CMD ["/bin/bash"]  

