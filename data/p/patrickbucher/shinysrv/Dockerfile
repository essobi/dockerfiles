FROM centos  
MAINTAINER Patrick Bucher "patrick.bucher@peax.ch"  
RUN ["rpm", "-Uvh", "https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm"]  
RUN ["yum", "-y", "install", "R", "wget", "git"]  
RUN ["yum", "-y", "clean", "all"]  
  
RUN ["R", "-e", "install.packages('shiny', repos='http://cran.rstudio.com/')"]  
RUN ["R", "-e", "install.packages('rmarkdown',
repos='http://cran.rstudio.com/')"]  
RUN ["R", "-e", "install.packages('DT', repos='http://cran.rstudio.com/')"]  
RUN ["wget", "https://download3.rstudio.org/centos5.9/x86_64/shiny-
server-1.5.3.838-rh5-x86_64.rpm"]  
RUN ["yum", "-y", "install", "--nogpgcheck", "shiny-
server-1.5.3.838-rh5-x86_64.rpm"]  
RUN ["rm", "shiny-server-1.5.3.838-rh5-x86_64.rpm"]  
  
RUN ["mkdir", "-p", "/srv/shiny-server"]  
RUN ["mkdir", "-p", "/var/log/shiny-server"]  
RUN ["mkdir", "-p", "/var/lib/shiny-server"]  
RUN ["chown", "-R", "shiny:shiny", "/srv/shiny-server"]  
RUN ["chown", "-R", "shiny:shiny", "/var/log/shiny-server"]  
RUN ["chown", "-R", "shiny:shiny", "/var/lib/shiny-server"]  
  
RUN ["ln", "-fs", "/usr/share/zoneinfo/Europe/Zurich", "/etc/localtime"]  
  
USER shiny:shiny  
RUN ["git", "clone", "https://github.com/patrickbucher/used-space.git",
"/srv/shiny-server/used-space"]  
CMD ["shiny-server"]  
  
EXPOSE 3838  

