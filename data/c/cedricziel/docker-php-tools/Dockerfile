FROM cedricziel/docker-php-tools:7.0  
  
# Install xvfb from scratch  
RUN DEBIAN_FRONTEND=noninteractive apt-get purge -y wkhtmltopdf \  
&& DEBIAN_FRONTEND=noninteractive apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y build-essential xorg
libssl-dev libxrender-dev wget gdebi xvfb \  
&& wget
https://bitbucket.org/wkhtmltopdf/wkhtmltopdf/downloads/wkhtmltox-0.13.0-alpha-7b36694_linux-
jessie-amd64.deb \  
&& DEBIAN_FRONTEND=noninteractive gdebi --n
wkhtmltox-0.13.0-alpha-7b36694_linux-jessie-amd64.deb \  
&& echo "xvfb-run -a -s \"-screen 0 640x480x16\" wkhtmltopdf \"\$@\"" >
/usr/local/bin/wkhtmltopdf-wrapper \  
&& chmod +x /usr/local/bin/wkhtmltopdf-wrapper \  
&& apt-get clean  

