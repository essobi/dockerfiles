### RNEURO with FSL
FROM muschellij2/rneuro_fsl

RUN r -e 'devtools::install_github("muschellij2/drammsr")'

RUN r -e 'devtools::install_github("muschellij2/extrantsr", upgrade_dependencies = FALSE)'

RUN r -e 'devtools::install_github("muschellij2/ichseg", upgrade_dependencies = FALSE)'

CMD ["bash"]

