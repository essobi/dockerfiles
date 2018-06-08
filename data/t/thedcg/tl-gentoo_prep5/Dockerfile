################################  
# Dockerfile: thedcg/tl-gentoo_prep5:latest  
  
# ベース  
FROM thedcg/tl-gentoo_prep4:latest  
  
################################  
# prep5/Dockerfile  
  
# 管理者  
#MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>  
  
# パッケージ  
  
RUN date --iso-8601=ns\  
&& emerge\  
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
&& date --iso-8601=ns  
  
# 終了  

