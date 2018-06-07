FROM debian:testing  
RUN sed -i "s/deb.debian.org/ftp.us.debian.org/" /etc/apt/sources.list  
RUN apt-get clean  
RUN apt-get -qq update  
RUN apt-get -qq install -y texlive-full wget biber python aspell aspell-en
aspell-nl git  

