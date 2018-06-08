FROM debian:wheezy  
  
MAINTAINER Kevin Li <mlf4aiur@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y -q --no-install-recommends \  
python \  
ipython-notebook \  
python-pandas \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME /notebooks  
WORKDIR /notebooks  
  
EXPOSE 8888  
# You can mount your own SSL certs as necessary here  
ENV PEM_FILE /key.pem  
# $PASSWORD will get `unset` within notebook.sh, turned into an IPython style
hash  
ENV PASSWORD Dont make this your default  
ENV USE_HTTP 0  
ADD notebook.sh /  
RUN chmod u+x /notebook.sh  
  
CMD ["/notebook.sh"]  

