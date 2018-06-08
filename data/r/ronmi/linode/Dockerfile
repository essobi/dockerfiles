FROM debian:buster  
MAINTAINER Ronmi Ren <ronmi.ren@gmail.com>  
  
RUN export ver=buster \  
;( echo "deb http://mirrors.linode.com/debian/ ${ver} main contrib non-free" \  
; echo "deb-src http://mirrors.linode.com/debian/ ${ver} main contrib non-
free" \  
; echo "" \  
; echo "deb http://mirrors.linode.com/debian-security/ ${ver}/updates main
contrib non-free" \  
; echo "deb-src http://mirrors.linode.com/debian-security/ ${ver}/updates main
contrib non-free" \  
; echo "" \  
; echo "# ${ver}-updates, previously known as 'volatile'" \  
; echo "deb http://mirrors.linode.com/debian/ ${ver}-updates main contrib non-
free" \  
; echo "deb-src http://mirrors.linode.com/debian/ ${ver}-updates main contrib
non-free" \  
; echo "" \  
; echo "deb http://mirrors.linode.com/debian/ ${ver}-backports main contrib
non-free" \  
; echo "deb-src http://mirrors.linode.com/debian/ ${ver}-backports main
contrib non-free" )\  
| tee /etc/apt/sources.list  

