################################  
# Dockerfile: thedcg/tl-gentoo_prep4:latest  
  
# ベース  
FROM thedcg/tl-gentoo_prep3:latest  
  
################################  
# prep4/Dockerfile  
  
# 管理者  
#MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>  
  
# パッケージ  
RUN date --iso-8601=ns\  
&& emerge\  
dev-vcs/git\  
app-arch/zip\  
app-text/dos2unix\  
perl-core/Encode\  
dev-perl/JSON\  
# net-misc/curl\  
&& date --iso-8601=ns  
  
# 終了  

