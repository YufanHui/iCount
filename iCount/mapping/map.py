"""
Call STAR to map reads to genome index and produce BAM file.

Calls STAR to map sequence reads to reference genome, by passing the
following parameters:

--runThreadN NumberOfThreads
--genomeDir /path/to/genomeDir
--readFilesIn /path/to/read1 [/path/to/read2]
--readFilesCommand gunzip -c
--sjdbGTFfile /path/to/ann.gtf
--outFileNamePrefix /path/to/output/dir/prefix
#--outSAMmapqUnique Integer0to255
--outSAMprimaryFlag AllBestScore
--outFilterMultimapNmax maxHits # default 10
--outFilterMismatchNmax # default 10
"""

import os
import logging

import iCount

LOGGER = logging.getLogger(__name__)


def run(sequences_fname, genomedir, outdir, annotation_fname='', multimax=50,
        mismatches=2, threads=1):
    """
    Map docstring... TODO

    Parameters
    ----------
    sequences_fname : str
        Sequencing reads to map to genome.
    genomedir : str
        Folder with genome index.
    outdir : str
        Output folder, where to store genome index.
    annotation_fname : str
        TODO
    multimax : int
        Number of allowed multiple hits.
    mismatches : int
        Number of allowed mismatches.
    threads : int
        Number of threads that STAR can use for generating index.

    Returns
    -------
    int
        Return code - TODO - will we cajenge this?
    """
    iCount.log_inputs(LOGGER, level=logging.INFO)

    if not os.path.isdir(genomedir):
        raise FileNotFoundError('Directory with genome index does not exist. Make sure it does.')
    if not os.path.isdir(outdir):
        raise FileNotFoundError('Output directory does not exist. Make sure it does.')
    return iCount.externals.star.map_reads(
        sequences_fname, genomedir,
        outdir,
        annotation=annotation_fname,
        multimax=multimax,
        mismatches=mismatches,
        threads=threads,
    )
