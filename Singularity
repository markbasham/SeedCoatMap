Bootstrap: docker
From: continuumio/miniconda3
%files
./* ./

%post
# install packages.
/bin/bash conda env create -f /enviroment.yml

#Activate the enviroment
/bin/bash -c "source activate main"

%runscript
ls -l
exec python /src/seedcoatmap.py "$@"
