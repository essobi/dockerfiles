FROM elixir:1.6.1  
RUN cd /tmp && wget
https://downloads.wkhtmltopdf.org/0.12/0.12.4/wkhtmltox-0.12.4_linux-generic-
amd64.tar.xz  
RUN cd /tmp && tar xf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz  
RUN mv /tmp/wkhtmltox /opt/  
RUN cd /usr/bin && ln -s /opt/wkhtmltox/bin/wkhtmltopdf  

