# Test env for Ryu SDN Framework  
#  
FROM ubuntu:15.04  
MAINTAINER FUJITA Tomonori <fujita.tomonori@lab.ntt.co.jp>  
  
RUN apt-get update  
RUN apt-get install -qy --no-install-recommends wget python git  
#RUN apt-get build-dep -qy --no-install-recommends python  
RUN apt-get install -qy ca-certificates  
  
RUN apt-get install -qy --no-install-recommends libreadline-dev zlib1g-dev
libbz2-dev libssl-dev libsqlite3-dev gcc build-essential python-dev
libxml2-dev libxslt1-dev python3-dev  
  
RUN apt-get install -qy --no-install-recommends bash-completion emacs24-nox
iproute2  
  
ENV HOME /root  
WORKDIR /root  
  
RUN wget -O - https://bootstrap.pypa.io/get-pip.py | python  
RUN git clone https://github.com/yyuu/pyenv.git ~/.pyenv  
  
ENV PYENV_ROOT /root/.pyenv  
ENV PATH $PYENV_ROOT/bin:$PATH  
  
RUN echo 'eval "$(pyenv init -)"' >> ~/.bash_profile  
RUN . /root/.bash_profile  
RUN echo "source .bash_profile" >> ~/.bashrc  
  
RUN pyenv install 2.6.9  
RUN pyenv install 2.7.11  
RUN pyenv install 3.4.4  
ADD version /root/.pyenv/version  
  
RUN pip install nose  
RUN pip install virtualenv  
RUN pip install tox  
  
RUN git clone https://github.com/osrg/ryu  

