FROM ubuntu:14.04.5  
MAINTAINER lnterface "https://github.com/lnterface"  
ENV GOLANG_VERSION 1.4.2  
ENV GOLANG_SRC_URL https://github.com/gomini/go-mips32.git  
ENV GOOS linux  
ENV GOARCH mips32le  
ENV GOROOT /usr/local/go-mips32  
  
RUN apt-get update && \  
apt-get install -y openssh-server git file gcc openssl && \  
apt-get clean all  
  
RUN mkdir /var/run/sshd  
RUN echo 'root:toor' |chpasswd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
RUN cd /usr/local/ \  
&& git clone "$GOLANG_SRC_URL" go-mips32 \  
&& cd /usr/local/go-mips32/src \  
&& ./make.bash  
  
ENV GOPATH /go-mips32  
ENV PATH $GOPATH/bin:/usr/local/go-mips32/bin:$PATH  
  
RUN mkdir -p "$GOPATH/src" "$GOPATH/pkg" "$GOPATH/bin" && chmod -R 777
"$GOPATH"  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  

