# Docker image with all necessary Homebrew and Ensembl taps, and the basic
dependencies  
FROM muffato/ensembl-basic-dependencies-linuxbrew  
  
# Close the Ensembl repos  
ARG ENSEMBL_INSTALL_DIR=/home/linuxbrew/repos  
RUN mkdir -p $ENSEMBL_INSTALL_DIR \  
&& git clone \--depth 1 https://github.com/Ensembl/ensembl.git
$ENSEMBL_INSTALL_DIR/ensembl \  
&& git clone \--depth 1 https://github.com/Ensembl/ensembl-compara.git
$ENSEMBL_INSTALL_DIR/ensembl-compara \  
&& git clone \--depth 1 https://github.com/Ensembl/ensembl-test.git
$ENSEMBL_INSTALL_DIR/ensembl-test \  
&& git clone \--branch master --depth 1 https://github.com/Ensembl/ensembl-
hive.git $ENSEMBL_INSTALL_DIR/ensembl-hive \  
&& git clone \--branch v1.6.x --depth 1 https://github.com/bioperl/bioperl-
live $ENSEMBL_INSTALL_DIR/bioperl-live \  
&& git clone \--branch release-1-6-9 --depth 1
https://github.com/bioperl/bioperl-run $ENSEMBL_INSTALL_DIR/bioperl-run  
  
# Install their requirements (CPAN)  
RUN sudo $ENSEMBL_INSTALL_DIR/ensembl-hive/docker/setup_os.Ubuntu-16.04.sh \  
&& sudo $ENSEMBL_INSTALL_DIR/ensembl-hive/docker/setup_cpan.Ubuntu-16.04.sh
$ENSEMBL_INSTALL_DIR/ensembl*  
  
# Setup the environment  
ENV PERL5LIB
"$ENSEMBL_INSTALL_DIR/ensembl/modules:$ENSEMBL_INSTALL_DIR/ensembl-
compara/modules:$ENSEMBL_INSTALL_DIR/ensembl-
test/modules:$ENSEMBL_INSTALL_DIR/ensembl-
hive/modules:$ENSEMBL_INSTALL_DIR/bioperl-live:$ENSEMBL_INSTALL_DIR/bioperl-
run/lib:$PERL5LIB"  
ENV PATH "$ENSEMBL_INSTALL_DIR/ensembl-hive/scripts:$PATH"  

