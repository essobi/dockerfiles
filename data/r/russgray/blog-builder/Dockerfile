FROM ubuntu  
  
RUN apt-get update \  
&& apt-get -y upgrade \  
&& apt-get -y install \  
build-essential \  
git \  
libffi-dev \  
libpython2.7-dev \  
libssl-dev \  
libxml2-dev \  
libxslt1-dev \  
linklint \  
moreutils \  
pandoc \  
python-dev \  
python-pip \  
zlib1g-dev \  
&& apt-get clean  
  
RUN rm -rf /var/lib/apt/lists/*  
  
RUN pip install --upgrade pip markdown pelican requests  
  
RUN git clone https://github.com/getpelican/pelican-plugins.git /opt/pelican-
plugins  
RUN git clone https://github.com/drbunsen/formd.git /opt/formd  
  
RUN pip install git+git://github.com/bstpierre/pelican-
comments#egg=pelican_comments  
  
RUN mkdir /pelican  
ADD ./requirements.txt /pelican/requirements.txt  
RUN pip install -r /pelican/requirements.txt  
  
ADD
https://gist.githubusercontent.com/russgray/e65eadcafb89bdf6cb41adb74fa2ada9/raw/23d9d075462a45bed57eec173bbc5dfeb7d4ebd7/subscript.py
/usr/local/lib/python2.7/dist-packages/markdown/extensions/subscript.py  
  
WORKDIR /blog  

