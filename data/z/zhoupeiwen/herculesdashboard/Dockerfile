FROM python:3.5  
ENV TZ Asia/Shanghai  
  
WORKDIR /app  
COPY ./requirements.txt /app  
RUN pip install -i http://pypi.douban.com/simple/ --trusted-host
pypi.douban.com -r requirements.txt  
COPY . /app  
  
#copy java env  
#ADD jdk-8u112-linux-x64.tar.gz /usr/local  
RUN wget -P /user/local http://download.oracle.com/otn-
pub/java/jdk/8u112-b15/jdk-8u112-linux-x64.tar.gz  
RUN tar -xvf /usr/local/jdk-8u112-linux-x64.tar.gz  
#copy chaintool src  
#ADD chaintool /usr/local/bin  
RUN wget -P /usr/local/bin https://github.com/hyperledger/fabric-
chaintool/releases/download/v0.9.0/chaintool  
RUN chmod +x /usr/local/bin/chaintool  
RUN mkdir -p /var/www/chaincodes  
ENV JAVA_HOME /usr/local/jdk1.8.0_112  
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar  
ENV PATH $PATH:$JAVA_HOME/bin  
  
#RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak  
#ADD sources.list /etc/apt/  
RUN apt-get update  
RUN apt-get install -y protobuf-compiler  
#ADD protobuf-3.1.0.tar.gz /usr/local  
#RUN apt-get update  
#RUN apt-get -y install autoconf automake libtool curl make g++ unzip  
#WORKDIR /usr/local/protobuf-3.1.0  
#RUN pwd  
#RUN ./autogen.sh  
#RUN ./configure  
#RUN make  
#RUN make check  
#RUN make install  
#RUN ldconfig  
RUN apt-get install golang  
RUN go get -u github.com/golang/protobuf/{proto,protoc-gen-go}  
  
WORKDIR /app  
  
#make chaintool  
CMD ["/usr/local/fabric-chaintool/MAKE INSTALL"]  
  
# use this in development  
CMD ["python", "dashboard.py"]  
  
# use this in product  
#CMD ["gunicorn", "-w", "128", "-b", "0.0.0.0:8080", "dashboard:app"]  

