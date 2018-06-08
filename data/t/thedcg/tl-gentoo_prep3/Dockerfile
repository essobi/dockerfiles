################################  
# Dockerfile: thedcg/tl-gentoo_prep3:latest  
  
# ベース  
FROM thedcg/tl-gentoo_prep2:latest  
  
################################  
# prep3/Dockerfile  
  
# 管理者  
#MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>  
  
# パッケージ  
RUN date --iso-8601=ns\  
&& emerge\  
x11-libs/pixman\  
app-eselect/eselect-fontconfig\  
app-eselect/eselect-pinentry\  
app-text/dvipsk\  
app-text/ghostscript-gpl\  
app-text/ps2pkm\  
dev-libs/icu\  
dev-libs/libtasn1\  
dev-libs/zziplib\  
dev-perl/Error\  
dev-perl/Digest-HMAC\  
dev-perl/Net-SSLeay\  
dev-perl/IPC-Run\  
dev-util/cmake\  
dev-tex/bibtexu\  
media-fonts/urw-fonts\  
media-libs/fontconfig\  
media-libs/freetype\  
media-libs/libjpeg-turbo\  
sys-devel/autogen\  
&& date --iso-8601=ns  
  
# 終了  

