FROM phusion/baseimage:0.9.14  
MAINTAINER Jason Kingsbury <jason@relva.co.uk>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9  
RUN echo 'deb http://mirrors.ebi.ac.uk/CRAN/bin/linux/ubuntu trusty/' >>
/etc/apt/sources.list  
  
RUN apt-get -q update  
RUN apt-get -y -qq install r-base gdebi-core wget r-base  
  
RUN mkdir -p /shiny /R/library /R/lib /system  
  
RUN R -e "install.packages('shiny', repos='http://cran.rstudio.com/')"  
RUN wget -O /tmp/shiny-server.deb
http://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-
server-1.4.0.721-amd64.deb  
RUN gdebi --option=APT::Get::force-yes=1,APT::Get::Assume-Yes=1 -n /tmp/shiny-
server.deb  
RUN rm /tmp/shiny-server.deb  
  
RUN ln -sf /dev/stdout /var/log/shiny-server.log  
  
EXPOSE 3838  
ADD shiny-server.conf /etc/shiny-server/  
ADD Renviron /etc/R/  
ADD ldpaths /etc/R/  
  
ADD init /system/init  
  
CMD ["/system/init"]  

