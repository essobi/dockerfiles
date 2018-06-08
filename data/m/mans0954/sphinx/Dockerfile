FROM debian:sid  
MAINTAINER christopher.hoskin@gmail.com  
  
# Install Tomcat  
RUN apt-get update && apt-get install -y python3-sphinx make
python3-sphinxcontrib.spelling python3-sphinxcontrib.plantuml latexmk plantuml
texlive-xetex texlive-latex-recommended  
  
RUN apt-get install fonts-freefont-ttf  
  
RUN mkdir /sphinx  
  
WORKDIR /sphinx  
  
ENTRYPOINT ["make"]  

