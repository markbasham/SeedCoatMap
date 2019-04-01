FROM continuumio/miniconda3

# set up work directory.
WORKDIR /home/me/dev/

# copy necessary files.
COPY ./* ./

# install packages.
RUN conda env create -f enviroment.yml

#Activate the enviroment
RUN /bin/bash -c "source activate main"

# run script.
ENTRYPOINT [ "python", "seedcoatmap.py"]
