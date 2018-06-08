################################  
# Dockerfile: thedcg/tl-gentoo_prep1:latest  
  
# ベース  
FROM thedcg/gentoo-llvm:latest  
  
################################  
# prep1/Dockerfile  
  
# 管理者  
#MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>  
  
# パッケージ  
  
RUN date --iso-8601=ns;\  
/usr/bin/env CONFIG_PROTECT_MASK="/etc"\  
emerge --autounmask-write --verbose-conflicts\  
dev-vcs/git\  
perl-core/Encode\  
dev-perl/JSON\  
app-arch/zip\  
app-text/dos2unix\  
# net-misc/curl\  
app-text/texlive\  
dev-texlive/texlive-fontsrecommended\  
dev-texlive/texlive-fontsextra\  
dev-texlive/texlive-science\  
dev-texlive/texlive-latex\  
dev-texlive/texlive-latexrecommended\  
dev-texlive/texlive-latexextra\  
dev-texlive/texlive-pictures\  
dev-texlive/texlive-metapost\  
dev-texlive/texlive-bibtexextra\  
dev-texlive/texlive-langcjk\  
dev-texlive/texlive-langjapanese\  
app-text/pdfjam\  
media-gfx/asymptote\  
; date --iso-8601=ns; exit 0  
  
#RUN date --iso-8601=ns\  
# && emerge --update --newuse --deep @world\  
# && emerge --update --changed-use --deep @world\  
# && date --iso-8601=ns  
  
#RUN date --iso-8601=ns\  
# && emerge --depclean\  
# && date --iso-8601=ns  
  
# 終了  

