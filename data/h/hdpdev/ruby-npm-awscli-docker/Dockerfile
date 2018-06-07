FROM circleci/ruby:2.5.1-node  
  
# installations command expect to run as root  
USER root  
  
RUN apt-get update \  
&& apt-get install -y \  
fonts-ipafont-gothic \  
fonts-ipafont-mincho \  
libxslt1-dev \  
libxml2-dev \  
libxmlsec1-dev \  
libxmlsec1-openssl \  
xmlsec1 \  
imagemagick \  
python3-dev \  
python3-setuptools \  
python3-pip \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install awscli --upgrade --user  
  
ENV PATH ~/.local/bin:$PATH  
  
CMD [ "irb" ]  

