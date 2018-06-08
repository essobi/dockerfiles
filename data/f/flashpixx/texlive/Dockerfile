FROM alpine:latest  
  
  
# --- configuration section ----------------------  
ENV DOCKERIMAGE_GLIBC_VERSION 2.26-r0  
ENV DOCKERIMAGE_INSTALLATIONSCHEME full  
  
  
# --- dependencies / installation section --------  
RUN wget -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub  
RUN wget -O /tmp/glibc.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$DOCKERIMAGE_GLIBC_VERSION/glibc-$DOCKERIMAGE_GLIBC_VERSION.apk  
RUN wget -O /tmp/glibc-bin.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$DOCKERIMAGE_GLIBC_VERSION/glibc-
bin-$DOCKERIMAGE_GLIBC_VERSION.apk  
RUN wget -O /tmp/glibc-i18n.apk https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/$DOCKERIMAGE_GLIBC_VERSION/glibc-i18n-$DOCKERIMAGE_GLIBC_VERSION.apk  
  
RUN apk --no-cache update &&\  
apk --no-cache upgrade &&\  
apk --no-cache add ca-certificates /tmp/glibc.apk /tmp/glibc-bin.apk
/tmp/glibc-i18n.apk musl-dev curl wget git openssh-client gnupg perl go  
  
RUN /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8  
RUN go get -u github.com/tcnksm/ghr  
  
RUN mkdir -p /tmp/tex && curl -L
http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz | tar xz
--strip 1 -C /tmp/tex;  
  
RUN echo -e "selected_scheme scheme-$DOCKERIMAGE_INSTALLATIONSCHEME\\nTEXDIR
/usr/local/texlive/\\nTEXMFLOCAL /usr/local/texlive/texmf-
local\\nTEXMFSYSCONFIG /usr/local/texlive/texmf-config\\nTEXMFSYSVAR
/usr/local/texlive/texmf-var\\nTEXMFHOME /root/texmf\nTEXMFCONFIG
/root/.texlive/texmf-config\\nTEXMFVAR /root/.texlive/texmf-
var\\nbinary_x86_64-linux 1\\ninstopt_adjustpath 1\\ninstopt_adjustrepo
1\\ninstopt_letter 1\\ninstopt_portable 0\\ninstopt_write18_restricted
1\\ntlpdbopt_autobackup 1\\ntlpdbopt_backupdir
tlpkg/backups\\ntlpdbopt_create_formats 1\\ntlpdbopt_desktop_integration
0\\ntlpdbopt_file_assocs 1\\ntlpdbopt_generate_updmap
0\\ntlpdbopt_install_docfiles 0\\ntlpdbopt_install_srcfiles
0\\ntlpdbopt_post_code 1\\ntlpdbopt_sys_bin /tmp\\ntlpdbopt_sys_info
/tmp\\ntlpdbopt_sys_man /tmp\\ntlpdbopt_w32_multi_user 1\\n" >
/tmp/texinstall.profile; /tmp/tex/install-tl -profile /tmp/texinstall.profile;  
RUN echo -e "\$pdf_mode = 1;\\n\$bibtex_use = 2;\\n\$pdflatex = 'pdflatex
-halt-on-error -file-line-error -shell-escape -interaction=nonstopmode
-synctex=1 %O %S';\\n\$clean_ext = 'synctex.gz synctex.gz(busy) run.xml xmpi
acn acr alg glsdefs vrb bbl ist glg glo gls ist lol log 1 dpth auxlock
%R-figure*.* %R-blx.bib snm nav dvi xmpi tdo';\\n\\nadd_cus_dep('glo', 'gls',
0, 'makeglossaries');\\nadd_cus_dep('acn', 'acr', 0,
'makeglossaries');\\nadd_cus_dep('mp', '1', 0, 'mpost');\\n\\nsub
makeglossaries {\\nreturn system('makeglossaries', \$_[0]);\\n}\\n\\nsub mpost
{\\nmy (\$name, \$path) = fileparse( \$_[0] );\\nmy \$return = system('mpost',
\$_[0]);\\nif ( (\$path ne '') && (\$path ne '.\\\\\\\\') && (\$path ne './')
) {\\nforeach ( '\$name.1', '\$name.log' ) { move \$_, \$path; }\\n}\\nreturn
\$return;\\n}\\n" > /root/.latexmkrc  
  
  
# --- machine configuration section --------------  
ENV TEXMFHOME /root/texmf  
ENV PATH /usr/local/texlive/bin/x86_64-linux:/root/go/bin:$PATH  
RUN tlmgr update --self --all --reinstall-forcibly-removed  
  
RUN rm -rf /tmp/*  

