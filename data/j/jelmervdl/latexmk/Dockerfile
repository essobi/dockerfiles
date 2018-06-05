FROM heichblatt/latexmk:latest  
MAINTAINER jelmervdl  
  
RUN /bin/dnf install -y \  
cairo \  
cairo-devel \  
cairomm-devel \  
libjpeg-turbo-devel \  
pango \  
pango-devel \  
pangomm \  
pangomm-devel \  
giflib-devel \  
nodejs\  
npm \  
&& /bin/dnf clean all  
  
RUN /bin/mkdir -pv /opt/hasl  
  
RUN /bin/dnf install -y gcc-c++ python \  
&& cd /opt/hasl \  
&& /usr/bin/npm install canvas \  
&& /bin/dnf erase -y gcc-c++ python  
  
RUN /bin/dnf install -y \  
texlive-tikz-qtree \  
texlive-pict2e \  
texlive-appendix \  
texlive-adjustbox \  
&& /bin/dnf clean all  
  
COPY hasl/*.js /opt/hasl/  
  
RUN /bin/chmod +x /opt/hasl/cli.js \  
&& /bin/ln -s /opt/hasl/cli.js /usr/bin/haslgraph  
  
RUN /bin/mkdir -pv /root/texmf/tex/latex  
  
COPY haslgraph.sty /root/texmf/tex/latex/  
  
COPY entrypoint.sh /usr/bin/local/  
RUN /bin/chmod +x /usr/bin/local/entrypoint.sh  
  
ENTRYPOINT ["/usr/bin/local/entrypoint.sh"]

