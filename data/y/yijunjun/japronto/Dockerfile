FROM centos:7  
MAINTAINER yijunjun "junjunyi@gmail.com"  
ENV LANG C.UTF-8  
ADD web /root/web  
  
ADD python3.6 /usr/local/python3.6  
  
EXPOSE 80  
CMD ["/usr/local/python3.6/bin/python"] ["/root/web/main.py"]  

