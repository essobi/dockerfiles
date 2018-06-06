FROM python:2  
MAINTAINER moooofly "special.agent@163.com"  
ENV VERSION=0.0.2  
RUN pip install docopt pygments appdirs  
  
WORKDIR /tmp  
RUN git clone https://github.com/moooofly/cheat.git  
  
WORKDIR /tmp/cheat  
RUN python setup.py install  
  
ENTRYPOINT ["cheat"]  
CMD ["-h"]  
  

