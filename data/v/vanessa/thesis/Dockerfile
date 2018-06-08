FROM python:2.7  
MAINTAINER Vanessa Sochat <vsochat@gmail.com>  
  
RUN apt-get update --fix-missing -qq -y \  
&& apt-get install -y \  
texlive-latex-base \  
texlive-xetex \  
latex-xcolor \  
libopenblas-dev \  
build-essential \  
texlive-math-extra \  
texlive-latex-extra \  
texlive-fonts-extra \  
tex4ht \  
curl \  
wget \  
git \  
fontconfig \  
make \  
uuid-runtime \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install pokemon  
RUN pip install beautifulsoup4  
  
RUN mkdir /code  
WORKDIR /code  
ADD . /code/  
  
RUN chmod u+x /code/generate.sh  
CMD python /code/generate.py  
EXPOSE 3031  

