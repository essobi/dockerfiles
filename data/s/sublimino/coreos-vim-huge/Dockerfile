FROM tianon/gentoo:latest  
  
ENV VIM_VERSION=7.4.273  
RUN \  
mkdir /usr/portage && \  
emerge-webrsync && \  
EBUILD=/usr/portage/app-editors/vim/vim-${VIM_VERSION}.ebuild && \  
sed -e '/^IUSE=/!b' -e 's#\bacl\b##' -i "${EBUILD}" && \  
sed -e '/^[\t ]*acl\?/!b' -e '/sys-apps\/acl/d' -i "${EBUILD}" && \  
sed -e '/^[\t ]*myconf/!b' -e 's/$(use_enable acl)/--disable-acl/' -i
"${EBUILD}" && \  
ebuild "${EBUILD}" digest && \  
ebuild "${EBUILD}" fetch && \  
ebuild "${EBUILD}" unpack && \  
ebuild "${EBUILD}" compile && \  
ebuild "${EBUILD}" install && \  
ebuild "${EBUILD}" qmerge && \  
emerge app-editors/vim-core  
  
ADD install_vim.sh /opt/  
  
CMD ["/opt/install_vim.sh"]  

