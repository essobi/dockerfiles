FROM dockerfile/nodejs  
  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y curl git htop man unzip vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Set locale  
RUN locale-gen fr_FR.UTF-8  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR:fr  
ENV LC_ALL fr_FR.UTF-8  
RUN apt-get update  
RUN apt-get install -y python-dev python-setuptools libxml2-dev python-lxml
libxslt-dev libz-dev python-sqlparse libjpeg8 libjpeg8-dev libfreetype6
libfreetype6-dev  
  
# Node things  
RUN npm install -g gulp  
RUN npm install -g bower  
  
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula
select true | sudo debconf-set-selections  
#RUN apt-get install ttf-mscorefonts-installer  
RUN apt-get install -y texlive  
RUN apt-get install -y texlive-xetex  
RUN apt-get install -y texlive-lang-french  
RUN apt-get install -y texlive-latex-extra  
RUN apt-get install -y pandoc  
  
RUN wget -P /usr/share/fonts/truetype
https://www.dropbox.com/s/ema28tjn52960mq/Merriweather.zip  
RUN unzip /usr/share/fonts/truetype/Merriweather.zip -d
/usr/share/fonts/truetype/Merriweather/  
RUN chmod a+r /usr/share/fonts/truetype/Merriweather/*.ttf  
# RUN fc-cache -f -v  
RUN mkdir -p ~/.pandoc  
RUN wget -P ~/.pandoc/templates
https://dl.dropboxusercontent.com/u/14517385/dev/default.epub  
RUN wget -P ~/.pandoc/templates
https://dl.dropboxusercontent.com/u/14517385/dev/default.html  
RUN touch ~/.pandoc/epub.css  
RUN touch ~/.pandoc/templates/epub.css  
RUN apt-get --reinstall install -qq language-pack-fr  
  
RUN apt-get -y install mysql-server  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
ADD ./startup.sh /opt/startup.sh  
  
EXPOSE 3306  
CMD ["/bin/bash", "/opt/startup.sh"]  

