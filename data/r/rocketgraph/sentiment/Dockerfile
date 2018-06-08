#  
# Rocketgraph NLP  
#  
# Pull base image.  
FROM rocketgraph/python  
  
MAINTAINER Konstantinos Christofilos <kostas.christofilos@rocketgraph.com>  
  
# Install packages  
RUN apt-get -y update &&\  
apt-get -y upgrade &&\  
apt-get -y install supervisor libhunspell-dev  
  
ADD ./supervisord.conf /etc/supervisor/supervisord.conf  
  
#Install Flask  
RUN pip install --user Flask  
  
#Install hunspell  
RUN pip install --user hunspell  
  
#Install textblob  
RUN pip install -U textblob  
RUN pip install -U textblob-de  
RUN pip install -U textblob-fr  
  
RUN python -m textblob.download_corpora  
  
EXPOSE 9876  
  
CMD ["supervisord", "-n"]  

