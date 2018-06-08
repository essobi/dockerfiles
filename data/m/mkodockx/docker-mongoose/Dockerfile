FROM ubuntu:trusty  
MAINTAINER https://m-ko-x.de Markus Kosmal <code@m-ko-x.de>  
  
ENV TARGET_HOST localhost  
  
RUN apt-get update -yqq \  
&& apt-get install -yqq nano wget curl  
  
RUN mkdir -p /tmp/erlang \  
&& cd /tmp/erlang \  
&& wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb \  
&& sudo dpkg -i erlang-solutions_1.0_all.deb  
  
RUN apt-get update -yqq \  
&& apt-get install -yqq mongooseim  
  
EXPOSE 5222 5280 5269  
  
RUN sed -i 's/\\["localhost"\\]/\\["${TARGET_HOST}"\\]/g'
/usr/lib/mongooseim/etc/ejabberd.cfg  
  
CMD /usr/lib/mongooseim/bin/mongooseim console -noshell  

