FROM alpine:3.3  
#SSH home and port. User is expected to expose a volume for SSH as /data/  
VOLUME ["/data/"]  
  
#FIXME: use these variables  
ENV USER=user  
#SSH PORT IS SET UP AS $PORT 0  
#ENV SSH_PORT=22  
ENV WEB_PORT=80  
ENV IPERF_TCP_PORT=5001  
ENV NETPERF_TCP_PORT=6001  
RUN apk add --update curl build-base bash iperf nmap nginx openssh rsync
tcpdump tshark iftop iptraf-ng && \  
#get netperf  
curl -LO ftp://ftp.netperf.org/netperf/netperf-2.7.0.tar.gz && \  
tar -xzf netperf-2.7.0.tar.gz && \  
cd netperf-2.7.0 && ./configure --prefix=/usr && make && make install && \  
rm -rf netperf-2.7.0 netperf-2.7.0.tar.gz && \  
rm -f /usr/share/info/netperf.info && \  
strip -s /usr/bin/netperf /usr/bin/netserver && \  
apk del curl build-base && rm -rf /var/cache/apk/* && \  
#SSH preparation  
adduser -D user -h /data/ && \  
#SSH keys  
mkdir -p user/.ssh && chmod 700 user/.ssh/ && \  
echo -e "Port 22\n" >> /etc/ssh/sshd_config && \  
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N '' && \  
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N '' && \  
echo -e "deleteme\ndeleteme" | passwd user && \  
#delete cache  
rm -rf /var/cache/apk/* netperf-2.7.0.tar.gz netperf-2.7.0  
#COPY SSH keys  
COPY user.pub $USER/.ssh/authorized_keys  
#EXPOSE $SSH_PORT  
EXPOSE 22  
#prepare content for nginx  
RUN mkdir -p /tmp/nginx/client-body  
COPY nginx/nginx.conf /etc/nginx/nginx.conf  
COPY nginx/default.conf /etc/nginx/conf.d/default.conf  
COPY website /usr/share/nginx/html  
  
#run nginx web server in $WEB_PORT  
RUN ["nginx"]  
EXPOSE 80  
#run iperf tcp server on port $IPERF_TCP_PORT (5001 default)  
RUN ["iperf", "-s", "-D", "-p 5001" ]  
EXPOSE 5001  
#run netperf tcp server on port $NETPERF_TCP_PORT (6001 default)  
RUN ["netserver", "-p 6001"]  
EXPOSE 6001  
COPY entry.sh /entry.sh  
RUN chmod 755 /entry.sh  
  
ENTRYPOINT ["/entry.sh"]  
  
CMD ["/usr/sbin/sshd", "-D"]  

