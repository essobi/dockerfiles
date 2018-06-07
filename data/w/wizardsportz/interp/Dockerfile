FROM gcc:latest  
MAINTAINER Luke Patmore <nq9l.patmore@gmail.com>  
COPY . /usr/src/wizardlisp  
WORKDIR /usr/src/wizardlisp  
RUN make  
RUN make clean  
CMD ["./wizardlisp"]  

