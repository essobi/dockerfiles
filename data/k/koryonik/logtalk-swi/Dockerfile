FROM ubuntu:14.04  
MAINTAINER Damien Roch, damien.roch@gmail.com  
  
# Add swi PPA  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:swi-prolog/stable  
  
# Install SWI & utils from packages  
RUN apt-get -qy update \  
&& apt-get install -y swi-prolog-nox unzip wget  
  
# Install logtalk3 from source  
RUN mkdir -p /logtalk  
WORKDIR /logtalk  
RUN wget -O /logtalk/logtalk3.zip
https://github.com/LogtalkDotOrg/logtalk3/archive/lgt3021stable.zip \  
&& unzip logtalk3.zip \  
&& cd logtalk3-lgt3021stable/scripts \  
&& ./install.sh -p /usr \  
&& ./logtalk_user_setup.sh  
  
# Configure logtalk3  
ENV LOGTALKHOME /usr/share/logtalk  
ENV LOGTALKUSER /root/logtalk  
ENV PATH
$PATH:$LOGTALKHOME/tools/lgtdoc/xml:$LOGTALKHOME/scripts:$LOGTALKHOME/integration  
ENV MANPATH $MANPATH:$LOGTALKHOME/man  
  
# Configure default unicode locale  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
# Set up the source directory  
VOLUME ["/source"]  
WORKDIR /source  
  
# Set up the command arguments  
CMD ["-"]  
ENTRYPOINT ["swilgt"]  

