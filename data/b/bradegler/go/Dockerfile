FROM bradegler/base  
  
ENV GOPATH /data  
ENV PATH
.:/data:/usr/local/go/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin  
  
RUN apt-get install -y build-essential mercurial subversion  
RUN wget -qO- http://golang.org/dl/go1.3.linux-amd64.tar.gz | tar -C
/usr/local -xzf -  
  
VOLUME /data  
  
CMD ["/bin/bash"]  

