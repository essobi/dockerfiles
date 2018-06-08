################################  
# Dockerfile: thedcg/tl-gentoo_prep7:latest  
  
# ベース  
FROM thedcg/tl-gentoo_prep6:latest  
  
################################  
# prep7/Dockerfile  
  
# 管理者  
#MAINTAINER Lemures Lemniscati <lemures.lemniscati@gmail.com>  
  
# パッケージ  
RUN date --iso-8601=ns\  
&& emerge\  
app-eselect/eselect-ruby\  
virtual/libelf\  
x11-libs/libXau\  
x11-libs/libxcb\  
x11-libs/libXdmcp\  
x11-libs/libpciaccess\  
x11-libs/libxshmfence\  
x11-libs/xtrans\  
x11-proto/dri2proto\  
x11-proto/damageproto\  
x11-proto/fixesproto\  
x11-proto/inputproto\  
x11-proto/kbproto\  
x11-proto/xcb-proto\  
x11-proto/xf86bigfontproto\  
x11-proto/xf86driproto\  
x11-libs/libdrm\  
x11-libs/libX11\  
&& date --iso-8601=ns  
  
# 終了  

