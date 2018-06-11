FROM debian  
RUN echo "nameserver 8.8.8.8" | tee /etc/resolv.conf > /dev/null  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y --force-yes build-essential autoconf libtool libssl-dev
curl python-pip git python-m2crypto  
RUN pip install cymysql  
RUN mkdir /myapp  
RUN git clone -b manyuser https://github.com/watsy0007/shadowsocks.git
/myapp/shadowsocks  
RUN sed -i 's/mdss.mengsky.net/os.environ["MYSQL_HOST"]/'
/myapp/shadowsocks/shadowsocks/Config.py  
RUN sed -i '3s/3306/os.environ["MYSQL_PORT"]/'
/myapp/shadowsocks/shadowsocks/Config.py  
RUN sed -i '4s/ss/os.environ["MYSQL_USER"]/'
/myapp/shadowsocks/shadowsocks/Config.py  
RUN sed -i '5s/ss/os.environ["MYSQL_PASS"]/'
/myapp/shadowsocks/shadowsocks/Config.py  
RUN sed -i '6s/shadowsocks/os.environ["MYSQL_DB"]/'
/myapp/shadowsocks/shadowsocks/Config.py  
RUN sed -i '8s/ss233333333/os.environ["MANAGE_PASS"]/'
/myapp/shadowsocks/shadowsocks/Config.py  
RUN sed -i '2,8s/\x27/ /g' /myapp/shadowsocks/shadowsocks/Config.py  
RUN sed -i '2 i import os' /myapp/shadowsocks/shadowsocks/Config.py  
RUN sed -i 's/rc4-md5/aes-256-cfb/g'
/myapp/shadowsocks/shadowsocks/config.json  
RUN echo "cd /myapp/shadowsocks/shadowsocks && python server.py && echo
'starting...'" > /myapp/shadowsocks/shadowsocks/start.sh  
WORKDIR /myapp  
EXPOSE 50000  
CMD ["bash", "/myapp/shadowsocks/shadowsocks/start.sh"]  

