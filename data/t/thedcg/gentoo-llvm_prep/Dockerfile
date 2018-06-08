################################  
# Dockerfile: thedcg/gentoo-llvm_prep:latest  
  
# ベース  
FROM thedcg/gentoo:latest  
  
################################  
# prep/Dockerfile  
  
# 管理者  
#MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>  
  
# アップデート  
RUN date --iso-8601=ns\  
&& emerge\  
dev-util/re2c\  
dev-util/ninja\  
net-misc/curl\  
app-arch/libarchive\  
dev-util/cmake\  
&& date --iso-8601=ns  
  
# 終了  

