# Base docker image  
FROM ubuntu:16.04  
# LABEL maintainer "Kenneth Tse <fuckgfw@linux.com>"  
RUN apt-get update -y  
RUN apt-get install python3-pip -y  
RUN pip3 install shadowsocks  
  
RUN apt-get install wget -y  
RUN wget https://github.com/xtaci/kcptun/releases -O - 2>/dev/null | grep
kcptun-linux-amd64- | grep "a href" | sort | tail -1 | awk -F '"' '{print $2}'
| { read uri; wget "https://github.com${uri}" -O /tmp/kcptun.tar.gz -c -t 0; }  
RUN mkdir /usr/local/kcptun -p  
RUN tar xzvf /tmp/kcptun.tar.gz -C /usr/local/kcptun  
RUN chown 0:0 /usr/local/kcptun/*  
  
# start script  
ARG CLIENT_SCRIPT=/usr/local/bin/fuckgfw_client.sh  
ARG SERVER_SCRIPT=/usr/local/bin/fuckgfw_server.sh  
RUN touch $CLIENT_SCRIPT  
  
# client script  
RUN touch $CLIENT_SCRIPT  
RUN echo "#!/bin/bash" >> $CLIENT_SCRIPT  
# #1:kcp_server #2:kcp_port kcp_#3:ss_port #4:kcp_mode  
# #5:ss_mode #6:ss_password #7:proxy_port  
RUN echo "nohup /usr/local/kcptun/client_linux_amd64 -r \$1:\$2 -l :\$3 -mode
\$4 > /tmp/kcp.log 2>&1 &" >> $CLIENT_SCRIPT  
RUN echo "nohup /usr/local/bin/sslocal -s 127.0.0.1 -p \$3 -b 0.0.0.0 -l \$7
-m \$5 -k \$6 --pid-file /tmp/ss.pid > /tmp/ss.log 2>&1 &" >> $CLIENT_SCRIPT  
RUN echo "while true; do sleep 3600; done" >> $CLIENT_SCRIPT  
RUN chmod +x $CLIENT_SCRIPT  
  
# server script  
RUN touch $SERVER_SCRIPT  
RUN echo "#!/bin/bash" >> $SERVER_SCRIPT  
# #1:ss_password #2:kcp_port  
RUN echo "nohup /usr/local/bin/ssserver -s 127.0.0.1 -p 9527 -m aes-256-cfb -k
\$1 --workers 4 --pid-file /tmp/ss.pid > /tmp/ss.log 2>&1 &" >> $SERVER_SCRIPT  
RUN echo "nohup /usr/local/kcptun/server_linux_amd64 -t 127.0.0.1:9527 -l :\$2
-mode fast2 > /tmp/kcp.log 2>&1 &" >> $SERVER_SCRIPT  
RUN echo "while true; do sleep 3600; done" >> $SERVER_SCRIPT  
RUN chmod +x $SERVER_SCRIPT  
  
ENV REMOTE_SERVER 0.0.0.0  
ENV KCP_LISTEN_PORT 9528  
ENV KCP_MODE fast2  
ENV SS_LISTEN_PORT 9527  
ENV SS_MODE aes-256-cfb  
ENV SS_PASSWORD password  
ENV PROXY_PORT 1080  
RUN apt-get purge --auto-remove -y wget  
RUN rm -rf /tmp/kcp* /var/cache/apk/*  
  
CMD /usr/local/bin/fuckgfw_client.sh $REMOTE_SERVER $KCP_LISTEN_PORT
$SS_LISTEN_PORT $KCP_MODE $SS_MODE $SS_PASSWORD $PROXY_PORT  
  

