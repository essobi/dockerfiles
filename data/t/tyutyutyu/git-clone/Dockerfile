FROM ubuntu  
MAINTAINER István Földházi "istvan.foldhazi@gmail.com"  
ENV REPO_URL "https://github.com/w3c/web-platform-tests"  
RUN apt-get update -y && apt-get upgrade -y  
RUN apt-get install -y \  
git \  
python \  
python-pip  
  
RUN pip install giturlparse.py  
  
RUN mkdir /root/.ssh/  
RUN chmod 700 /root/.ssh/  
  
COPY gethost.py /gethost.py  
COPY clone.sh /clone.sh  
  
VOLUME /root/.ssh/id_rsa  
VOLUME /repo  
  
ENTRYPOINT /clone.sh  

