FROM tianon/perl  
RUN cpanm Perl::Critic  
COPY .perlcriticrc /etc/  
COPY .perltidyrc /etc/  
ENV PERLCRITIC /etc/.perlcriticrc  
ENV PERLTIDY /etc/.perltidyrc  

