FROM python:latest  
RUN git clone https://github.com/breakwa11/shadowsocks.git  
WORKDIR ./shadowsocks/  
RUN bash initcfg.sh  
WORKDIR ./shadowsocks/  
EXPOSE 8388  
CMD python server.py -k 888888 -o http_simple  

