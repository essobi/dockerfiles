FROM jpetazzo/dind  
  
MAINTAINER Jesús Ángel González Novez <jesusgonzaleznovez@gmail.com>  
  
RUN apt-get update  
RUN apt-get install -y nodejs  
RUN apt-get install -y npm  
RUN echo 'alias node="nodejs"' >> ~/.bashrc  
RUN . ~/.bashrc  
  
RUN cd /home/ && git clone https://github.com/jesusgn90/Try-2-Learn  
  
RUN cd /home/Try-2-Learn && npm install  

