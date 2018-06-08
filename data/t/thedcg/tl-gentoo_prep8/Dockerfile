################################  
# Dockerfile: thedcg/tl-gentoo_prep8:latest  
  
# ベース  
FROM thedcg/tl-gentoo_prep7:latest  
  
################################  
# prep8/Dockerfile  
  
# 管理者  
#MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>  
  
# パッケージ  
RUN date --iso-8601=ns\  
&& emerge\  
app-text/pdfjam\  
media-gfx/asymptote\  
dev-texlive/texlive-langcjk\  
dev-texlive/texlive-langjapanese\  
&& date --iso-8601=ns  
  
# 終了  

