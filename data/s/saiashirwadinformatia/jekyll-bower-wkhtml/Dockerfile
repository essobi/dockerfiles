# Ruby-Node based image with Jekyll-Bower support  
FROM saiashirwadinformatia/jekyll-bower:latest  
MAINTAINER Rohan Sakhale <rs@saiashirwad.com>  
  
RUN wget
http://download.gna.org/wkhtmltopdf/0.12/0.12.3/wkhtmltox-0.12.3_linux-
generic-amd64.tar.xz \  
&& tar xvf wkhtmltox-0.12.3_linux-generic-amd64.tar.xz \  
&& chmod +x wkhtmltox/bin/wkhtmltopdf \  
&& chmod +x wkhtmltox/bin/wkhtmltoimage \  
&& mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf \  
&& mv wkhtmltox/bin/wkhtmltoimage /usr/local/bin/wkhtmltoimage \  
&& rm -rf wkhtmltox*  
  
CMD ["wkhtmltopdf", "wkhtmltoimage"]

