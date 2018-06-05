FROM ubuntu-upstart:14.04  
COPY Dockerfile /  
COPY install-reddit.sh /  
  
RUN mkdir install  
COPY install /install/  
  
#install python 2.7.6  
RUN \  
apt-get update && \  
apt-get install -y python python-dev python-pip python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update \  
&& apt-get install -y wget \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN chmod +x ./install-reddit.sh  
  
RUN chmod +x ./install  
  
RUN apt-get install binutils  
  
MAINTAINER mcrouter <mcrouter@fb.com>  
  
ENV MCROUTER_DIR /usr/local/mcrouter  
ENV MCROUTER_REPO https://github.com/facebook/mcrouter.git  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y git  
RUN mkdir -p $MCROUTER_DIR/repo  
RUN cd $MCROUTER_DIR/repo  
RUN git clone $MCROUTER_REPO  
  
#RUN cd $MCROUTER_DIR/repo/mcrouter/mcrouter/scripts && \  
# ./clean_ubuntu_14.04.sh $MCROUTER_DIR && rm -rf $MCROUTER_DIR/repo && \  
# ln -s $MCROUTER_DIR/install/bin/mcrouter /usr/local/bin/mcrouter  
#add a new user  
#RUN useradd -ms /bin/bash newuser  
#USER newuser  
#WORKDIR /home/newuser  
#RUN apt-transport-https  
#RUN apt-get install software-properties-common  
#RUN ./install-reddit.sh  

