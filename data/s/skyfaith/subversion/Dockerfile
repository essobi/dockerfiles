FROM marvambass/subversion  
RUN sed -i 's|AuthType Digest|AuthType Basic|g' /etc/apache2/mods-
enabled/dav_svn.conf  
RUN sed -i 's|Location \/svn\/|Location \/repo\/|g' /etc/apache2/mods-
enabled/dav_svn.conf  

