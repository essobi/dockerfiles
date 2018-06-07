FROM ubuntu:14.04.4  
MAINTAINER Eric Crosson (eric.s.crosson@utexas.edu)  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -qq && apt-get install -qq gdebi wget libgd2-xpm-dev make  
RUN wget -O $HOME/graphviz-2.38.0.deb \  
http://www.graphviz.org/pub/graphviz/stable/ubuntu/ub12.04/x86_64/graphviz_2.38.0-1~precise_amd64.deb  
RUN wget -O $HOME/libgraphviz4.deb \  
http://www.graphviz.org/pub/graphviz/stable/ubuntu/ub12.04/x86_64/libgraphviz4_2.38.0-1~precise_amd64.deb  
# RUN apt-get remove libcdt4 libpathplan4 libxdot4  
RUN wget -O libgd-xpm.deb
http://security.ubuntu.com/ubuntu/pool/main/libg/libgd2/libgd2-xpm_2.0.36~rc1~dfsg-6ubuntu2.1_amd64.deb  
RUN dpkg -i libgd-xpm.deb && apt-get install -f  
RUN yes | gdebi $HOME/libgraphviz4.deb  
RUN yes | gdebi $HOME/graphviz-2.38.0.deb  
  
WORKDIR /data  
  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

