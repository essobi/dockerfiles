from ubuntu:14.04  
maintainer vivekdurai <vivek@humblepaper.com>  
  
# Build this Dockerfile and name the image 'docworker'  
RUN apt-get update && apt-get install --no-install-recommends -y \  
build-essential python-dev wget git python-pip \  
ca-certificates \  
curl \  
mercurial \  
git-core  
  
# install pdf2image  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
sudo apt-get -y install libfreetype6-dev && \  
wget --no-check-certificate
https://pdf2image.googlecode.com/files/pdf2image-0.53-source.tar.gz && \  
mkdir pdf2image && tar xf pdf2image-0.53-source.tar.gz -C pdf2image && cd
pdf2image && ./configure && make && make install && \  
apt-get install -y ghostscript  
  
RUN curl -s https://storage.googleapis.com/golang/go1.4.2.linux-amd64.tar.gz |
tar -v -C /usr/local -xz  
  
ENV GOPATH /gobranch  
ENV GOROOT /usr/local/go  
ENV PATH /usr/local/go/bin:/go/bin:/usr/local/bin:/gobranch/bin:$PATH  
  
#RUN export DEBIAN_FRONTEND=noninteractive && sudo apt-get -y install
libfreetype6-dev && apt-get install -y ghostscript apt-get install -y unzip  
  
#RUN wget --no-check-certificate
https://github.com/LaSanta/pdf2image/archive/master.zip && mkdir pdf2image &&
unzip master.zip -d pdf2image && cd pdf2image && ./configure && make && make
install  
  
# a few extras - install xhtml2pdf and pydocs  
#RUN pip install xhtml2pdf pydocx  

