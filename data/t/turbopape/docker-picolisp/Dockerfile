FROM gcc:latest  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get -y install apt-utils build-essential openjdk-7-jdk g++-multilib \  
&& ldconfig  
#RUN sudo adduser -D pil  
  
COPY ./picoLisp /usr/src/picoLisp  
  
WORKDIR /usr/src/picoLisp  
RUN make -C src64 \  
&& ln -s /usr/src/picoLisp /usr/lib/picolisp \  
&& ln -s /usr/lib/picolisp/bin/picolisp /usr/bin \  
&& ln -s /usr/lib/picolisp/bin/pil /usr/bin  
EXPOSE 8080  
#USER pil  
CMD [ "pil", "+" ]  

