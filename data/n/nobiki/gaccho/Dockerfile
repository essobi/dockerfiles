FROM debian:stretch  
MAINTAINER Naoaki Obiki  
RUN apt-get update && apt-get install -y python3 python3-pip git locales  
RUN apt-get install -y libncurses5 libncurses5-dev libncursesw5
libncursesw5-dev libreadline-dev pkg-config  
  
RUN locale-gen ja_JP.UTF-8 && localedef -f UTF-8 -i ja_JP ja_JP  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:jp  
ENV LC_ALL ja_JP.UTF-8  
RUN git clone "https://github.com/nobiki/gaccho.git" /usr/local/lib/gaccho  
  
RUN pip3 install git+https://github.com/nobiki/gaccho_rss.git  
#RUN pip3 install git+https://github.com/nobiki/gaccho_twitter.git  
CMD ["python3","/usr/local/lib/gaccho/gaccho.py"]  

