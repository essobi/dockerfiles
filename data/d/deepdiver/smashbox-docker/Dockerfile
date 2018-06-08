FROM ubuntu:16.04  
# add ownCloud client  
ADD Release.key /  
RUN apt-key add - < Release.key  
RUN rm Release.key  
RUN echo 'deb
http://download.opensuse.org/repositories/isv:/ownCloud:/desktop/Ubuntu_16.04/
/' > /etc/apt/sources.list.d/owncloud-client.list  
  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y owncloud-client git python-pip curl  
  
RUN mkdir /smashbox  
RUN mkdir /root/smashdir  
  
WORKDIR /smashbox  
  
RUN git clone \--depth 1 https://github.com/owncloud/smashbox /smashbox  
RUN git checkout master  
  
RUN pip install -r requirements.txt  
  
ADD smashbox-docker.conf /smashbox/etc/smashbox.conf  
  
ADD run.sh /  
ENTRYPOINT ["/run.sh"]

