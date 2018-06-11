FROM python:2  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get -y install \  
lynx \  
html2text \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists  
  
WORKDIR /work  
RUN pip install futures \  
&& git clone https://github.com/thp/urlwatch.git \  
&& cd urlwatch \  
&& python setup.py install \  
&& rm -rvf /root/.cache/ /work/urlwatch  
  
CMD urlwatch -v -c /work/cache/ --urls=/work/urls.txt --hooks=/work/hooks.py  
  

