FROM debian:jessie  
MAINTAINER Pascal Maximilian Bremer <mail at pmbremer.de>  
ENV DEBIAN_FRONTEND noninteractive  
RUN REPO=http://cdn-fastly.deb.debian.org && \  
echo "deb $REPO/debian jessie main\ndeb $REPO/debian-security jessie/updates
main" > /etc/apt/sources.list && \  
apt-get -y update && \  
apt-get -y install locales git && \  
/usr/sbin/update-locale LANG=C.UTF-8 && \  
locale-gen C.UTF-8 && \  
apt-get remove -y locales && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
ENV LANG C.UTF-8  
ENV NLTK_DATA_ROOT /opt/nltk_data  
ENV PATH=/opt/conda/bin:$PATH  
RUN useradd -ms /bin/bash server  
  
#RUN mkdir /opt/conda && mkdir /opt/nltk_data  
RUN cd /home/server && \  
git clone https://github.com/TextyML/WebService.git data && \  
cd data && \  
rm -rf textyml && \  
git clone https://github.com/TextyML/texty.ml.git textyml-git && \  
mv textyml-git/Import textyml && rm -rf textyml-git && cd .. && \  
chown -R server:server data  
  
USER server  
WORKDIR /home/server/data  
EXPOSE 5555  
ENTRYPOINT ["python"]

