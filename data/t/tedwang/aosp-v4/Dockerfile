#  
# We can use either base12 or base14  
#  
FROM tedwang/aosp-base12:latest  
  
MAINTAINER tedwang.tw@gmail.com  
  
#  
# AOSP requirement depends on android versions  
#  
# Java 6  
# Never ask for confirmations from Oracle  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo "debconf shared/accepted-oracle-license-v1-1 select true" |
/usr/bin/debconf-set-selections  
RUN echo "debconf shared/accepted-oracle-license-v1-1 seen true" |
/usr/bin/debconf-set-selections  
RUN apt-get update  
RUN apt-get install python-software-properties -y  
RUN add-apt-repository ppa:webupd8team/java  
RUN apt-get update  
RUN apt-get install oracle-java6-installer -y  
RUN apt-get install oracle-java6-set-default -y  
  
# Clean up  
RUN apt-get clean  
  
#  
# user account  
#  
ENV MYNAME android  
ENV MYPASS android  
ENV HOME /home/$MYNAME  
#RUN mkdir -p $HOME  
RUN echo "User: android Pass: $MYPASS"  
RUN useradd --create-home -d $HOME \--shell /bin/bash --user-group --groups
adm,sudo $MYNAME  
RUN echo "$MYNAME:$MYPASS" | chpasswd  
  
USER $MYNAME  
WORKDIR $HOME  
  
#VOLUME ["$HOME/aosp"]  
# shell prompt  
ENV PS1 "\$(if [[ \$? == 0 ]]; then echo '\\[\033[0;32m\\]'; else echo
'\\[\033[0;31m\\]'; fi)\$? \$(if [[ ${EUID} == 0 ]]; then echo
'\\[\033[0;31m\\]\u'; else echo '\\[\033[0;34m\\]\u@'; fi)\\[\033[0;33m\\] \w
\\[\033[0;32m\\]\$\\[\033[00m\\] "  
RUN echo export PS1="$PS1" >> ~/.bashrc  
  
#  
# AOSP Repo tool  
#  
RUN mkdir ~/bin  
RUN echo "export PATH=~/bin:\$PATH" >> ~/.bashrc  
#ENV PATH ~/bin:$PATH  
RUN curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo  
RUN chmod a+x ~/bin/repo  
  
#ENV JAVA_HOME /usr/bin/java  
#ENV PATH $JAVA_HOME:$PATH  

