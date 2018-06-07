FROM ubuntu:14.04  
RUN apt-get update  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-get -y install python-software-properties  
RUN apt-get -y install software-properties-common  
RUN apt-get -y install curl  
RUN add-apt-repository ppa:openjdk-r/ppa  
RUN apt-get update  
  
#NodeJS#  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get -y install nodejs  
  
#Redis#  
RUN sed -i "s/^exit 101$/exit 0/" /usr/sbin/policy-rc.d  
RUN apt-get -y install redis-server  
  
#Java#  
RUN apt-get -y install openjdk-8-jre  
  
#Neo4J#  
RUN apt-get -y install wget  
RUN wget -O - https://debian.neo4j.org/neotechnology.gpg.key | sudo apt-key
add -  
RUN echo 'deb https://debian.neo4j.org/repo stable/' | sudo tee
/etc/apt/sources.list.d/neo4j.list  
RUN apt-get update  
RUN apt-get -y install neo4j  
RUN usr/bin/neo4j-admin set-initial-password neo  
  
#R#  
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list  
RUN echo "deb http://ftp.iitm.ac.in/cran/bin/linux/ubuntu trusty/" >>
/etc/apt/sources.list  
RUN gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-key E084DAB9  
RUN gpg -a --export E084DAB9 | sudo apt-key add -  
RUN apt-get update  
RUN apt-get -y install r-base  
RUN apt-get -y install r-base-dev  
  
#R packages#  
RUN apt-get -y install build-essential libcurl4-gnutls-dev libxml2-dev libssl-
dev  
RUN su - -c "R -e \"install.packages('devtools',
repos='http://cran.rstudio.com/')\""  
RUN su - -c "R -e \"install.packages('rjson', repos =
'http://cran.rstudio.com/')\""  
RUN su - -c "R -e \"install.packages('shiny', repos =
'http://cran.rstudio.com/')\""  
RUN su - -c "R -e \"devtools::install_github('ropensci/plotly')\""  
RUN su - -c "R -e \"devtools::install_github('nicolewhite/RNeo4j')\""  
  
#Shiny Server#  
RUN apt-get -y install gdebi-core  
RUN wget https://download3.rstudio.org/ubuntu-12.04/x86_64/shiny-
server-1.5.3.838-amd64.deb  
RUN dpkg -i shiny-server-1.5.3.838-amd64.deb  
ADD ./config/shiny-server.conf /etc/shiny-server/shiny-server.conf  
  
ADD ./ ./code  
RUN chown -R neo4j:adm /var/lib/neo4j  
RUN chown shiny.shiny /  
RUN npm --prefix ./code install ./code  
RUN ["chmod", "+x", "./code/bin/initialize.sh"]  
  
ENTRYPOINT ["/code/bin/initialize.sh"]  
  
EXPOSE 8000  
EXPOSE 4000

