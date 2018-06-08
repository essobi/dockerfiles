################################  
# Dockerfile: thedcg/tl-gentoo_prep6:latest  
  
# ベース  
FROM thedcg/tl-gentoo_prep5:latest  
  
################################  
# prep6/Dockerfile  
  
# 管理者  
#MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>  
  
# パッケージ  
RUN date --iso-8601=ns\  
&& emerge\  
app-eselect/eselect-opengl\  
app-eselect/eselect-mesa\  
dev-libs/boehm-gc\  
dev-libs/elfutils\  
dev-libs/libatomic_ops\  
dev-libs/libbsd\  
dev-libs/libpthread-stubs\  
dev-libs/libyaml\  
dev-util/ragel\  
media-fonts/font-util\  
media-gfx/imagemagick\  
virtual/libudev\  
x11-misc/util-macros\  
x11-proto/xproto\  
x11-proto/xextproto\  
x11-proto/xf86vidmodeproto\  
x11-proto/glproto\  
x11-proto/presentproto\  
x11-proto/dri3proto\  
&& date --iso-8601=ns  
  
# 終了  

