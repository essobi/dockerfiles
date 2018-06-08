FROM debian:latest  
  
RUN apt-get update && apt-get install --no-install-recommends --no-install-
suggests -y \  
daemontools \  
python3 \  
python3-pip \  
python3-setuptools \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY requirements.txt /  
#RUN pip3 install -U pip  
RUN pip3 install -r requirements.txt  
  
#optional: useful for in exec hacking:  
#RUN apt-get install -y --force-yes procps net-tools netcat-traditional git
vim mc && \  
#apt-get clean  
#ENV TERM xterm  
#setup here  
ENV APPNAME myapp  
ENV BASEDIR /www  
ENV APPPORT 8080  
ENV APPUID 1000  
ENV APPGID 1000  
ENV LOGUID 1001  
ENV LOGGID 1001  
RUN mkdir ${BASEDIR}  
COPY run-boot /  
COPY supervise /supervise/  
RUN mkdir /service && ln -s /supervise/gunicorn /service/gunicorn  
  
VOLUME [ ${BASEDIR} ]  
  
EXPOSE ${APPPORT}  
  
CMD /run-boot  

