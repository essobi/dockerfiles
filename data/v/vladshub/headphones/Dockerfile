FROM vladshub/python-virtualenv  
MAINTAINER Vladislav Shub <vlad6il@gmail.com>  
  
EXPOSE 8181  
ENV PYTHONIOENCODING "UTF-8"  
RUN virtualenv /env  
ENV HEADPHONES_VERSION "master"  
RUN git clone https://github.com/rembo10/headphones.git /headphones \  
&& cd /headphones \  
&& git checkout $HEADPHONES_VERSION  
  
WORKDIR /headphones  
  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  

