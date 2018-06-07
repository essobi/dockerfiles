FROM debian:8  
MAINTAINER Taylor "Nekroze" Lawson  
  
RUN apt-get update -y  
RUN apt-get install -y python git  
  
RUN git clone https://github.com/DobyTang/LazyLibrarian.git /lazylibrarian  
  
VOLUME /config  
  
EXPOSE 5299  
CMD python2 /lazylibrarian/LazyLibrarian.py --datadir /config  

