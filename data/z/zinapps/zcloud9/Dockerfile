FROM debian  
MAINTAINER Sarfaraz Ali Khan <mrkhan1417@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
python \  
python-pip \  
build-essential \  
nodejs \  
sshfs \  
git \  
curl  
  
RUN pip install virtualenv  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get install --yes nodejs  
  
RUN git clone git://github.com/c9/core.git c9sdk  
RUN /c9sdk/scripts/install-sdk.sh  
  
RUN mkdir /www  
ENV USERNAME admin  
ENV PASSWD cloud9  
ENV WORKDIR www  
  
EXPOSE 8181  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD ["bash", "/start.sh"]  

