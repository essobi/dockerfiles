FROM debian:wheezy  
MAINTAINER Antoine Millet <antoine@inaps.org>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo "deb http://ftp.debian.org/debian wheezy-backports main" >>
/etc/apt/sources.list \  
&& apt-get -y -qq --force-yes update \  
&& apt-get -y -qq --force-yes install git curl python python-jinja2 nodejs
nodejs-legacy \  
&& apt-get clean  
  
RUN curl https://www.npmjs.com/install.sh | clean=yes sh  
  
ADD launcher.py /  
RUN chmod +x /launcher.py  
  
RUN git clone https://github.com/prawnsalad/KiwiIRC.git /kiwi  
ADD config.js.template /kiwi/  
RUN cd /kiwi/ && npm install  
RUN /kiwi/kiwi build  
  
RUN addgroup --quiet --system kiwi  
RUN adduser --home /kiwi --group --quiet --system kiwi  
  
RUN chown kiwi:kiwi -R /kiwi  
  
USER kiwi  
  
EXPOSE 7778  
CMD []  
ENTRYPOINT ["/launcher.py"]  

