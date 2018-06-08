FROM ubuntu:16.04  
MAINTAINER sfcklx, simolx@163.com  
  
ENV SAGE_VERSION 7.5.1  
ENV SAGE_ROOT /home/sage/sage-$SAGE_VERSION  
  
VOLUME [/home/sage/notebook_data]  
RUN apt-get update -y && apt-get install -y binutils gcc make m4 perl tar git
dvipng ffmpeg imagemagick texlive libssl1.0.0 libssl-dev openssh-server
openssh-client tk tk-dev autoconf  
RUN mkdir /home/sage && useradd -d /home/sage sage && chown -R sage:sage
/home/sage  
USER sage  
RUN git clone \--branch ${SAGE_VERSION} \--depth 1
https://github.com/sagemath/sage.git $SAGE_ROOT  
WORKDIR $SAGE_ROOT  
RUN ./sage -f python2  
RUN make  
EXPOSE 8080  
EXPOSE 22  
CMD [ "sh", "-c", "$SAGE_ROOT/sage" ]  

