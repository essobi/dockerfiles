FROM asciidoctor/docker-asciidoctor  
MAINTAINER uochan  
  
RUN gem install asciidoctor-pdf-cjk-kai_gen_gothic --no-ri --no-rdoc && \  
gem install --version '0.12.7' compass --no-ri --no-rdoc && \  
gem install --version '4.3.2' zurb-foundation --no-ri --no-rdoc && \  
asciidoctor-pdf-cjk-kai_gen_gothic-install  
  
WORKDIR /root  
RUN wget -O VLGothic.zip
"http://osdn.jp/frs/redir.php?m=jaist&f=%2Fvlgothic%2F62375%2FVLGothic-20141206.zip"
&& \  
unzip VLGothic.zip && \  
mkdir -p /root/.fonts && \  
cp VLGothic/VL-Gothic-Regular.ttf /root/.fonts && \  
rm -rf /root/VLGothic*  
  
RUN wget https://github.com/asciidoctor/asciidoctor-stylesheet-
factory/archive/master.zip && \  
unzip master.zip && \  
cd asciidoctor-stylesheet-factory-master && \  
compass compile && \  
cp -pr stylesheets /  
  
WORKDIR /documents  

