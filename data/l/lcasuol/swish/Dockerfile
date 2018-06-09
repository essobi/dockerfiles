FROM ubuntu:16.04  
# Debian Jessie image released 2016 May 03.  
#FROM
debian@sha256:f7062cf040f67f0c26ff46b3b44fe036c29468a7e69d8170f37c57f2eec1261b  
MAINTAINER Kacper Sokol <ks1591@bristol.ac.uk>  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
USER root  
RUN apt-get update \  
&& apt-get install -y software-properties-common  
RUN apt-add-repository ppa:swi-prolog/devel \  
&& apt-get update \  
&& apt-get install -y \  
git \  
swi-prolog \  
graphviz \  
npm \  
nodejs-legacy  
#wget \  
#unzip \  
RUN npm install -g bower  
RUN npm install -g clean-css-cli requirejs  
  
# Set environment variables  
ENV SHELL /bin/bash  
ENV SWISH_DIR /opt/swish  
ENV SWISH_USER jovyan  
ENV SWISH_UID 1000  
ENV HOME /home/$SWISH_USER  
#ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
# Create jovyan user with UID=1000 and in the 'users' group \ -N -u $SWISH_UID  
RUN useradd -m -s /bin/bash $SWISH_USER \  
&& mkdir -p $SWISH_DIR \  
&& chown $SWISH_USER $SWISH_DIR  
  
#RUN git clone https://github.com/marc-hanheide/swish.git $SWISH_DIR \  
# # Use global 3050  
# && echo ":- use_module(server).\n:- initialization server(3050)." >
$SWISH_DIR/run.pl \  
# && cd $SWISH_DIR \  
# && bower install  
#RUN date  
#RUN cd $SWISH_DIR && cat Makefile  
#RUN cd $SWISH_DIR && make js  
#&& make  
ADD .git/index /tmp/git-index  
  
COPY . $SWISH_DIR  
RUN chown -R $SWISH_USER $SWISH_DIR  
  
#RUN git clone -b old-version-working-for-now https://github.com/marc-
hanheide/swish.git $SWISH_DIR  
# \  
#&& wget http://www.swi-prolog.org/download/swish/swish-bower-components.zip
-P $HOME \  
#&& unzip -o $HOME/swish-bower-components.zip -d $SWISH_DIR  
USER $SWISH_USER  
WORKDIR $SWISH_DIR  
  
RUN bower install  
RUN echo ":- use_module(server).\n:- initialization server(3050)." >
$SWISH_DIR/run.pl  
  
EXPOSE 3050  
WORKDIR /home/$SWISH_USER  
  
# Configure container startup  
ENTRYPOINT ["start-swish.sh"]  
#CMD ["start-swish.sh"]  
# Add local files as late as possible to avoid cache busting  
COPY start-swish.sh /usr/local/bin/

