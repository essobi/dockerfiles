FROM python:alpine  
MAINTAINER robin.roth@kit.edu  
  
RUN apk add --no-cache bash git openssh  
  
COPY flit.ini requirements.txt README.rst /hostlist/  
COPY hostlist /hostlist/hostlist  
COPY tests /hostlist/tests  
  
ENV FLIT_ROOT_INSTALL=1  
RUN pip install flit  
RUN cd /hostlist && \  
pip install -r requirements.txt && \  
flit install  
  
COPY docker/init.sh /  
  
ENV REPOURL=https://github.com/particleKIT/hostlist  
ENV REPODIR=tests  
ENV REPOSSHKEY=""  
ENV REPOHOSTKEY=""  
ENV SSLCERT=""  
ENV SSLPRIVATE=""  
ENV SSLCHAIN=""  
VOLUME /ssl  
  
EXPOSE 443  
WORKDIR /data  
  
ENTRYPOINT /init.sh  

