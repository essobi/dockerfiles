FROM ubuntu:xenial  
  
RUN apt-get update \  
&& apt-get install -y \  
apt-transport-https \  
curl \  
ca-certificates \  
build-essential \  
gcc \  
git \  
libpq-dev \  
make \  
pkg-config \  
python3 \  
python3-dev \  
python3-pip \  
locales \  
&& apt-get autoremove -y \  
&& apt-get clean  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen  
RUN pip3 install --upgrade pip && pip3 install tox  
  
RUN mkdir /code  
WORKDIR /code  
ADD . /code/  
RUN pip3 install .  
RUN pip3 install git+https://github.com/dag4202/biasio-data.git  
  
ENV LC_ALL C.UTF-8  
ENV LANG C.UTF-8  
CMD ["biascollect"]

