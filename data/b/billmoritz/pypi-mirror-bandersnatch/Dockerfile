FROM debian:stretch  
  
MAINTAINER Jan Losinski <losinski@wh2.tu-dresden.de>  
  
RUN apt-get update && \  
apt-get -y install --no-install-recommends \  
python3-dev \  
ca-certificates \  
python3-pip \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
pip3 install --upgrade virtualenv  
  
RUN groupadd user && \  
useradd --uid 1000 --create-home --home-dir /home/user -g user user  
  
WORKDIR /home/user  
  
RUN su user -c "/usr/local/bin/virtualenv ./bandersnatch-env && \  
. ./bandersnatch-env/bin/activate && \  
pip3 install -r
https://bitbucket.org/pypa/bandersnatch/raw/stable/requirements.txt"  
  
COPY default.conf /etc/bandersnatch.conf  
RUN chown user:user /etc/bandersnatch.conf  
  
COPY run.sh /usr/local/bin/run.sh  
  
VOLUME /srv/pypi  
CMD ["/usr/local/bin/run.sh"]  

