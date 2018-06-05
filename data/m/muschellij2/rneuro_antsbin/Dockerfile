## Emacs, make this -*- mode: sh; -*-  
### RNEURO  
FROM muschellij2/rneuro_fsl  
  
ENV itkrrel=0.0.1  
RUN wget
https://github.com/stnava/ITKR/releases/download/latest/ITKR_${itkrrel}_R_x86_64-pc-
linux-gnu.tar.gz;  
RUN R CMD INSTALL ITKR_${itkrrel}_R_x86_64-pc-linux-gnu.tar.gz;  
RUN rm ITKR_${itkrrel}_R_x86_64-pc-linux-gnu.tar.gz;  
  
ENV ANTsRCorerel=0.0.0  
ENV reldir=untagged-a878f5e1fd9cffd7bb04  
ENV reldir=latest  
RUN wget
https://github.com/stnava/ANTsRCore/releases/download/${reldir}/ANTsRCore_${ANTsRCorerel}_R_x86_64-pc-
linux-gnu.tar.gz;  
RUN R CMD INSTALL ANTsRCore_${ANTsRCorerel}_R_x86_64-pc-linux-gnu.tar.gz;  
RUN rm ANTsRCore_${ANTsRCorerel}_R_x86_64-pc-linux-gnu.tar.gz;  
  
RUN r -e 'devtools::install_github("stnava/ANTsR", upgrade_dependencies =
FALSE)'  
  
RUN r -e 'devtools::install_github("muschellij2/extrantsr")'  

