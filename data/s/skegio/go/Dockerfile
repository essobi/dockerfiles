FROM skegio/base  
  
RUN apt-get update && apt-get install gcc -y  
RUN curl https://storage.googleapis.com/golang/go1.6.4.linux-amd64.tar.gz |
tar -C /usr/local -xzf -  
ENV PATH $PATH:/usr/local/go/bin  
  
# set up environment  
RUN echo "export GOPATH=\$HOME/go\nexport
PATH=\$PATH:/usr/local/go/bin:\$GOPATH/bin\n" > /etc/profile.d/go.sh  

