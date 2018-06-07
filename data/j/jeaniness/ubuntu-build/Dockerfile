FROM jeaniness/base:ubuntu  
MAINTAINER Jeanine Sinanan-Singh <jeanine@vitaeindustries.com>  
  
COPY . /src  
  
RUN make all  
  
FROM jeaniness/base:ubuntu  
  
COPY \--from=0 /usr/local/lib/ /usr/local/lib/  
  
ENV LD_LIBRARY_PATH=/usr/local/lib:${LD_LIBRARY_PATH}  
RUN /sbin/ldconfig  
  
CMD ["/bin/bash"]  

