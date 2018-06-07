# OCR Dockerfilie  
FROM debian:jessie  
  
RUN apt-get update  
RUN apt-get install -y \  
git \  
vim \  
python \  
curl \  
ruby \  
vim  
RUN apt-get install -y pdftk \  
poppler-utils \  
tesseract-ocr \  
exactimage \  
mercurial  
  
# Setup Disk  
RUN mkdir /opt/ocr/  
  
####################  
## Install pdfocr ##  
####################  
  
WORKDIR /opt/ocr/  
RUN curl -LkSs https://api.github.com/repos/gkovacs/pdfocr/tarball -o
master.tar.gz  
RUN tar -xvzf master.tar.gz  
RUN rm master.tar.gz  
RUN mv gkovacs* pdfocr  
  
################  
# Install Ruby #  
################  
  
# Install rvm  
RUN apt-get install -y ps-watcher  
RUN curl -L https://get.rvm.io | bash -s stable  
  
# Install package dependencies  
RUN /usr/local/rvm/bin/rvm requirements  
  
# Install ruby  
RUN /usr/local/rvm/bin/rvm install ruby-2.1.1  
  
# Set the version # with an rvm wrapper  
RUN /usr/local/rvm/bin/rvm wrapper ruby-2.1.1 \--no-prefix bundle ruby gem  
  
###################  
# Install the App #  
###################  
RUN ls  
RUN git clone https://github.com/witoff/DistributedOcr.git /opt/ocr/main  
RUN /usr/local/rvm/bin/bundle install
--gemfile=/opt/ocr/main/container_ocr/Gemfile  
  
#######  
# RUN #  
#######  
  
CMD ["/usr/local/rvm/bin/ruby", "/opt/ocr/main/container_ocr/main.rb"]  

