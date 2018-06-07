FROM ubuntu:14.04  
MAINTAINER mopemope yutaka.matsubara@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN dpkg-divert --local \--rename --add /sbin/initctl && rm -f /sbin/initctl
&& ln -s /bin/true /sbin/initctl  
  
RUN apt-get -yq update  
  
RUN chmod go+w,u+s /tmp  
  
# Install required packages  
RUN apt-get -qy upgrade && apt-get -y install build-essential git python-pip
python-all-dev && apt-get clean  
  
RUN /bin/echo -e "LANG=\"ja_JP.UTF-8\"" > /etc/default/local \  
&& echo "Asia/Tokyo" > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata  
  
RUN pip install git+https://github.com/BrightcoveOS/Diamond.git psutil docker-
py  
RUN mkdir -p /diamond/storage  
ADD ./conf /diamond/  
ADD ./run_diamond /diamond/  
RUN chmod +x /diamond/run_diamond  
  
ENTRYPOINT ["/diamond/run_diamond"]  
#CMD "/bin/bash"  

