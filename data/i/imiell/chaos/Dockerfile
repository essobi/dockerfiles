FROM ubuntu:14.04  
RUN apt-get update  
RUN apt-get install -y -qq python-pip git  
RUN pip install shutit #  
  
WORKDIR /opt  
RUN git clone https://github.com/ianmiell/shutit-library.git  
WORKDIR /opt/shutit-library/chaos  
RUN shutit build --delivery dockerfile  
  
CMD ["/root/work.sh"]  

