FROM jdeathe/centos-ssh:centos-7  
WORKDIR /root/  
ADD install-shadowsocks.sh /root/install-shadowsocks.sh  
RUN sh install-shadowsocks.sh  
  
RUN mkdir /root/kcptun  
  
ADD /kcptun/ /root/kcptun/  
#RUN yum -y install python36u python36u-pip  
RUN yum -y install python-pip  
ADD requirements.txt requirements.txt  
RUN pip install -r requirements.txt  
  
EXPOSE 8989  
EXPOSE 6688/udp  
EXPOSE 5000  
EXPOSE 22  
ENV SS_PASSWORD kexueshangwang  
  
ADD ss.conf /etc/supervisord.d/ss.conf  
ADD kcp.conf /etc/supervisord.d/kcp.conf  
ADD flask.conf /etc/supervisord.d/flask.conf  
  
ADD code /root/code  
  
RUN echo >> /etc/services-config/ssh/authorized_keys && \  
echo ssh-rsa
AAAAB3NzaC1yc2EAAAABIwAAAQEAuBVCr81bMAMRkdQMrJ6WR5+Za2uNexZs8Y4jZkRf1L6ninwoMMuuDv19EXs1SXQKPqFFq2DcMyZT1329ULKEMASVkmyJoYxEHNPjP8m2IkMs1B8VMVR6hN6isCDdHdj15Q6uSP1vn3YtZUsVl9SVXeZW6uYT5A0NXWkjUdX6OtXzjxSAyqwLt6F1FxAcOFoc2SDiA9Wzhm52Z68RwAGSZdxX6SMQEV2XSEF9Z35pvCMXEXjYAn+QhUdq5nSVBLNBks8d3cWEd2YhazpmcvLbwt1ArpBs4yR/hijze3Du7MF2lKBwdw/tALsckFyPgOqSh2dVv+Jg2qBERLVUMAyVzQ==
root@tvsrv01 >> /etc/services-config/ssh/authorized_keys  

