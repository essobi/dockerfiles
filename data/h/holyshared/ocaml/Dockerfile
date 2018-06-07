FROM ubuntu:18.04  
ENV DEBIAN_FRONTEND noninteractive  
ARG compiler_version="4.06.1"  
LABEL maintainer "Noritaka Horio <holy.shared.design@gmail.com>"  
RUN apt -y update && \  
apt -y install sudo m4 opam libssl-dev pkg-config && \  
rm -rf /var/lib/apt/lists/*  
RUN adduser --disabled-password --gecos "" develop && passwd -l develop  
ADD developsudo /etc/sudoers.d/develop  
RUN chmod 440 /etc/sudoers.d/develop && \  
chown root:root /etc/sudoers.d/develop && \  
chown -R develop:develop /home/develop  
USER develop  
ENV HOME /home/develop  
WORKDIR /home/develop  
RUN opam init -y && opam switch ${compiler_version} && opam install -y camlp4  
RUN echo "eval \\`opam config env\\`" >> ~/.bashrc  
RUN mkdir project  

