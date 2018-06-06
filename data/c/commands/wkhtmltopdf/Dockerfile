FROM debian  
MAINTAINER Ryuichi Tokugami  
  
RUN apt-get update; apt-get install -y wget xz-utils fontconfig libxrender1
libxext6 libx11-6 && \  
wget http://download.gna.org/wkhtmltopdf/0.12/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz && \  
tar Jxf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz && \  
cp -r wkhtmltox/bin/* /usr/bin/ ; cp -r wkhtmltox/lib/* /usr/lib/ ; cp -r
wkhtmltox/include/* /usr/include/ && \  
mkdir -p /usr/share/fonts/otf ; \  
wget https://github.com/adobe-fonts/source-han-
sans/raw/release/OTF/SourceHanSansJ.zip && \  
unzip SourceHanSansJ.zip ; mv SourceHanSansJ /usr/share/fonts/otf/ ; \  
wget https://github.com/adobe-fonts/source-han-
sans/raw/release/OTF/SourceHanSansHWJ.zip && \  
unzip SourceHanSansHWJ.zip ; mv SourceHanSansHWJ /usr/share/fonts/otf/ ; \  
wget https://github.com/adobe-fonts/source-han-
sans/raw/release/SubsetOTF/SourceHanSansJP.zip && \  
unzip SourceHanSansJP.zip ; mv SourceHanSansJP /usr/share/fonts/otf/ ; \  
rm -f SourceHanSans*; fc-cache j; rm -rf /wkhtml* ; \  
apt-get --purge remove wget xz-utils ; rm -rf /var/lib/apt/lists/*  
  
WORKDIR /data  
ENTRYPOINT ["/usr/local/bin/wkhtmltopdf"]  
CMD ["-h"]  

