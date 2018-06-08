FROM ubuntu  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN apt-add-repository ppa:ansible/ansible  
RUN apt-get update && apt-get install -y wget build-essential libboost-all-dev
gperf libevent-dev uuid-dev  
RUN apt-get install -y ansible  
  
WORKDIR /tmp  
RUN wget
https://github.com/gearman/gearmand/releases/download/1.1.15/gearmand-1.1.15.tar.gz  
RUN tar xvzf gearmand-1.1.15.tar.gz  
  
WORKDIR /tmp/gearmand-1.1.15  
RUN ./configure  
RUN make && make install  
RUN LD_LIBRARY_PATH=/usr/local/lib ldconfig  
  
WORKDIR /tmp  
RUN mkdir -p /root/.ssh  
RUN echo "Host bitbucket.org\n\tStrictHostKeyChecking no\n" >>
/root/.ssh/config  
RUN echo "Host *.unblockr.net\n\tStrictHostKeyChecking no\n" >>
/root/.ssh/config  
  
RUN rm -rf /tmp/gearmand-1.1.15.tar.gz /tmp/gearmand-1.1.15  
  
RUN apt-get install -y git  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.2.0/dumb-
init_1.2.0_amd64.deb  
RUN dpkg -i dumb-init_*.deb  
  
RUN apt-get install -y curl  
RUN git clone https://github.com/course-hero/slacktee.git  
  
RUN apt-get install -y jq  
  
COPY slacktee.conf /root/.slacktee  
RUN ./slacktee/install.sh /usr/bin  
  
COPY bin /usr/local/bin/  
COPY slacktee.conf /etc/slacktee.conf  
  
CMD [ gearmand ]  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
  
EXPOSE 4730  

