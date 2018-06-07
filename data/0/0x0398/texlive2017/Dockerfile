FROM ubuntu:16.04  
MAINTAINER Jethro Van Thuyne <post@jethro.be>  
  
COPY ./scripts/cleanpdf /usr/bin/  
  
RUN apt-get update && \  
\  
\  
apt-get install -y --no-install-recommends wget perl ghostscript && \  
\  
\  
wget -L "http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz"
-O install.tl.tar.gz && \  
tar xzf install.tl.tar.gz && \  
cd install-tl-* && \  
\  
\  
echo "selected_scheme scheme-custom\n\  
TEXDIR /usr/local/texlive/2017\n\  
TEXMFCONFIG ~/.texlive2017/texmf-config\n\  
TEXMFHOME ~/texmf\n\  
TEXMFLOCAL /usr/local/texlive/texmf-local\n\  
TEXMFSYSCONFIG /usr/local/texlive/2017/texmf-config\n\  
TEXMFSYSVAR /usr/local/texlive/2017/texmf-var\n\  
TEXMFVAR ~/.texlive2017/texmf-var\n\  
binary_x86_64-linux 1\n\  
collection-basic 1\n\  
collection-latex 1\n\  
instopt_adjustpath 0\n\  
instopt_adjustrepo 1\n\  
instopt_letter 0\n\  
instopt_portable 0\n\  
instopt_write18_restricted 1\n\  
tlpdbopt_autobackup 1\n\  
tlpdbopt_backupdir tlpkg/backups\n\  
tlpdbopt_create_formats 1\n\  
tlpdbopt_desktop_integration 1\n\  
tlpdbopt_file_assocs 1\n\  
tlpdbopt_generate_updmap 0\n\  
tlpdbopt_install_docfiles 0\n\  
tlpdbopt_install_srcfiles 0\n\  
tlpdbopt_post_code 1\n\  
tlpdbopt_sys_bin /usr/bin\n\  
tlpdbopt_sys_info /usr/share/info\n\  
tlpdbopt_sys_man /usr/share/man\n\  
" >> install.profile && \  
\  
\  
./install-tl --profile install.profile && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr update --all && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install babel-french && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install ec && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install eurosym && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install fourier && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install fouriernc && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install graphviz && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install ncntrsbk && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install makecell && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install tabu && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install textpos && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install varwidth && \  
/usr/local/texlive/2017/bin/x86_64-linux/tlmgr install wrapfig && \  
\  
\  
apt-get autoremove && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists && \  
chmod +x /usr/bin/cleanpdf  
  
ENV PATH="/usr/local/texlive/2017/bin/x86_64-linux:${PATH}"  
  
VOLUME ["/data"]  

