FROM gcc:4.9  
RUN apt-get update; apt-get install -qy texinfo  
RUN mkdir -p /opt/parallax  
COPY propeller-gcc /opt/src  
WORKDIR /opt/src  
RUN make  
CMD ["/opt/parallax/bin/gcc"]  

