FROM ubuntu:trusty  
MAINTAINER Mark Stillwell <mark@stillwell.me>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install \  
curl \  
git \  
python-bottle \  
supervisor && \  
curl -sL
http://download.opensuse.org/repositories/home:p_conrad:coins/xUbuntu_14.04/Release.key
| apt-key add - && \  
echo 'deb
http://download.opensuse.org/repositories/home:/p_conrad:/coins/xUbuntu_14.04/
/' > /etc/apt/sources.list.d/namecoin.list && \  
apt-get update && \  
apt-get -y install namecoin && \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN useradd -m -s /bin/bash namecoin  
  
WORKDIR /home/namecoin  
  
COPY run.sh ./run.sh  
COPY supervisord.conf ./supervisord.conf  
  
RUN chown -R namecoin:namecoin . && \  
chmod 755 ./run.sh && \  
chmod 644 ./supervisord.conf  
  
USER namecoin  
  
RUN git clone https://github.com/namecoin/nmcontrol.git  
  
VOLUME /home/namecoin  
  
EXPOSE 8053/udp 8336 9000  
CMD ["/home/namecoin/run.sh"]  

