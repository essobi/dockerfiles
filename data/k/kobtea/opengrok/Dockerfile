FROM tomcat:9.0  
MAINTAINER kobtea  
  
RUN apt-get update && \  
apt-get install -y git inotify-tools autoconf pkg-config make gcc  
RUN git clone \--depth 1 https://github.com/universal-ctags/ctags.git
/tmp/ctags  
WORKDIR /tmp/ctags  
RUN bash autogen.sh && \  
bash configure && \  
make && \  
make install  
  
RUN mkdir -p /var/opengrok/src /var/opengrok/data  
RUN wget -O -
https://github.com/OpenGrok/OpenGrok/releases/download/1.0/opengrok-1.0.tar.gz
| tar xvzf - --directory=/var/opengrok --strip-components=1  
  
ENV OPENGROK_TOMCAT_BASE /usr/local/tomcat  
ENV OPENGROK_INSTANCE_BASE /var/opengrok  
ENV SRC_ROOT $OPENGROK_INSTANCE_BASE/src  
ENV SKIN='-L default'  
ENV WEBAPP_NAME source  
  
RUN /var/opengrok/bin/OpenGrok update  
RUN /var/opengrok/bin/OpenGrok deploy  
  
ADD run.sh /usr/local/bin/run  
CMD ["/usr/local/bin/run"]  
  
EXPOSE 8080  

