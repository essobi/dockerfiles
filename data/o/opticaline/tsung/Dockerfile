# Tsung  
#  
# VERSION 1.7.0  
FROM alpine:latest  
  
# install dependencies  
RUN apk --update add \  
alpine-sdk \  
erlang \  
erlang-ssl \  
erlang-dev \  
erlang-snmp \  
erlang-eunit \  
erlang-xmerl \  
erlang-inets \  
erlang-os-mon \  
erlang-crypto \  
gnuplot \  
bash \  
perl \  
perl-template-toolkit \  
# install tsung  
&& wget http://tsung.erlang-projects.org/dist/tsung-1.7.0.tar.gz \  
&& tar zvxf tsung-1.7.0.tar.gz \  
&& cd tsung-1.7.0/ \  
&& cd /tsung-1.7.0 \  
&& ./configure \  
&& make \  
&& make install \  
# clean up  
&& cd .. \  
&& rm -rf tsung-1.7.0.tar.gz tsung-1.7.0/ \  
&& apk del alpine-sdk \  
&& rm -rf /var/cache/apk/*  
  
VOLUME [ "/root/.tsung" ]  
  
# export web reports port  
EXPOSE 8091  
  
# run command  
CMD [ "tsung", "-k", "start" ]  

