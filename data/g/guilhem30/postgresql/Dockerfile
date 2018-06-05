FROM postgres:9.4  
RUN localedef -i fr_FR -c -f UTF-8 -A /usr/share/locale/locale.alias
fr_FR.UTF-8  
ENV LANG fr_FR.UTF-8  
ENV LANGUAGE fr_FR:fr  
ENV LC_ALL fr_FR.UTF-8  
RUN echo "Europe/Paris" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  

