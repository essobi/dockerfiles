FROM ubuntu:15.10  
MAINTAINER m3talsmith <m3talsmith@gmail.com>  
  
RUN apt-get update > /dev/null &&\  
apt-get upgrade -y > /dev/null &&\  
apt-get install -y\  
build-essential\  
python-software-properties\  
git\  
imagemagick libmagickcore-dev libmagickwand-dev\  
libyaml-dev\  
libssl-dev\  
curl\  
wget\  
make\  
libwxgtk2.8-dev\  
> /dev/null  
  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
RUN mkdir /dbuild  
WORKDIR /dbuild  
RUN wget -q http://packages.erlang-solutions.com/site/esl/esl-
erlang/FLAVOUR_1_general/esl-erlang_18.1-1~ubuntu~wily_amd64.deb  
RUN dpkg -i esl-erlang_18.1-1~ubuntu~wily_amd64.deb > /dev/null  
RUN wget -q https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb  
RUN dpkg -i erlang-solutions_1.0_all.deb > /dev/null  
WORKDIR /  
RUN rm -rf /dbuild  
  
CMD ["erl"]  

