FROM fedora:latest  
MAINTAINER Genadi Postrilko <genadipost@gmail.com>  
  
RUN dnf install -y python-sphinx \  
texlive-cm texlive-ec texlive-times texlive-helvetic texlive-courier \  
texlive-cmap texlive-fancyhdr texlive-fancybox texlive-titlesec texlive-framed
texlive-threeparttable texlive-babel-english \  
texlive-mdwtools texlive-wrapfig texlive-parskip texlive-upquote texlive-capt-
of texlive-multirow texlive-eqparbox texlive-dvips \  
texlive-mfware-bin texlive-gsftopk-bin \  
gcc \  
automake \  
openssl-devel \  
git \  
httpd  
  
RUN git clone https://github.com/acassen/keepalived \  
&& cd keepalived \  
&& ./configure \  
&& make html \  
&& rm -rf /var/www/html \  
&& ln -s /keepalived/doc/build/html /var/www/html  
  
EXPOSE 80  
CMD apachectl -DFOREGROUND  

