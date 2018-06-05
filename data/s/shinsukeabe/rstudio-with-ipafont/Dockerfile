FROM rocker/rstudio:latest  
  
RUN wget -O IPAfont00303.zip
http://ipafont.ipa.go.jp/old/ipafont/IPAfont00303.php  
RUN unzip IPAfont00303.zip  
RUN mv IPAfont00303 /usr/share/fonts/truetype/  
RUN fc-cache  
  

