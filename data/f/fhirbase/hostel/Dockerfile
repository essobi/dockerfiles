FROM ubuntu:14.04  
MAINTAINER Nikolay Ryzhikov <niquola@gmail.com>, Maksym Bodnarchuk
<bodnarchuk@gmail.com>  
  
RUN apt-get -qq update  
RUN apt-get install -qq -y software-properties-common curl  
RUN apt-get -qqy install git build-essential  
RUN add-apt-repository ppa:webupd8team/java && apt-get -qq update  
RUN echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN apt-get install -qq -y oracle-java7-installer  
RUN useradd -d /home/hostel -m -s /bin/bash hostel && echo
"hostel:hostel"|chpasswd && adduser hostel sudo  
  
RUN echo 'hostel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers  
  
USER hostel  
ENV HOME /home/hostel  
RUN cd /home/hostel && mkdir -p /home/hostel/bin && curl
https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein >
/home/hostel/bin/lein && chmod a+x /home/hostel/bin/lein  
RUN /home/hostel/bin/lein  
env PATH /home/hostel/bin:$PATH  
  
RUN sudo apt-get -qqy install nginx  
  
# All commands will rebuild each time above this line.  
COPY . /home/hostel/service  
RUN sudo chown -R hostel:hostel /home/hostel/service  
RUN cd ~/service && lein deps  
RUN cd ~/service && lein compile  
  
EXPOSE 80  
EXPOSE 8080  
CMD cd ~/service && lein run  

