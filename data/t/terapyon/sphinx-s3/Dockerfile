FROM ruby:2.2  
MAINTAINER "Manabu TERADA" <terada@cmscom.jp>  
  
RUN apt-get update -y  
RUN apt-get install -y default-jre  
RUN gem install s3_website jekyll jekyll-time-to-read  
  
RUN apt-get install -y build-essential  
RUN apt-get install -y python3  
RUN apt-get install -y python3-dev  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python3 get-pip.py  
RUN pip install virtualenv  
COPY requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
#CMD ["/bin/bash"]  

